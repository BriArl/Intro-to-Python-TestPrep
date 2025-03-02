import tkinter as tk
from tkinter import messagebox, ttk  # Added ttk for dropdown
from PIL import Image, ImageTk
import json
import os

# Load questions from JSON file
with open("questions.json", "r") as file:
    all_questions = json.load(file)

current_question = 0
selected_chapter = None  # Holds the currently selected chapter
questions = []  # Will hold questions from selected chapter
img_label = None
question_image = None

# Function to load answer from the .py file
def load_correct_answer():
    answer_path = questions[current_question]["answer_file"]
    with open(answer_path, "r") as file:
        return file.read().strip()  # Read & remove extra spaces

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
    global img_label, question_image  

    if not questions:
        messagebox.showwarning("No Questions", "Select a chapter first.")
        return

    question_data = questions[current_question]
    question_label.config(text=f"Question {current_question + 1}")

    # Load and display image
    image_path = question_data["image"]
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((600, 450))  # 🔥 Increased size
        question_image = ImageTk.PhotoImage(img)

        if img_label is None:  # First time loading
            img_label = tk.Label(root, image=question_image)
            img_label.pack(pady=10)
        else:  # Update existing image
            img_label.config(image=question_image)
    else:
        messagebox.showerror("Error", f"Image not found: {image_path}")

    # Clear answer box for new question
    answer_box.delete("1.0", tk.END)

# Function to update questions based on selected chapter
def select_chapter(event):
    global selected_chapter, questions, current_question
    selected_chapter = chapter_var.get()
    questions = all_questions.get(selected_chapter, [])
    
    if not questions:
        messagebox.showwarning("Empty Chapter", "No questions in this chapter!")
    else:
        current_question = 0
        load_question()

# Function to toggle fullscreen mode
def toggle_fullscreen():
    if root.attributes("-fullscreen"):
        root.attributes("-fullscreen", False)  # Exit fullscreen
    else:
        root.attributes("-fullscreen", True)  # Enter fullscreen

# Function to exit the app
def exit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Python Practice App")
root.geometry("900x700")  # 🔥 Starts in normal window mode

# Allow exiting full-screen with "Esc" key
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

# Add traditional window control buttons
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

window_menu = tk.Menu(menu_bar, tearoff=0)
window_menu.add_command(label="Toggle Fullscreen", command=toggle_fullscreen)
window_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="Window", menu=window_menu)

# Chapter Selection
chapter_var = tk.StringVar()
chapter_label = tk.Label(root, text="Select Chapter:", font=("Arial", 14))
chapter_label.pack()

chapter_dropdown = ttk.Combobox(root, textvariable=chapter_var, values=list(all_questions.keys()))
chapter_dropdown.pack()
chapter_dropdown.bind("<<ComboboxSelected>>", select_chapter)  # Triggers function when a chapter is chosen

question_label = tk.Label(root, text="Question 1", font=("Arial", 18))
question_label.pack()

# 🔥 Image above answer box
img_label = tk.Label(root)
img_label.pack(pady=10)

answer_box = tk.Text(root, height=8, width=70)
answer_box.pack(pady=10)

# 🔥 Frame to CENTER buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

prev_button = tk.Button(button_frame, text="Previous Question", command=previous_question)
prev_button.grid(row=0, column=0, padx=10)

check_button = tk.Button(button_frame, text="Check Answer", command=check_answer)
check_button.grid(row=0, column=1, padx=10)

next_button = tk.Button(button_frame, text="Next Question", command=next_question)
next_button.grid(row=0, column=2, padx=10)

# 🔥 Exit button at the bottom
exit_button = tk.Button(root, text="Exit", command=exit_app, bg="red", fg="white", font=("Arial", 12, "bold"))
exit_button.pack(pady=20)

root.mainloop()
