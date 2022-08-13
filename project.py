# Import Required Library
from tkinter import *
import random



# Computer Value
class GUI:
    def __init__(self, root):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.root = root

        self.laple_Titel=Label(self.root,
                               text="Rock Paper Scissor",
                               font="normal 20 bold",
                               fg="blue")
        self.laple_Titel.pack(pady=20)
        self.frame = Frame(self.root)
        self.frame.pack()

        self.label_plyer = Label(self.frame,
                                 text="Player              ",
                                 font=10)

        self.label_vs = Label(self.frame,
                              text="VS             ",
                              font="normal 10 bold")

        self.label_computer = Label(self.frame, text="Computer", font=10)

        self.label_plyer.pack(side=LEFT)
        self.label_vs.pack(side=LEFT)
        self.label_computer.pack()
        self.frame_2 = Frame(self.root)
        self.frame_2.pack()
        self.label_plyer_score = Label(self.frame_2,
                                 text="0               ",
                                 font=10)

        self.label_vs1 = Label(self.frame_2,
                              text="score              ",
                              font="normal 10 bold")

        self.label_computer_score = Label(self.frame_2, text="0     ", font=10)

        self.label_plyer_score.pack(side=LEFT)
        self.label_vs1.pack(side=LEFT)
        self.label_computer_score.pack()

        self.label_wining = Label(root,
                                  text="",
                                  font="normal 20 bold",
                                  bg="white",
                                  width=15,
                                  borderwidth=2,
                                  relief="solid")
        self.label_wining.pack(pady=20)

        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.button_rock = Button(self.frame1, text="Rock",
                                  font=10, width=7,
                                  command=self.isrock)

        self.button_paper = Button(self.frame1, text="Paper ",
                                   font=10, width=7,
                                   command=self.ispaper)

        self.button_scissor = Button(self.frame1, text="Scissor",
                                     font=10, width=7,
                                     command=self.isscissor)

        self.button_rock.pack(side=LEFT, padx=10)
        self.button_paper.pack(side=LEFT, padx=10)
        self.button_scissor.pack(padx=10)

        self.button_reset=Button(self.root, text="Reset Game",
               font=10, fg="red",
               bg="black", command=self.reset_game)
        self.button_reset.pack(pady=20)


        self.computer_value = {
            "0": "Rock",
            "1": "Paper",
            "2": "Scissor"
}
        self.score_player=0
        self.score_computer = 0
    def reset_game(self):
        """
        ths function reset all the game stats and start the game over again
        """
        self.score_computer=0
        self.score_player=0
        self.label_plyer.config(text="Player              ")
        self.label_computer.config(text="Computer")
        self.label_wining.config(text="")
        self.label_plyer_score.config(text=f"{self.score_player}                 ")
        self.label_computer_score.config(text=f"{self.score_computer}           ")


    def isrock(self):
        """
         this function decides the winner if the plyer choose the Rock button and count the score for the winner.
        """

        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Player Win"
            self.score_player+=1
        else:
            self.score_computer+= 1
            match_result = "Computer Win"
        self.label_plyer_score.config(text=f"{self.score_player}                 ")
        self.label_computer_score.config(text=f"{self.score_computer}           ")

        self.label_wining.config(text=match_result)
        self.label_plyer.config(text="Rock            ")
        self.label_computer.config(text=c_v)


    def ispaper(self):
        """
        this function decides the winner if the plyer choose the paper button and count the score for the winner.
        """
        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Computer Win"
            self.score_computer+=1
        else:
            self.score_player += 1
            match_result = "Player Win"
        self.label_plyer_score.config(text=f"{self.score_player}                 ")
        self.label_computer_score.config(text=f"{self.score_computer}           ")
        self.label_wining.config(text=match_result)
        self.label_plyer.config(text="Paper           ")
        self.label_computer.config(text=c_v)


    def isscissor(self):
        """
        this function decides the winner if the plyer choose the scissor button and count the score for the winner.
        """
        c_v = self.computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Computer Win"
            self.score_computer+=1
        elif c_v == "Scissor":
            match_result = "Match Draw"
        else:
            self.score_player+=1
            match_result = "Player Win"
        self.label_plyer_score.config(text=f"{self.score_player}                 ")
        self.label_computer_score.config(text=f"{self.score_computer}           ")
        self.label_wining.config(text=match_result)
        self.label_plyer.config(text="Scissor         ")
        self.label_computer.config(text=c_v)









