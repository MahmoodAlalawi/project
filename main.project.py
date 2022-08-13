from project import *


def main():

    root = Tk()
    root.title("Rock Paper Scissor Game")
    root.geometry('300x300')
    root.resizable(False, False)
    widgets = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()