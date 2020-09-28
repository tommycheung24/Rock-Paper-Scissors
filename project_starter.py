"""
<Describe your game here. Remove the angle brackets.>

Change log:
  - 0.0.2: Added support for handle_release
  - 0.0.1: Initial version
"""
__VERSION__ = "0.0.2"

import arcade, math, random
from cisc108_game import Cisc108Game

################################################################################
## Game Constants

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.ALIZARIN_CRIMSON
GAME_TITLE = "Santa Reindeer Snowman"


SANTA = arcade.load_texture("santa claus.png")
REINDEER = arcade.load_texture("reindeer.png")
SNOWMAN = arcade.load_texture("snowman2.png")

################################################################################
## Helper definitions
def random_number() -> int:
    """
    Returns a random number between 1 and 3
    Args:
    Returns:
        (int): a randon number
    """
    return random.randint(1, 3)


################################################################################
## Record definitions

World = {
    # the choice the the user pick between santa, reindeer, snowman
    "user choice": str,
    # the choice of the computer
    "cpu choice": str,
    # how many times the user won
    "score": int,
    # if the user won the round or not
    "Won?": str,
    # the number of attempts
    "attempts": int,
}

INITIAL_WORLD = {
    "user choice": None,
    "cpu choice": None,
    "score": 0,
    "Won?": None,
    "attempts": 0,
}


################################################################################
# Drawing functions
def draw_instruction():
    """
    Draws the text on the page, this includes the directions of the game, name of the game, and the rules of the game.
    
    """
    arcade.draw_text(
        "This is a game of Santa, Reindeer, Snowman", 0, 50, arcade.color.WHITE, 15
    )
    arcade.draw_text(
        "Santa beats snowman, snowman beats reindeer, reindeer beats santa",
        0,
        30,
        arcade.color.WHITE,
        13,
    )
    arcade.draw_text(
        "Press button 1 for santa, 2 for reindeer, and 3 for snowman",
        0,
        10,
        arcade.color.WHITE,
        15,
    )
    arcade.draw_text(
        "User Choice", WINDOW_WIDTH - 175, WINDOW_HEIGHT - 60, arcade.color.WHITE, 15
    )
    arcade.draw_text("CPU Choice", 75, WINDOW_HEIGHT - 60, arcade.color.WHITE, 15)


def draw_score(score: int):
    """
    Draws the player's current score in the top-left corner of the
    screen.
    
    Args:
        score (int): The player's current score.
    """
    arcade.draw_text(
        "Number of Wins: " + str(score), 0, WINDOW_HEIGHT - 30, arcade.color.WHITE, 20
    )


def draw_attempts(attempts: int):
    """
    Draws the player's current attempts in the top-right corner of the
    screen.
    
    Args:
        attempts (int): The player's total attempts.
    """
    arcade.draw_text(
        "Attempts: " + str(attempts), 350, WINDOW_HEIGHT - 30, arcade.color.WHITE, 20
    )


def draw_round_result(result: str):
    """
    Draws the result of the round(if the user won or not) also
    it gives the user the information of what will happen
    if they press key, 1,2, or 3
    """
    if result == "Win":
        arcade.draw_text(
            "YOU HAVE WON THIS ROUND!!!", 10, WINDOW_HEIGHT / 2, arcade.color.WHITE, 30
        )
        arcade.draw_text(
            "Pressing button 1, 2, or 3 will automatically start the next round",
            0,
            3 / 8 * WINDOW_HEIGHT,
            arcade.color.WHITE,
            15,
        )
    elif result == "Did not win":
        arcade.draw_text(
            "You have not won this round. \nPressing button 1, 2, or 3 will automatically start the next round",
            0,
            WINDOW_HEIGHT / 2,
            arcade.color.WHITE,
            15,
        )


def draw_option(x: int, y: int, option: str):
    """
    Draws a picture of either santa, reindeer, or scissor on the desired location  
    Args:
        x(int): the x position on screen
        y(int): the y position on screen
        option(str): the option of santa, reindeer, or scissor
    """
    if option == "santa":
        arcade.draw_texture_rectangle(x, y, SANTA.height / 35, SANTA.width / 35, SANTA)
    if option == "snowman":
        arcade.draw_texture_rectangle(
            x, y, SNOWMAN.height / 4, SNOWMAN.width / 4, SNOWMAN
        )
    if option == "reindeer":
        arcade.draw_texture_rectangle(
            x, y, REINDEER.height / 5, REINDEER.width / 5, REINDEER
        )


