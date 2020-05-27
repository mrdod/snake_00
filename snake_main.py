import os
import msvcrt
import random


def clear():
    os.system('cls')


def print_screen():
    clear()
    for y in range(9):
        for x in range(8):
            print(Snake.position[x + y * 8], end=' ')
        print(' ')
    print('Score:', Snake.score)
    print('Use wasd to move')


class Snake:
    position = []
    head = 9
    score = 0
    food = 28
    food_reached = False


# Init List
for x in range(8):
    Snake.position.append('-')
for x in range(7):
    for y in range(8):
        if y == 0 or y == 7:
            Snake.position.append('|')
        else:
            Snake.position.append(' ')
for x in range(8):
    Snake.position.append('-')

Snake.position[Snake.head] = 'O'
Snake.position[Snake.food] = '*'
print_screen()


while 1:
    char = msvcrt.getch().decode('ASCII')

    # Input Processor
    if char == 'd':
        if Snake.position[Snake.head + 1] == '*':
            Snake.food_reached = True

        if Snake.position[Snake.head + 1] != '|':
            Snake.position[Snake.head] = ' '
            Snake.head = Snake.head + 1
            Snake.position[Snake.head] = 'O'
    elif char == 'a':
        if Snake.position[Snake.head - 1] == '*':
            Snake.food_reached = True

        if Snake.position[Snake.head - 1] != '|':
            Snake.position[Snake.head] = ' '
            Snake.head = Snake.head - 1
            Snake.position[Snake.head] = 'O'
    elif char == 's':
        if Snake.position[Snake.head + 8] == '*':
            Snake.food_reached = True

        if Snake.position[Snake.head + 8] != '-':
            Snake.position[Snake.head] = ' '
            Snake.head = Snake.head + 8
            Snake.position[Snake.head] = 'O'
    elif char == 'w':
        if Snake.position[Snake.head - 8] == '*':
            Snake.food_reached = True

        if Snake.position[Snake.head - 8] != '-':
            Snake.position[Snake.head] = ' '
            Snake.head = Snake.head - 8
            Snake.position[Snake.head] = 'O'

    while Snake.food_reached:
        rand_num = random.randrange(64)

        if Snake.position[rand_num] == ' ':
            Snake.position[rand_num] = '*'
            Snake.food_reached = False
            Snake.score = Snake.score + 10

    print_screen()