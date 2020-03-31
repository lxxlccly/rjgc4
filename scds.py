'''诗词大赛主程序'''
import tkinter


class Game(object):
    '''诗词大赛游戏'''
    def __init__(self):
        self.is_running = True
        self.mode_select = None

    def start(self):
        '''开始游戏'''
        while self.is_running:
            self.selection()

    def selection(self):
        '''模式选择界面'''
        if self.is_running:
            self.mode_select = tkinter.Tk()
            self.mode_select.title("游戏模式选择")
            self.mode_select.geometry("400x400+500+150")
            mode1 = tkinter.Button(self.mode_select, text="出口成诗", font=('楷体', 18),
                                   activeforeground='blue', command=self.c_k_c_s)
            mode1.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.2)
            mode2 = tkinter.Button(self.mode_select, text="点字成诗", font=('楷体', 18),
                                   activeforeground='blue', command=self.d_z_c_s)
            mode2.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.4)
            exit0 = tkinter.Button(self.mode_select, text="退出游戏", font=('楷体', 18),
                                   activeforeground='red', command=self.exit_mode_select)
            exit0.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.6)
            self.mode_select.protocol("WM_DELETE_WINDOW", self.exit_mode_select)
            self.mode_select.mainloop()

    def d_z_c_s(self):
        '''点字成诗界面'''
        self.mode_select.destroy()

    def c_k_c_s(self):
        '''出口成诗界面'''
        self.mode_select.destroy()

    def exit_mode_select(self):
        '''退出游戏'''
        self.is_running = False
        self.mode_select.destroy()


if __name__ == '__main__':
    game = Game()
    game.start()
    print('游戏结束')
