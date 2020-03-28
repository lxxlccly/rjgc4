'''点字成诗PoetGame的测试函数'''
from unittest import TestCase, mock
from dzcs import PoetGame
import langconv
from itertools import chain, cycle
import json


class TestPoetGame(TestCase):
    '''类PoetGame的测试函数'''
    def setUp(self):
        self.poet_game = PoetGame()

    def test_start(self):
        '''start的测试函数'''
        pass

    @mock.patch('builtins.input', new=mock.Mock(return_value='一二三四五六七'))
    def test_answer_question(self):
        self.poet_game.answer_question()
        self.assertEqual('一二三四五六七', self.poet_game.answers[0])

    @mock.patch('random.randint', new=mock.Mock(side_effect=chain(cycle([0, 0]))))
    def test_get_sentence(self):
        '''get_sentence的测试函数'''
        self.poet_game.get_sentence()
        self.assertEqual(langconv.Converter('zh-hans').convert('寥落古行宮'),
                         self.poet_game.right_answer[len(self.poet_game.right_answer)-1], '不匹配')

    def test_get_disturb(self):
        '''get_disturb的测试函数'''
        address = './poet/tssbs.json'  # 从唐诗三百首里随机获取题目的代码
        with open(address, 'r', encoding='utf-8') as load_f:
            self.poet_game.all_poet = json.load(load_f)
        self.poet_game.questions.append([])
        self.poet_game.get_disturb(0, 7)
        self.assertEqual(5, len(self.poet_game.questions[0]), '字的数目不符')

    def test_get_question(self):
        '''get_question的测试函数'''
        self.poet_game.get_question(0)
        self.assertEqual(12, len(self.poet_game.questions[0]), '字的数目不符')

    def test_print_grade(self):
        '''print_grade的测试函数'''
        self.poet_game.answers = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        self.poet_game.right_answer = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        self.poet_game.grade = 100
        with mock.patch('builtins.print') as mock1:
            self.poet_game.print_grade()
            mock1.assert_has_calls([
                mock.call('总结：'),
                mock.call(' 1、回答正确。您的回答：一；正确答案：一'),
                mock.call(' 2、回答正确。您的回答：二；正确答案：二'),
                mock.call(' 3、回答正确。您的回答：三；正确答案：三'),
                mock.call(' 4、回答正确。您的回答：四；正确答案：四'),
                mock.call(' 5、回答正确。您的回答：五；正确答案：五'),
                mock.call(' 6、回答正确。您的回答：六；正确答案：六'),
                mock.call(' 7、回答正确。您的回答：七；正确答案：七'),
                mock.call(' 8、回答正确。您的回答：八；正确答案：八'),
                mock.call(' 9、回答正确。您的回答：九；正确答案：九'),
                mock.call('10、回答正确。您的回答：十；正确答案：十'),
                mock.call('您的总得分为：100分')
            ])
