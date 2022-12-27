""" This file contains the Tkinter classes for the Othello game. It mainly displays the game state.

    Contains the GameBoard, Players, Score
"""

import os.path
import othello

PLAYERS = {othello.BLACK: 'Black', othello.WHITE: 'White'}

class GameBoard:
    def __init__(self, game_state: othello.OthelloGame) -> None:
        # Initialize the game board's settings here
        self._game_state = game_state
        self._rows = self._game_state.get_rows()
        self._cols = self._game_state.get_columns()

    def new_game_settings(self, game_state) -> None:
        """ The game board's new game settings is now changed accordingly to
            the specified game state """
        self._game_state = game_state
        self._rows = self._game_state.get_rows()
        self._cols = self._game_state.get_columns()


    def update_game_state(self, game_state: othello.OthelloGame) -> None:
        """ Updates our current _game_state to the specified one in the argument """
        self._game_state = game_state

    def get_rows(self) -> int:
        """ Returns the total number of rows in the board """
        return self._rows

    def get_columns(self) -> int:
        """ Returns the total number of rows in the board """
        return self._cols


class Player:
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        """ Returns the player's name """
        return self._name


class Score:
    def __init__(self, color: str, game_state: othello.OthelloGame) -> None:
        """ Initializes the score label """
        self._player = color
        self._score = game_state.get_scores(self._player)

    def update_score(self, game_state: othello.OthelloGame) -> None:
        """ Updates the score with the specified game state """
        self._score = game_state.get_scores(self._player)

    def get_score(self) -> int:
        """ Returns the score """
        return self._score

class Turn:
    def __init__(self, game_state: othello.OthelloGame) -> None:
        """ Initializes the player's turn Label """
        self._player = game_state.get_turn()

    def switch_turn(self, game_state: othello.OthelloGame) -> None:
        """ Switch's the turn between the players """
        self._player = game_state.get_turn()

    def update_turn(self, turn: str) -> None:
        """ Updates the turn to whatever the current game state's turn is """
        self._player = turn

    def _opposite_turn(self) -> None:
        """ Returns the opposite turn of current turn """
        return {othello.BLACK: othello.WHITE, othello.WHITE: othello.BLACK}[self._player]