#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import json
import eventlet


class PoetGame(object):
    def __init__(self):
        self.question_amount = 10
        self.right_answer = []
        self.grade = 0

    def start(self):
        for i in range(self.question_amount):
            self.get_question(i)
            self.answer_question()

    def answer_question(self):
        eventlet.monkey_patch()
        with eventlet.Timeout(3, False):
            print('hhh')

    def get_question(self, number):
        print('第%u题：' % int(number + 1))
        for i in range(58):
            address = './poet/poet.song.' + str(i * 1000) + '.json'
            with open(address, 'r', encoding='utf-8') as load_f:
                load_dict = json.load(load_f)
                print(load_dict[0]['author'])
                print(load_dict[0]['paragraphs'])
                res = re.findall(r'[\u4E00-\u9FA5]+', load_dict[0]['paragraphs'][0])
                print(res)
                print(load_dict[0]['title'])
                print(load_dict[0]['id'])

    def print_grade(self):
        print(self.grade)


if __name__ == '__main__':
    game = PoetGame()
    game.start()

