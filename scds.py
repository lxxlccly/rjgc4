'''诗词大赛主程序'''
import tkinter
import ckcs
import time_limit


class SayPoet(object):
    '''出口成诗游戏'''
    def __init__(self):
        self.say_poet_interface = None
        self.say_poet = ckcs.PoetGame()
        self.exiting = 0

    def run(self):
        '''出口成诗运行函数'''
        global mode_select_interface
        mode_select_interface.destroy()
        self.say_poet.get_question()
        self.say_poet.get_poet_library()
        a_threading = time_limit.MyThread(target=self.cycle)
        a_threading.start()
        a_threading.join()
        self.show_grade()

    @time_limit.limit_decor(10)  # 超时设置(s)
    def cycle(self):
        '''定时循环'''
        answer_unfinished = 1
        while answer_unfinished:
            self.say_poet_display()
            if self.say_poet.unanswered == [0] * self.say_poet.question_amount:
                answer_unfinished = 0
            if self.exiting == 1:
                break
        return 1

    def say_poet_display(self):
        '''出口成诗界面'''
        self.say_poet_interface = tkinter.Tk()
        self.say_poet_interface.title("出口成诗")
        self.say_poet_interface.geometry("400x400+500+150")
        for i in range(4):
            for j in range(3):
                question_button = tkinter.Button(self.say_poet_interface, text=self.say_poet.questions[i*3+j],
                                                 font=('楷体', 18), activeforeground='red', command=self.exit_say_poet)
                question_button.place(relwidth=0.3, relheight=0.1, relx=j*0.35, rely=i*0.12+0.02)
        exit0 = tkinter.Button(self.say_poet_interface, text="退出游戏", font=('楷体', 18),
                               activeforeground='red', command=self.exit_say_poet)
        exit0.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0.9)
        back0 = tkinter.Button(self.say_poet_interface, text="返回首页", font=('楷体', 18),
                               activeforeground='red', command=self.back_mode_selection)
        back0.place(relwidth=0.3, relheight=0.1, relx=0, rely=0.9)
        self.say_poet_interface.protocol("WM_DELETE_WINDOW", self.exit_say_poet)
        self.say_poet_interface.mainloop()

    def show_grade(self):
        '''显示回答情况和最终得分'''
        pass

    def exit_say_poet(self):
        '''出口成诗界面的退出游戏函数'''
        global is_running
        is_running = False
        self.say_poet_interface.destroy()
        self.exiting = 1

    def back_mode_selection(self):
        '''出口成诗界面返回游戏模式选择界面的函数'''
        self.say_poet_interface.destroy()
        self.exiting = 1


class ClickPoet(object):
    def __init__(self):
        self.click_poet = None

    def run(self):
        '''点字成诗运行函数'''
        global mode_select_interface
        mode_select_interface.destroy()

    def click_poet_display(self):
        '''点字成诗界面'''


class ModeSelection(object):
    '''诗词大赛游戏'''
    def start(self):
        '''开始游戏'''
        global is_running
        while is_running:
            self.selection()

    def selection(self):
        '''模式选择界面'''
        saying_poet = SayPoet()
        clicking_poet = ClickPoet()
        global is_running, mode_select_interface
        if is_running:
            mode_select_interface = tkinter.Tk()
            mode_select_interface.title("游戏模式选择")
            mode_select_interface.geometry("400x400+500+150")
            mode1 = tkinter.Button(mode_select_interface, text="出口成诗", font=('楷体', 18),
                                   activeforeground='blue', command=saying_poet.run)
            mode1.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.2)
            mode2 = tkinter.Button(mode_select_interface, text="点字成诗", font=('楷体', 18),
                                   activeforeground='blue', command=clicking_poet.run)
            mode2.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.4)
            exit0 = tkinter.Button(mode_select_interface, text="退出游戏", font=('楷体', 18),
                                   activeforeground='red', command=self.exit_mode_select)
            exit0.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.6)
            mode_select_interface.protocol("WM_DELETE_WINDOW", self.exit_mode_select)
            mode_select_interface.mainloop()

    def exit_mode_select(self):
        '''模式选择界面的退出游戏函数'''
        global mode_select_interface, is_running
        is_running = False
        mode_select_interface.destroy()


if __name__ == '__main__':
    mode_select_interface = None
    is_running = True
    game = ModeSelection()
    game.start()
    print('游戏结束')
