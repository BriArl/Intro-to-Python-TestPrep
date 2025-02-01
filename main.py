import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # <-- Required for images
import json
import os

# Load questions from JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

current_question = 0
img_label = None  # Placeholder for image label
question_image = None  # Store image reference

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

# Function to move to the previous question
def previous_question():
    global current_question
    if current_question > 0:
        current_question -= 1
        load_question()
    else:
        messagebox.showwarning("No Previous Question", "You are on the first question!")

# Function to load question data
def load_question():
    global img_label, question_image  # Ensure image updates correctly

    question_data = questions[current_question]
    question_label.config(text=f"Question {current_question + 1}")

    # Load and display image
    image_path = question_data["image"]
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((500, 375))  # 🔥 Increased size
        question_image = ImageTk.PhotoImage(img)

        if img_label is None:  # First time loading
            img_label = tk.Label(root, image=question_image)
            img_label.pack(pady=10)  # 🔥 Add space around image
        else:  # Update existing image
            img_label.config(image=question_image)
    else:
        messagebox.showerror("Error", f"Image not found: {image_path}")

    # Clear answer box for new question
    answer_box.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Python Practice App")

question_label = tk.Label(root, text="Question 1", font=("Arial", 14))
question_label.pack()

# 🔥 Image now ABOVE the answer box
img_label = tk.Label(root)  # Placeholder, updated in load_question()
img_label.pack(pady=10)  

answer_box = tk.Text(root, height=8, width=50)
answer_box.pack(pady=10)  # 🔥 Add space

# Buttons
prev_button = tk.Button(root, text="Previous Question", command=previous_question)
prev_button.pack(side=tk.LEFT, padx=10, pady=10)

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack(side=tk.LEFT, padx=10, pady=10)

next_button = tk.Button(root, text="Next Question", command=next_question)
next_button.pack(side=tk.LEFT, padx=10, pady=10)

load_question()
root.mainloop()



