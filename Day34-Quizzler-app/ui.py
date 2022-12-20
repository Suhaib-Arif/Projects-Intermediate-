from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface():
    def __init__(self,quiz_bank: QuizBrain):
        self.quiz=quiz_bank

        self.window=Tk()
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20,pady=20)
        self.window.title("Quizzler")

        self.canvas=Canvas()
        self.canvas.config(height=250,width=300)
        self.Quest_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text="SOME TEXT",
            fill=THEME_COLOR,
            font=("Arial",17,"italic")
            )
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

        self.points=Label(text=f"score:{self.quiz.score}",bg=THEME_COLOR,fg="#fff")
        self.points.grid(row=0,column=2)

        false_image=PhotoImage(file="images/false.png")

        self.false_button=Button(image=false_image,bg=THEME_COLOR,highlightthickness=0,command=self.is_wrong)
        self.false_button.grid(row=2,column=2)
        self
        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,bg=THEME_COLOR,highlightthickness=0,command=self.is_right)
        self.true_button.grid(row=2,column=1)

        self.display_question()

        self.window.mainloop()

    def display_question(self):
        self.canvas.config(bg="White")
        self.points.config(text=f"score: {self.quiz.score}")
        if self.quiz.still_has_questions():

            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.Quest_text,text=q_text)


        else:
            self.canvas.itemconfig(self.Quest_text,text=f"Your final score is {self.quiz.score}")
    def is_right(self):
        result=self.quiz.check_answer("true")
        self.flash_screen(result)

    def is_wrong(self):

        result=self.quiz.check_answer("false")
        self.flash_screen(result)

    def flash_screen(self, result):
        color = ""
        if result:
            color="lime green"
        else:
            color="tomato"
        self.canvas.config(bg=color,highlightthickness=0)
        self.window.after(1000,self.display_question)
