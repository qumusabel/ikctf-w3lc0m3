from random import randint
import signal


def generate(lvl):
    if lvl == 20:
        return "(22/5) + 75 * 200 ** 2 -25 * 0.25 + 13 ** 2", 3000167.15

    num = [str(randint(1, 100)) for i in range(-(-lvl // 4) + 1)]
    signs = [['+', '-', '*', '/'][randint(0, 3)] for i in range(-(-lvl // 4))]
    question = ' '.join(num)
    for i in signs:
        question = question.replace(' ', i, 1)
    return question, eval(question)


FLAG = "IKC{38_pythons_54dfd4}"


if __name__ == '__main__':
    #signal.alarm(30)
    print("ALL RIGHT HERE WE GO!!!")

    i = 1
    while i <= 20:
        print(i, end='. ')
        quest, answ = generate(i+1)

        if len(str(answ).split('.')[1]) > 6:
            # print('hard', quest, '=', answ)
            continue

        print(quest, end=' = ')
        if input() == str(answ).strip().replace(',', '.'):
            print("Correct!")
        else:
            print("Wrong :-(")
            quit(0)
        i += 1

    print('W3ll d0n3!', FLAG)
