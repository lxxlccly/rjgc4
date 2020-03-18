'''诗词大赛'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import json
import eventlet
import random


class PoetGame(object):
    def __init__(self):
        self.question_amount = 10
        self.right_answer = []
        self.grade = 0
        self.questions = []

    def start(self):
        '''开始游戏'''
        for i in range(self.question_amount):
            self.get_question(i)
            self.answer_question()
            print('正确答案为：' + self.right_answer[i])

    def answer_question(self):
        '''回答问题'''
        eventlet.monkey_patch()
        with eventlet.Timeout(3, False):
            print('hhh')

    def get_sentence(self):
        '''获得一个诗句'''
        random_poet = random.randint(0, 57999)
        address = './poet/poet.song.' + str(int(random_poet // 1000 * 1000)) + '.json'
        with open(address, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            sentence_amount = len(load_dict[int(random_poet % 1000)]['paragraphs'])
            random_sentence = random.randint(0, sentence_amount - 1)
            sentences = re.findall(r'[\u4E00-\u9FA5]+',
                                  load_dict[int(random_poet % 1000)]['paragraphs'][random_sentence])
            random_sentence = random.randint(0, len(sentences) - 1)
            sentence = sentences[random_sentence]
        self.right_answer.append(sentence)
        words = re.findall(r'[\u4E00-\u9FA5]', sentence)
        self.questions.append(words)

    def get_disturb(self, number, len_sentence):
        '''获得对诗句进行干扰的汉字'''
        len_disturb = 12 - len_sentence
        for i in range(len_disturb):
            word = random.randint(0x4e00, 0x9fbf)
            self.questions[number].append(chr(word))

    def get_question(self, number):
        '''获得题目'''
        print('第%u题：' % int(number + 1))
        self.get_sentence()
        self.get_disturb(number, len(self.right_answer[number]))
        random.shuffle(self.questions[number])
        print(self.questions[number])

    def print_grade(self):
        '''打印成绩'''
        print(self.grade)


if __name__ == '__main__':
    game = PoetGame()
    game.start()

