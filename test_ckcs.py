'''出口成诗PoetGame的测试函数'''
from unittest import TestCase, mock
from ckcs import PoetGame
from itertools import chain
import json


class TestPoetGame(TestCase):
    '''类PoetGame的测试函数'''
    def setUp(self):
        self.poet_game = PoetGame()

    def test_start(self):
        '''start的测试函数
        都是调用，所以直接通过'''
        pass

    @mock.patch('builtins.input', new=mock.Mock(
        side_effect=chain(['1', '寥落古行宫，宫花寂寞红。', '2', '白头宫女在，閒坐说玄宗。',
                           '3', '白头宫女在，閒坐说玄宗。', '4', '白日依山尽，黄河入海流。',
                           '5', '白日依山尽，黄河入海流。', '6', '三日入厨下，洗手作羹汤。',
                           '7', '愿君多采撷，此物最相思。', '8', '红豆生南国，春来发几枝。',
                           '9', '君自故乡来，应知故乡事。', '10', '来日绮窗前，寒梅着花未？',
                           '11', '返景入深林，复照青苔上。', '12', '返景入深林，复照青苔上。'])))
    def test_cycle(self):
        self.poet_game.questions = ["行宫", "宫女", "玄宗", "白日", "黄河", "洗手",
                                    "相思", "红豆", "故乡", "寒梅", "深林", "青苔"]
        address = './poet/tssbs.json'
        with open(address, 'r', encoding='utf-8') as load_f:
            self.poet_game.all_poet = json.load(load_f)
        self.poet_game.cycle()
        self.assertEqual('寥落古行宫，宫花寂寞红。', self.poet_game.answers[0])
        self.assertEqual('白头宫女在，閒坐说玄宗。', self.poet_game.answers[1])
        self.assertEqual('白头宫女在，閒坐说玄宗。', self.poet_game.answers[2])
        self.assertEqual('白日依山尽，黄河入海流。', self.poet_game.answers[3])
        self.assertEqual('白日依山尽，黄河入海流。', self.poet_game.answers[4])
        self.assertEqual('三日入厨下，洗手作羹汤。', self.poet_game.answers[5])
        self.assertEqual('愿君多采撷，此物最相思。', self.poet_game.answers[6])
        self.assertEqual('红豆生南国，春来发几枝。', self.poet_game.answers[7])
        self.assertEqual('君自故乡来，应知故乡事。', self.poet_game.answers[8])
        self.assertEqual('来日绮窗前，寒梅着花未？', self.poet_game.answers[9])
        self.assertEqual('返景入深林，复照青苔上。', self.poet_game.answers[10])
        self.assertEqual('返景入深林，复照青苔上。', self.poet_game.answers[11])

    @mock.patch('random.randint', new=mock.Mock(side_effect=chain([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])))
    def test_get_question(self):
        self.poet_game.get_question()
        self.assertEqual("行宫", self.poet_game.questions[0])
        self.assertEqual("宫女", self.poet_game.questions[1])
        self.assertEqual("玄宗", self.poet_game.questions[2])
        self.assertEqual("白日", self.poet_game.questions[3])
        self.assertEqual("黄河", self.poet_game.questions[4])
        self.assertEqual("洗手", self.poet_game.questions[5])
        self.assertEqual("相思", self.poet_game.questions[6])
        self.assertEqual("红豆", self.poet_game.questions[7])
        self.assertEqual("故乡", self.poet_game.questions[8])
        self.assertEqual("寒梅", self.poet_game.questions[9])
        self.assertEqual("深林", self.poet_game.questions[10])
        self.assertEqual("青苔", self.poet_game.questions[11])

    def test_get_poet_library(self):
        self.poet_game.get_poet_library()
        self.assertEqual("行宫", self.poet_game.all_poet[0]["chapter"])
        self.assertEqual(["寥落古行宫，宫花寂寞红。", "白头宫女在，閒坐说玄宗。"],
                         self.poet_game.all_poet[0]["paragraphs"])
        self.assertEqual("塞下曲·野幕敞琼筵", self.poet_game.all_poet[len(self.poet_game.all_poet) - 1]["chapter"])
        self.assertEqual(["野幕敞琼筵，羌戎贺劳旋。", "醉和金甲舞，雷鼓动山川。"],
                         self.poet_game.all_poet[len(self.poet_game.all_poet) - 1]["paragraphs"])

    def test_print_grade(self):
        '''print_grade的测试函数'''
        self.poet_game.answers = ['一二三四五六七', '', '', '', '', '', '', '', '', '', '', '']
        with mock.patch('builtins.print') as mock1:
            self.poet_game.print_grade()
            mock1.assert_has_calls([
                mock.call('总结：'),
                mock.call(' 1、回答正确。您的回答为：一二三四五六七'),
                mock.call(' 2、回答错误/未回答。'),
                mock.call(' 3、回答错误/未回答。'),
                mock.call(' 4、回答错误/未回答。'),
                mock.call(' 5、回答错误/未回答。'),
                mock.call(' 6、回答错误/未回答。'),
                mock.call(' 7、回答错误/未回答。'),
                mock.call(' 8、回答错误/未回答。'),
                mock.call(' 9、回答错误/未回答。'),
                mock.call('10、回答错误/未回答。'),
                mock.call('11、回答错误/未回答。'),
                mock.call('12、回答错误/未回答。'),
                mock.call('您的总得分为：8.3分')
            ])
