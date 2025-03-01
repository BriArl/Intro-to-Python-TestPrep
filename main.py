import tkinter as tk
from tkinter import messagebox
import json
import os

# Load questions from JSON file
with open("questions.json", "r") as file:
    all_questions = json.load(file)

# Store the selected chapter's questions
current_questions = []
current_question_index = 0

# Function to update the current questions based on selected chapter
def select_chapter(chapter):
    global current_questions, current_question_index
    current_questions = all_questions.get(chapter, [])
    current_question_index = 0
    
    if not current_questions:
        messagebox.showwarning("No Questions", f"No questions found for {chapter}")
        return
    
    load_question()

# Function to load answer from the .py file
def load_correct_answer():
    answer_path = current_questions[current_question_index]["answer_file"]
    with open(answer_path, "r") as file:
        return file.read().strip()

# Function to check the user's answer
def check_answer():
    user_answer = answer_box.get("1.0", tk.END).strip()
    correct_answer = load_correct_answer()

    if user_answer == correct_answer:
        messagebox.showinfo("Correct!", "Great job! Moving to next question.")
        next_question()
    else:
        messagebox.showerror("Incorrect", "Try again!")

# Function to move to the next question
def next_question():
    global current_question_index
    if current_question_index < len(current_questions) - 1:
        current_question_index += 1
        load_question()
    else:
        messagebox.showinfo("Completed", "You have finished all the questions!")

# Function to move to the previous question
def prev_question():
    global current_question_index
    if current_question_index > 0:
        current_question_index -= 1
        load_question()

# Function to load question data
def load_question():
    if not current_questions:
        question_label.config(text="No questions available")
        return

    question_data = current_questions[current_question_index]
    question_label.config(text=f"Question {current_question_index + 1}")
    answer_box.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Python Practice App")

# Dropdown for chapter selection
chapter_var = tk.StringVar(root)
chapter_var.set("Select a Chapter")  # Default value

chapter_menu = tk.OptionMenu(root, chapter_var, *all_questions.keys(), command=select_chapter)
chapter_menu.pack()

question_label = tk.Label(root, text="Question", font=("Arial", 14))
question_label.pack()

answer_box = tk.Text(root, height=8, width=50)
answer_box.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

prev_button = tk.Button(button_frame, text="Previous Question", command=prev_question)
prev_button.pack(side=tk.LEFT, padx=5)

check_button = tk.Button(button_frame, text="Check Answer", command=check_answer)
check_button.pack(side=tk.LEFT, padx=5)

next_button = tk.Button(button_frame, text="Next Question", command=next_question)
next_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
