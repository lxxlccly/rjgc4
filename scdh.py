'''诗词大赛'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import json
import time
import random
import langconv
import time_limit

LIMIT_TIME = 60


class PoetGame(object):
    '''诗词大赛函数'''
    def __init__(self):
        self.question_amount = 10
        self.right_answer = []
        self.answers = []
        self.grade = 0
        self.questions = []

    def start(self):
        '''开始游戏'''
        for i in range(self.question_amount):
            print('当前得分：%u' % self.grade)
            self.get_question(i)
            a_threading = time_limit.MyThread(target=self.answer_question)
            a_threading.start()
            #time.sleep(LIMIT_TIME) 这两句做界面的时候用
            #a_threading.stop()
            a_threading.join()
            if a_threading.get_result() == 0:
                self.answers.append('')
            if self.answers[i] == self.right_answer[i]:
                print('回答正确')
                self.grade += 100/self.question_amount
            else:
                print('回答错误，正确答案为：' + self.right_answer[i])
        self.print_grade()

    @time_limit.limit_decor(LIMIT_TIME)  # 超时设置(s)
    def answer_question(self):
        '''回答问题'''
        print('请输入答案：')
        answer = input()
        self.answers.append(answer)
        return 1

    def get_sentence(self):
        '''获得一个诗句

        #从58000首诗里随机获取题目的代码
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
        '''
        #从唐诗三百首里随机获取题目的代码
        address = './poet/tangshisanbaishou.json'
        with open(address, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            all_poet = []
            for i in range(len(load_dict['content'])):
                all_poet = all_poet + load_dict['content'][i]['content']
        random_poet = random.randint(0, len(all_poet) - 1)
        sentence_amount = len(all_poet[random_poet]['paragraphs'])
        random_sentence = random.randint(0, sentence_amount - 1)
        sentences = re.findall(r'[\u4E00-\u9FA5]+',
                               all_poet[random_poet]['paragraphs'][random_sentence])
        if len(sentences) == 0:
            random_sentence = 0
        else:
            random_sentence = random.randint(0, len(sentences) - 1)
        sentence = sentences[random_sentence]
        sentence = langconv.Converter('zh-hans').convert(sentence)
        self.right_answer.append(sentence)
        words = re.findall(r'[\u4E00-\u9FA5]', sentence)
        self.questions.append(words)

    def get_disturb(self, number, len_sentence):
        '''获得对诗句进行干扰的汉字'''
        len_disturb = 12 - len_sentence
        i = 0
        while i < len_disturb:
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xfe)
            val = f'{head:x} {body:x}'
            word = bytes.fromhex(val).decode('gb2312', errors='ignore') #或者用decode('gbk')
            self.questions[number].append(word)
            i += 1

    def get_question(self, number):
        '''获得题目'''
        print('第%u题：' % int(number + 1))
        self.get_sentence()
        self.get_disturb(number, len(self.right_answer[number]))
        random.shuffle(self.questions[number])
        print(self.questions[number])

    def print_grade(self):
        '''打印成绩'''
        print('总结：')
        for i in range(len(self.right_answer)):
            if self.answers[i] == self.right_answer[i]:
                print('{0:>2}、回答正确。您的回答：{1}；正确答案：{2}'
                      .format(i + 1, self.answers[i], self.right_answer[i]))
            else:
                print('{0:>2}、回答错误。您的回答：{1}；正确答案：{2}'
                      .format(i + 1, self.answers[i], self.right_answer[i]))
        print('您的总得分为：%s分' % str(self.grade))


if __name__ == '__main__':
    game = PoetGame()
    game.start()