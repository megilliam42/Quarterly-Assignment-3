#connected to database creation as database creation creates the data needed in this 

import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connect to the database
def connect_db():
    connection = sqlite3.connect('solar_system_questions.db')
    cursor = connection.cursor()
    return connection, cursor

# Function to fetch all questions from a specific table
def get_all_questions(table_name):
    connection, cursor = connect_db()
    cursor.execute(f"SELECT question, answer_a, answer_b, answer_c, answer_d, correct_answer FROM {table_name}")
    questions = cursor.fetchall()
    connection.close()
    return questions

# Function to open the quiz window for the selected topic
def open_quiz_window():
    # Create a new window for the quiz
    quiz_window = tk.Toplevel(root)
    quiz_window.title(f"Quiz - {table_var.get().capitalize()}")

    # Load questions from the selected table
    load_questions(quiz_window)

# Function to display the current question and multiple-choice answers
def display_current_question(window):
    if current_question_index < len(questions):
        question, answer_a, answer_b, answer_c, answer_d, correct_answer = questions[current_question_index]
        question_text.delete(1.0, tk.END)  # Clear previous text
        question_text.insert(tk.END, f"Q: {question}\n\n")

        # Set the text for each radio button to show the answer choices
        choice_var.set(None)  # Reset selected choice
        radio_a.config(text=answer_a, value=answer_a)
        radio_b.config(text=answer_b, value=answer_b)
        radio_c.config(text=answer_c, value=answer_c)
        radio_d.config(text=answer_d, value=answer_d)

        feedback_label.config(text="")  # Clear previous feedback
    else:
        messagebox.showinfo("End of Questions", "You have reached the end of the questions.", parent=window)

# Function to load questions from the selected table and reset the question index
def load_questions(window):
    global questions, current_question_index
    questions = get_all_questions(table_var.get())
    current_question_index = 0

    # Set up widgets for the quiz in the new window
    global question_text, radio_a, radio_b, radio_c, radio_d, feedback_label

    # Text widget to display the current question
    question_text = tk.Text(window, width=50, height=5)
    question_text.pack()

    # Radio buttons for multiple-choice answers
    choice_var.set(None)  # Reset selected choice
    radio_a = tk.Radiobutton(window, text="Answer A", variable=choice_var, value="A")
    radio_a.pack(anchor="w")
    radio_b = tk.Radiobutton(window, text="Answer B", variable=choice_var, value="B")
    radio_b.pack(anchor="w")
    radio_c = tk.Radiobutton(window, text="Answer C", variable=choice_var, value="C")
    radio_c.pack(anchor="w")
    radio_d = tk.Radiobutton(window, text="Answer D", variable=choice_var, value="D")
    radio_d.pack(anchor="w")

    # Button to submit the answer
    submit_button = tk.Button(window, text="Submit Answer", command=check_answer)
    submit_button.pack()

    # Label to display feedback
    feedback_label = tk.Label(window, text="", font=("Arial", 10))
    feedback_label.pack()

    # Next button to go to the next question
    next_button = tk.Button(window, text="Next Question", command=lambda: next_question(window))
    next_button.pack()

    # Display the first question
    display_current_question(window)

# Function to show the next question
def next_question(window):
    global current_question_index
    current_question_index += 1
    display_current_question(window)

# Function to check if the selected answer is correct
def check_answer():
    if current_question_index < len(questions):
        _, _, _, _, _, correct_answer = questions[current_question_index]
        selected_answer = choice_var.get()  # User's selected answer
        if selected_answer == correct_answer:
            feedback_label.config(text="Correct!", fg="green")
        else:
            feedback_label.config(text=f"Incorrect. The correct answer was: {correct_answer}", fg="red")
    else:
        messagebox.showinfo("End of Questions", "No question loaded to check the answer.")

# Main application window
root = tk.Tk()
root.title("Quiz Selection")

# Dropdown menu to select the table
table_var = tk.StringVar()
table_var.set("geography")
table_menu = tk.OptionMenu(root, table_var, "solar_systems", "geography", "literature", "python", "art")
table_menu.pack()

# Button to open the quiz window
start_quiz_button = tk.Button(root, text="Start Quiz", command=open_quiz_window)
start_quiz_button.pack()

# Initialize question data and choice variable
questions = []
current_question_index = 0
choice_var = tk.StringVar()

# Run the application
root.mainloop()
