import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout

from game import play_game, main


class TestMysteryIsland(unittest.TestCase):

    def test_player_can_quit_game(self):
        with patch("builtins.input", side_effect=["Sanctus", "11"]):
            result = play_game()

        self.assertFalse(result)

    def test_player_starts_at_beach_with_five_energy_and_empty_inventory(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn("Current location: Beach", game_output)
        self.assertIn("Energy: 5", game_output)
        self.assertIn("Inventory: []", game_output)

    def test_legal_movement_reduces_energy_by_one(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "2", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn("Current location: Jungle", game_output)
        self.assertIn("Energy: 4", game_output)

    def test_rejected_movement_does_not_change_location_or_energy(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "4", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn("Current location: Beach", game_output)
        self.assertIn("Energy: 5", game_output)

    def test_replay_resets_player_state(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            # First game: complete a winning journey
            "First Player", "1", "1", "2", "3", "1",
            "4", "5", "1", "6", "7", "8", "9",

            # Agree to replay
            "yes",

            # Second game: check fresh state and quit
            "Second Player", "10", "11"
        ]):
            with redirect_stdout(output):
                main()

        game_output = output.getvalue()

        self.assertIn("Welcome, Second Player!", game_output)
        self.assertIn("Current location: Beach", game_output)
        self.assertIn("Energy: 5", game_output)
        self.assertIn("Inventory: []", game_output)

    def test_player_cannot_cross_bridge_without_rope(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "2", "4", "5", "2",
            "7", "8", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn(
            "You cannot cross the bridge without a rope!",
            game_output
        )
        self.assertIn("Energy: 2", game_output)

    def test_player_can_collect_rope(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "1", "1", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        self.assertIn("Inventory: ['rope']", output.getvalue())

    def test_player_can_collect_lantern(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "2", "3", "1", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn("lantern", game_output.lower())
        self.assertIn("Inventory: ['lantern']", game_output)

    def test_player_cannot_collect_rope_twice(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "1", "1", "1", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn("Inventory: ['rope']", game_output)
        self.assertNotIn("Inventory: ['rope', 'rope']", game_output)

    def test_player_cannot_collect_lantern_twice(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "2", "3", "1", "3", "10", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn("Inventory: ['lantern']", game_output)
        self.assertNotIn(
            "Inventory: ['lantern', 'lantern']",
            game_output
        )

    def test_player_cannot_light_lighthouse_without_lantern(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "1", "1", "2", "4", "5",
            "2", "7", "8", "9", "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue().lower()

        self.assertIn("lantern", game_output)

    def test_player_can_win_game(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "1", "1", "2", "3", "1",
            "4", "5", "1", "6", "7", "8", "9"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue().lower()

        self.assertIn("congratulations", game_output)
        self.assertIn("lighthouse", game_output)

    def test_player_loses_when_energy_reaches_zero(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus", "1", "1", "2", "4", "5",
            "1", "7", "8"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue().lower()

        self.assertIn("game over", game_output)
        self.assertNotIn("energy: -1", game_output)

    def test_invalid_menu_input_does_not_consume_energy(self):
        output = io.StringIO()

        with patch("builtins.input", side_effect=[
            "Sanctus",
            "abc",
            "10",
            "11"
        ]):
            with redirect_stdout(output):
                play_game()

        game_output = output.getvalue()

        self.assertIn("Invalid", game_output)
        self.assertIn("Energy: 5", game_output)


if __name__ == "__main__":
    unittest.main()
