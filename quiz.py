import tkinter as tk
from tkinter import messagebox

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.score = 0
        self.question_no = 0

        self.label = tk.Label(root, text="Welcome to the Sanatan Dharm Quiz Game!")
        self.label.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.pack()

    def play_game(self):
        self.question_no += 1
        if self.question_no <= 5:
            question = self.get_question(self.question_no)
            self.show_question(question)
        else:
            self.show_result()

    def get_question(self, question_no):
        questions = [
            "There are how many yugs in Sanatan Dharm ?",
            "How Many Number of Verses in Bhagwad Gita ?",
            "What are the four pillar of Sanatan Dharm ?",
            "How many forms of bhairav in Hindu Dharm ? ",
            "Which Number is important in Hindu Dharm ?"
        ]
        return questions[question_no - 1]

    def show_question(self, question):
        self.label.config(text=question)
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack(pady=10)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        correct_answers = [
            "4",
            "700",
            "Dharm, Arth, Kaam, Moksha",
            "52",
            "108",
        ]
        user_answer = self.answer_entry.get().lower()
        if user_answer == correct_answers[self.question_no - 1]:
            self.score += 1
            messagebox.showinfo("Correct", "Correct! You got 1 point.")
        else:
            messagebox.showerror("Incorrect", f"Incorrect! The correct answer is {correct_answers[self.question_no - 1]}.")

        self.answer_entry.destroy()
        self.submit_button.destroy()
        self.play_game()

    def show_result(self):
        try:
            percentage = (self.score * 100) / 5
        except ZeroDivisionError:
            percentage = 0

        result_message = f"Quiz completed!\nNumber of questions: {self.question_no}\nYour score: {self.score}\nPercentage: {percentage}%"
        messagebox.showinfo("Quiz Result", result_message)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameGUI(root)
    root.mainloop()
