'''
Tests for my CISC108 final project.

Change log:
  - 0.0.1: Initial version
'''

__VERSION__ = '0.0.1'

from cisc108 import assert_equal
from cisc108_game import assert_type

################################################################################
# Game import
# Rename this to the name of your project file.
from project_starter import *

def make_test_world()-> World:
    return {
    'user choice': None,
    'cpu choice': None,
    'score': 0,
    'Won?': None,
    'attempts': 0
}

#I am testing every function that isn't drawing something.
    
################################################################################
## random_number()

# this function is supposed to generate a number from 1 to 3
for i in range(4):
    assert_equal(random_number()<= 0, False)
    assert_equal(1<= random_number()<= 3, True)
    assert_equal(3<random_number(),False)

#################################################################################
## handle_key()

#this function handle's how the world will respond to users
#key stoke

TEST_WORLD = make_test_world()

#sees if pressing 1 will change the user choice to santa and attempts will increase
handle_key(TEST_WORLD, ord('1'))
assert_equal(TEST_WORLD['user choice'],'santa')
assert_equal(TEST_WORLD['attempts'],1)

#sees if pressing 2 will change the user choice to reindeer
handle_key(TEST_WORLD, ord('2'))
assert_equal(TEST_WORLD['user choice'],'reindeer')
assert_equal(TEST_WORLD['attempts'],2)

#sees if pressing 2 will change the user choice to reindeer
handle_key(TEST_WORLD, ord('3'))
assert_equal(TEST_WORLD['user choice'],'snowman')
assert_equal(TEST_WORLD['attempts'],3)

#####################################################################################
## assign_number()
#this function assigns a number to a option and changes the cpu choice according
#santa = 1, reindeer = 2, snowman = 3

TEST_WORLD = make_test_world()

#sees if the number 1 will change the cpu option to santa in world
assign_number(TEST_WORLD, 1)
assert_equal(TEST_WORLD['cpu choice'],'santa')

#sees if the number 2 will change the cpu option to reindeer in world
assign_number(TEST_WORLD, 2)
assert_equal(TEST_WORLD['cpu choice'],'reindeer')

#sees if the number 3 will change the cpu option to snowman in world
assign_number(TEST_WORLD, 3)
assert_equal(TEST_WORLD['cpu choice'],'snowman')

#####################################################################################
## win_point()
#This function adds a point to the score if the user beat the computer in the game
#Santa beats snowman, snowman beats reindeer, reindeer beats santa

TEST_WORLD = make_test_world()

#sees if santa(user) does beat snowman(cpu) and if the the score changes with 'won?'
#and vise versa
TEST_WORLD['user choice'] = 'santa'
TEST_WORLD['cpu choice'] = 'snowman'
win_point(TEST_WORLD)
assert_equal(TEST_WORLD['Won?'],'Win')
assert_equal(TEST_WORLD['score'], 1)
TEST_WORLD['cpu choice'] = 'santa'
TEST_WORLD['user choice'] = 'snowman'
win_point(TEST_WORLD)
assert_equal(TEST_WORLD['Won?'],'Did not win')
assert_equal(TEST_WORLD['score'], 1)

#sees if snowman(user) does beat reindeer(cpu) and if the the score changes with 'won?'
#and vise versa
TEST_WORLD['user choice'] = 'snowman'
TEST_WORLD['cpu choice'] = 'reindeer'
win_point(TEST_WORLD)
assert_equal(TEST_WORLD['Won?'],'Win')
assert_equal(TEST_WORLD['score'], 2)
TEST_WORLD['cpu choice'] = 'snowman'
TEST_WORLD['user choice'] = 'reindeer'
win_point(TEST_WORLD)
assert_equal(TEST_WORLD['Won?'],'Did not win')
assert_equal(TEST_WORLD['score'], 2)


#sees if reindeer(user) does beat santa(cpu) and if the the score changes with 'won?'
#and vise versa
TEST_WORLD['user choice'] = 'reindeer'
TEST_WORLD['cpu choice'] = 'santa'
win_point(TEST_WORLD)
assert_equal(TEST_WORLD['Won?'],'Win')
assert_equal(TEST_WORLD['score'], 3)
TEST_WORLD['cpu choice'] = 'reindeer'
TEST_WORLD['user choice'] = 'santa'
win_point(TEST_WORLD)
assert_equal(TEST_WORLD['Won?'],'Did not win')
assert_equal(TEST_WORLD['score'], 3)

#sees if snowman does beat snowman and if the the score changes with 'won?'
TEST_WORLD['user choice'] = 'snowman'
TEST_WORLD['cpu choice'] = 'snowman'
win_point(TEST_WORLD)
assert_equal(TEST_WORLD['Won?'],'Did not win')
assert_equal(TEST_WORLD['score'], 3)






