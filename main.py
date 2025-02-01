import tkinter as tk
from tkinter import messagebox
import json
import os

# Load questions from JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

current_question = 0

# Function to load answer from the .py file
def load_correct_answer():
    answer_path = questions[current_question]["answer_file"]
    with open(answer_path, "r") as file:
        return file.read().strip()  # Read & remove extra spaces

# Function to check the user's answer
def check_answer():
    user_answer = answer_box.get("1.0", tk.END).strip()  # Get text from entry box
    correct_answer = load_correct_answer()

    if user_answer == correct_answer:
        messagebox.showinfo("Correct!", "Great job! Moving to next question.")
        next_question()
    else:
        messagebox.showerror("Incorrect", "Try again!")

# Function to move to the next question
def next_question():
    global current_question
    if current_question < len(questions) - 1:
        current_question += 1
        load_question()
    else:
        messagebox.showinfo("Completed", "You have finished all the questions!")

# Function to load question data
def load_question():
    question_data = questions[current_question]
    question_label.config(text=f"Question {current_question + 1}")
    answer_box.delete("1.0", tk.END)  # Clear answer box

# GUI setup
root = tk.Tk()
root.title("Python Practice App")

question_label = tk.Label(root, text="Question 1", font=("Arial", 14))
question_label.pack()

answer_box = tk.Text(root, height=8, width=50)
answer_box.pack()

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack()

next_button = tk.Button(root, text="Next Question", command=next_question)
next_button.pack()

load_question()
root.mainloop()

