#!/usr/bin/env python3

from random import randint, choice
import signal


def _kill():
    print("\nYour time's up!")
    import os
    os._exit(0)


def generate(lvl):
    if lvl == 20:
        return "(22/5) + 75 * 200 ** 2 -25 * 0.25 + 13 ** 2", 3000167.15

    num = [str(choice(range(1,100))) for i in range(-(-lvl // 4) + 1)]
    signs = [choice(['+', '-', '*', '/']) for i in range(-(-lvl // 4))]
    question = ' '.join(num)
    for i in signs:
        question = question.replace(' ', i, 1)
    return question, eval(question)


FLAG = "IKC{38_pythons_54dfd4}"


if __name__ == '__main__':
    import threading
    kill = threading.Timer(30.0, _kill)
    kill.start()
    del threading
    print("ALL RIGHT HERE WE GO!!!")

    i = 1
    while i <= 20:
        quest, answ = generate(i+1)

        # Detecting long floats
        if type(answ) == float:
            if len(str(answ).split('.')[1]) > 6:
                # print('hard', quest, '=', answ)
                continue

        print(quest)

        if input() != str(answ).strip().replace(',', '.'):
            print('Wrong :(')
            exit(0)

        i += 1

    print('W3ll d0n3!', FLAG)
