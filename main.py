import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

# Load questions and answers from JSON file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# Check the user's answer
def check_answer():
    user_answer = answer_entry.get().strip()
    correct_answer = questions[current_question]['answer']
    
    if user_answer == correct_answer:
        messagebox.showinfo("Correct!", "Well done! Moving to the next question.")
        next_question()
    else:
        messagebox.showerror("Incorrect", "Try again!")

# Load the next question
def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        update_question_display()
    else:
        messagebox.showinfo("Finished!", "You have completed all questions!")
        root.quit()

# Update the question display
def update_question_display():
    global question_image
    question_label.config(text=f"Question {current_question + 1}")
    
    img = Image.open(questions[current_question]['image'])
    img = img.resize((400, 300), Image.ANTIALIAS)
    question_image = ImageTk.PhotoImage(img)
    image_label.config(image=question_image)
    
    answer_entry.delete(0, tk.END)

# Initialize the application
root = tk.Tk()
root.title("Python Practice App")
questions = load_questions()
current_question = 0

# GUI Components
question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=10)

question_image = None
image_label = tk.Label(root)
image_label.pack()

answer_entry = tk.Entry(root, font=("Arial", 12))
answer_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

# Load the first question
update_question_display()

# Run the app
root.mainloop()
