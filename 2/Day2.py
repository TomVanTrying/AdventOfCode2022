from enum import IntEnum
from collections import namedtuple

EXAMPLE_GUIDE = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

class Result(IntEnum):
    LOSE = 0
    DRAW = 3
    WIN = 6

class Hand(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSOR  = 3

def decode_opponent(code_letter):
    if code_letter == 'A':
        return Hand.ROCK
    elif code_letter == 'B':
        return Hand.PAPER
    elif code_letter == 'C':
        return Hand.SCISSOR

def decode_player(code_letter):
    if code_letter == 'X':
        return Hand.ROCK
    elif code_letter == 'Y':
        return Hand.PAPER
    elif code_letter == 'Z':
        return Hand.SCISSOR

def decode_result_needed(code_letter):
    if code_letter == 'X':
        return Result.LOSE
    elif code_letter == 'Y':
        return Result.DRAW
    elif code_letter == 'Z':
        return Result.WIN


def play_game2(opponent_hand, result_must_be):
    score = 0

    # DRAW NEEDED
    if result_must_be == Result.DRAW:
        score = result_must_be + opponent_hand

    # WIN NEEDED
    elif result_must_be == Result.WIN:
        if opponent_hand == Hand.ROCK:
            score = result_must_be + Hand.PAPER
        elif opponent_hand == Hand.PAPER:
            score = result_must_be + Hand.SCISSOR
        elif opponent_hand == Hand.SCISSOR:
            score = result_must_be + Hand.ROCK

    # LOST NEEDED
    elif result_must_be == Result.LOSE:
        if opponent_hand == Hand.ROCK:
            score = result_must_be + Hand.SCISSOR
        elif opponent_hand == Hand.PAPER:
            score = result_must_be + Hand.ROCK
        elif opponent_hand == Hand.SCISSOR:
            score = result_must_be + Hand.PAPER

    return score

def play_game(opponent_hand, player_hand):

    # ROCK
    if player_hand == Hand.ROCK and opponent_hand == Hand.SCISSOR:
        player_result = Result.WIN
        opp_result = Result.LOSE
    elif player_hand == Hand.ROCK and opponent_hand == Hand.ROCK:
        player_result = Result.DRAW
        opp_result  = Result.DRAW
    elif player_hand == Hand.ROCK and opponent_hand == Hand.PAPER:
        player_result = Result.LOSE
        opp_result = Result.WIN

    # SCISSOR
    elif player_hand == Hand.SCISSOR and opponent_hand == Hand.PAPER:
        player_result = Result.WIN
        opp_result = Result.LOSE
    elif player_hand == Hand.SCISSOR and opponent_hand == Hand.SCISSOR:
        player_result = Result.DRAW
        opp_result  = Result.DRAW
    elif player_hand == Hand.SCISSOR and opponent_hand == Hand.ROCK:
        player_result = Result.LOSE
        opp_result = Result.WIN

    # PAPER
    elif player_hand == Hand.PAPER and opponent_hand == Hand.ROCK:
        player_result = Result.WIN
        opp_result = Result.LOSE
    elif player_hand == Hand.PAPER and opponent_hand == Hand.PAPER:
        player_result = Result.DRAW
        opp_result  = Result.DRAW
    elif player_hand == Hand.PAPER and opponent_hand == Hand.SCISSOR:
        player_result = Result.LOSE
        opp_result = Result.WIN

    player_score = player_hand + player_result
    opp_score = opponent_hand + opp_result

    return (player_score, opp_score)

def use_strategy(guide):
    rounds_player = []
    rounds_opponent = []

    for round in guide:
        opponent_hand = decode_opponent(round[0])
        player_hand = decode_player(round[1])
        player_score, opponent_score = play_game(opponent_hand, player_hand)
        rounds_player.append(player_score)
        rounds_opponent.append(opponent_score)

    return sum(rounds_player), sum(rounds_opponent)

def use_p2_strategy(guide):
    rounds_player = []

    for round in guide:
        opponent_hand = decode_opponent(round[0])
        result_needed = decode_result_needed(round[1])
        player_score = play_game2(opponent_hand, result_needed)
        rounds_player.append(player_score)

    print(rounds_player)

    return sum(rounds_player)

def part1():

    # guide = EXAMPLE_GUIDE

    # Get inputs into a list of lists
    with open('strategy.txt') as f:
        lines = f.read().splitlines()

    guide = []
    for line in lines:
        res = tuple(map(str, line.split(' ')))
        guide.append(res)

    player, opponent = use_strategy(guide)

    print(player)
    # print(opponent)

def part2():
    # guide = EXAMPLE_GUIDE

    # Get inputs into a list of lists
    with open('strategy.txt') as f:
        lines = f.read().splitlines()

    guide = []
    for line in lines:
        res = tuple(map(str, line.split(' ')))
        guide.append(res)

    player = use_p2_strategy(guide)
    print(player)

if __name__ == "__main__":
    # part1()
    part2()