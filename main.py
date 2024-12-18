import tkinter as tk
from tkinter import ttk, messagebox
import random


class MathTutorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Tutor - Learn and Practice")
        self.score = 0
        self.create_scrollable_frame()
        self.main_menu()

    def create_scrollable_frame(self):
        """Sets up a scrollable frame for the application."""
        self.canvas = tk.Canvas(self.root)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

    def clear_window(self):
        """Clears all widgets from the scrollable frame."""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.scrollable_frame, text="Welcome to Math Tutor", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.scrollable_frame, text="Choose an option below:", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.scrollable_frame, text="Learn", command=self.learn_module, width=20, height=2,
                  bg="lightblue").pack(pady=10)
        tk.Button(self.scrollable_frame, text="Practice", command=self.practice_module, width=20, height=2,
                  bg="lightgreen").pack(pady=10)
        tk.Button(self.scrollable_frame, text="Quiz", command=self.quiz_module, width=20, height=2,
                  bg="lightyellow").pack(pady=10)
        tk.Button(self.scrollable_frame, text="Leaderboard", command=self.show_leaderboard, width=20, height=2,
                  bg="lightcoral").pack(pady=10)
        tk.Button(self.scrollable_frame, text="Exit", command=self.root.quit, width=20, height=2).pack(pady=20)

    def learn_module(self):
        self.clear_window()
        tk.Label(self.scrollable_frame, text="Learn About Areas", font=("Arial", 18)).pack(pady=10)

        shapes = ["Square", "Rectangle", "Triangle"]
        for shape in shapes:
            tk.Button(self.scrollable_frame, text=f"Learn {shape}",
                      command=lambda s=shape: self.show_formula_with_visual(s), width=20, height=2).pack(pady=5)

        tk.Button(self.scrollable_frame, text="Back to Main Menu", command=self.main_menu, width=20, height=2).pack(
            pady=20)

    def show_formula_with_visual(self, shape):
        formulas = {
            "Square": ("Area = side × side", "A square has four equal sides."),
            "Rectangle": ("Area = length × width", "A rectangle has opposite sides equal."),
            "Triangle": ("Area = 0.5 × base × height", "A triangle has three sides.")
        }

        visuals = {
            "Square": "🟪",
            "Rectangle": "⬛",
            "Triangle": "🔺"
        }

        formula, description = formulas[shape]
        visual = visuals[shape]

        messagebox.showinfo(
            f"{shape} Formula",
            f"{visual}\n\nFormula: {formula}\n\nDescription: {description}"
        )

    def practice_module(self):
        self.clear_window()
        tk.Label(self.scrollable_frame, text="Practice Area Calculations", font=("Arial", 18)).pack(pady=10)

        shapes = ["Square", "Rectangle", "Triangle"]
        for shape in shapes:
            tk.Button(self.scrollable_frame, text=f"Practice {shape}",
                      command=lambda s=shape: self.practice_questions(s), width=20, height=2).pack(pady=5)

        tk.Button(self.scrollable_frame, text="Back to Main Menu", command=self.main_menu, width=20, height=2).pack(
            pady=20)

    def practice_questions(self, shape):
        self.clear_window()
        tk.Label(self.scrollable_frame, text=f"Practice: {shape}", font=("Arial", 18)).pack(pady=10)

        if shape == "Square":
            side = random.randint(1, 20)
            correct_area = side * side
            tk.Label(self.scrollable_frame, text=f"Side: {side}", font=("Arial", 14)).pack(pady=5)
        elif shape == "Rectangle":
            length = random.randint(1, 20)
            width = random.randint(1, 20)
            correct_area = length * width
            tk.Label(self.scrollable_frame, text=f"Length: {length}, Width: {width}", font=("Arial", 14)).pack(pady=5)
        elif shape == "Triangle":
            base = random.randint(1, 20)
            height = random.randint(1, 20)
            correct_area = 0.5 * base * height
            tk.Label(self.scrollable_frame, text=f"Base: {base}, Height: {height}", font=("Arial", 14)).pack(pady=5)

        user_entry = tk.Entry(self.scrollable_frame)
        user_entry.pack(pady=10)

        def check_answer():
            try:
                user_area = float(user_entry.get())
                if abs(user_area - correct_area) < 0.01:
                    messagebox.showinfo("Correct", f"Well done! The area is {correct_area:.2f}.")
                else:
                    messagebox.showinfo("Incorrect", f"Oops! The correct area is {correct_area:.2f}.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        tk.Button(self.scrollable_frame, text="Submit", command=check_answer, width=15).pack(pady=10)
        tk.Button(self.scrollable_frame, text="Back to Practice Menu", command=self.practice_module, width=20).pack(
            pady=10)

    def quiz_module(self):
        self.clear_window()
        tk.Label(self.scrollable_frame, text="Quiz: Test Your Skills", font=("Arial", 18)).pack(pady=10)
        self.score = 0
        self.quiz_question(1)

    def quiz_question(self, question_number):
        if question_number > 5:
            messagebox.showinfo("Quiz Complete", f"Your final score is {self.score}/5!")
            self.main_menu()
            return

        shape = random.choice(["Square", "Rectangle", "Triangle"])
        if shape == "Square":
            side = random.randint(1, 20)
            correct_area = side * side
        elif shape == "Rectangle":
            length = random.randint(1, 20)
            width = random.randint(1, 20)
            correct_area = length * width
        elif shape == "Triangle":
            base = random.randint(1, 20)
            height = random.randint(1, 20)
            correct_area = 0.5 * base * height

        tk.Label(self.scrollable_frame, text=f"Question {question_number}: Calculate the area of a {shape}",
                 font=("Arial", 14)).pack(pady=10)

        if shape == "Square":
            tk.Label(self.scrollable_frame, text=f"Side: {side}").pack(pady=5)
        elif shape == "Rectangle":
            tk.Label(self.scrollable_frame, text=f"Length: {length}, Width: {width}").pack(pady=5)
        elif shape == "Triangle":
            tk.Label(self.scrollable_frame, text=f"Base: {base}, Height: {height}").pack(pady=5)

        user_entry = tk.Entry(self.scrollable_frame)
        user_entry.pack(pady=10)

        def check_quiz_answer():
            nonlocal question_number
            try:
                user_area = float(user_entry.get())
                if abs(user_area - correct_area) < 0.01:
                    self.score += 1
                question_number += 1
                self.quiz_question(question_number)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")

        tk.Button(self.scrollable_frame, text="Submit", command=check_quiz_answer, width=15).pack(pady=10)

    def show_leaderboard(self):
        messagebox.showinfo("Leaderboard", f"Your current quiz score is: {self.score}/5.")


# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = MathTutorApp(root)
    root.geometry("600x400")
    root.mainloop()