def draw_world(world: World):
    """
    The world will draw the 3 options of santa, reindeer, and snowman on the lower part of the window.
    Will also draw out some instructions on what game it is, the buttons to press, and
    the the rule of the game. Also draw what the user input and the computer generated
    input. Also draws the score that the user have and the number of attempts
    
    Args:
        world (World): The current world to draw
    """
    draw_option(1 / 4 * WINDOW_WIDTH, 1 / 4 * WINDOW_HEIGHT, "santa")
    draw_option(1 / 2 * WINDOW_WIDTH, 1 / 4 * WINDOW_HEIGHT, "snowman")
    draw_option(3 / 4 * WINDOW_WIDTH, 1 / 4 * WINDOW_HEIGHT, "reindeer")
    draw_option(3 / 4 * WINDOW_WIDTH, 3 / 4 * WINDOW_HEIGHT, world["user choice"])
    draw_option(1 / 4 * WINDOW_WIDTH, 3 / 4 * WINDOW_HEIGHT, world["cpu choice"])
    draw_instruction()
    draw_score(world["score"])
    draw_round_result(world["Won?"])
    draw_attempts(world["attempts"])


################################################################################
# World manipulating functions


def update_world(world: World):
    """
    <Describe what happens every update.>
    
    Args:
        world (World): The current world to update.
    """


def handle_key(world: World, key: int):
    """
    If the user hit the key 1,2, or 3 then a picture of santa,reindeer, or snowman
    will pop out respectively. When the user hit one of those keys, the computer
    will also randomly pick of the three options too. Then win_point() will
    be called to see if the user won or not. 
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the pressed keyboard key (use ord and chr).
    """
    if key == ord("1"):
        world["user choice"] = "santa"
    elif key == ord("2"):
        world["user choice"] = "reindeer"
    elif key == ord("3"):
        world["user choice"] = "snowman"
    if key == ord("1") or key == ord("2") or key == ord("3"):
        world["attempts"] += 1
        assign_number(world, random_number())
        win_point(world)


def assign_number(world: World, number: int):
    """
    Assigns the three options to a number(santa-1, reindeer-2, snowman-3) and
    changes the cpu option in the world accordingly
    Args:
        number(int): the number that is given
        world(World): the current state of the world
    """
    if number == 1:
        world["cpu choice"] = "santa"
    elif number == 2:
        world["cpu choice"] = "reindeer"
    elif number == 3:
        world["cpu choice"] = "snowman"


def win_point(world: World):
    """
    Increase the player's score if the player win. Santa beats snowman,
    snowman beats reindeer, reindeer beats santa. Everything else will not
    be considered a win.
    Args:
        world(World): Current state of the World
    """
    if world["user choice"] == "santa" and world["cpu choice"] == "snowman":
        world["score"] += 1
        world["Won?"] = "Win"
    elif world["user choice"] == "snowman" and world["cpu choice"] == "reindeer":
        world["score"] += 1
        world["Won?"] = "Win"
    elif world["user choice"] == "reindeer" and world["cpu choice"] == "santa":
        world["score"] += 1
        world["Won?"] = "Win"
    else:
        world["Won?"] = "Did not win"


def handle_mouse(world: World, x: int, y: int, button: str):
    """
    <Describe how your game responds to mouse clicks.>
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of the mouse when the button was clicked.
        y (int): The y-coordinate of the mouse when the button was clicked.
        button (str): The button that was clicked ('left', 'right', 'middle')
    """


def handle_motion(world: World, x: int, y: int):
    """
    <Describe how your game responds to the mouse being moved.>
    
    Args:
        world (World): Current state of the world.
        x (int): The x-coordinate of where the mouse was moved to.
        y (int): The x-coordinate of where the mouse was moved to.
    """


def handle_release(world: World, key: int):
    """
    <Describe how your game responds to releasing a keyboard key.>
    
    Args:
        world (World): Current state of the world.
        key (int): The ASCII value of the released keyboard key (use ord and chr).
    """


############################################################################
# Set up the game
# Don't need to change any of this

if __name__ == "__main__":
    Cisc108Game(
        World,
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        GAME_TITLE,
        INITIAL_WORLD,
        draw_world,
        update_world,
        handle_key,
        handle_mouse,
        handle_motion,
        handle_release,
    )
    arcade.set_background_color(BACKGROUND_COLOR)
    arcade.run()
