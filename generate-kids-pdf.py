#!/usr/bin/env python3
"""Generate kid-friendly step-by-step PDF for Expense Management."""

from fpdf import FPDF
from pathlib import Path

OUTPUT = Path(__file__).parent / "docs" / "Expense-Management-For-Kids.pdf"


class KidPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 8, "Expense Management - Easy Guide for Kids", align="C")
            self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def title_page(self):
        self.add_page()
        self.set_font("Helvetica", "B", 26)
        self.set_text_color(15, 52, 96)
        self.ln(40)
        self.cell(0, 12, "Expense Management", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(233, 69, 96)
        self.cell(0, 10, "A Fun Step-by-Step Guide", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_font("Helvetica", "", 14)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 8, (
            "Learn how this website works!\n"
            "Written in simple words so anyone can follow along."
        ), align="C")
        self.ln(25)
        self.set_font("Helvetica", "", 12)
        self.cell(0, 8, "Read each step. Try it on your computer as you go!", align="C")

    def h1(self, text):
        self.ln(3)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(15, 52, 96)
        self.multi_cell(self.epw, 9, text)
        self.ln(2)

    def h2(self, text):
        self.ln(2)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(233, 69, 96)
        self.multi_cell(self.epw, 8, text)
        self.ln(1)

    def body(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 7, text)
        self.ln(2)

    def step(self, num, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(15, 52, 96)
        self.cell(12, 7, f"{num}.")
        self.set_font("Helvetica", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw - 12, 7, text)
        self.ln(1)

    def tip(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(45, 106, 79)
        self.multi_cell(self.epw, 6, "TIP: " + text)
        self.ln(2)

    def box(self, text):
        self.set_x(self.l_margin)
        self.set_fill_color(240, 244, 248)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 6, text, fill=True)
        self.ln(3)


def build_pdf():
    OUTPUT.parent.mkdir(exist_ok=True)
    pdf = KidPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.title_page()

    # Page 2 - What is it
    pdf.add_page()
    pdf.h1("Step 1: What Is This Website?")
    pdf.body(
        "Imagine you have a notebook where you write down every time you spend money. "
        "Maybe you bought a snack, a toy, or paid for a bus ride. You write: "
        "what you bought, how much it cost, and when you bought it."
    )
    pdf.body(
        "This website is like that notebook - but on the computer! "
        "It helps you remember your spending so you know where your money goes."
    )
    pdf.h2("Cool things you can do:")
    pdf.step(1, "Make your own account (like having your own notebook).")
    pdf.step(2, "Write down each expense (each time you spend money).")
    pdf.step(3, "See all your expenses in a list.")
    pdf.step(4, "See a colorful pie chart showing what you spend on most!")
    pdf.tip("Only YOU can see your expenses. Other people cannot see your notebook.")

    # Page 3 - Parts of the website
    pdf.h1("Step 2: The 3 Main Parts")
    pdf.body("This website has 3 parts that work together, like a team:")
    pdf.h2("Part A - What You See (Frontend)")
    pdf.body(
        "This is the screen in your web browser. It has buttons, forms, and colors. "
        "Files: index.html (the pages), style.css (the colors), app.js (the brain on your screen)."
    )
    pdf.h2("Part B - The Helper Server (Backend)")
    pdf.body(
        "This is a program running on the computer that listens for your clicks and saves data. "
        "File: backend/index.js. Think of it as a helpful robot behind the scenes."
    )
    pdf.h2("Part C - The Memory Box (Database)")
    pdf.body(
        "This saves your account and expenses so they are not lost when you close the browser. "
        "File: backend/expenses.db (created automatically). Like a filing cabinet."
    )
    pdf.box(
        "YOU  -->  Browser (frontend)  -->  Server (backend)  -->  Database\n"
        "You click something, the browser asks the server, the server saves or reads data."
    )

    # Page 4 - How to start
    pdf.add_page()
    pdf.h1("Step 3: How to Start the Website on Your Computer")
    pdf.body("Before you can use the website, someone needs to start the server. Follow these steps:")
    pdf.step(1, "Open Terminal (Mac) or Command Prompt (Windows).")
    pdf.step(2, "Go to the project folder (Expense Management).")
    pdf.step(3, "Type: npm install   (only needed the first time - downloads helpers).")
    pdf.step(4, "Type: npm start   (starts the server robot).")
    pdf.step(5, "Open your web browser and go to: http://localhost:3000")
    pdf.tip("If you see 'Server not running', go back and make sure npm start is running.")
    pdf.body(
        "localhost means 'this same computer'. Port 3000 is like a door number "
        "where the website lives."
    )

    # Page 5 - Login and signup
    pdf.h1("Step 4: Making an Account (Sign Up)")
    pdf.body("The first time you visit, you need your own account.")
    pdf.step(1, "Click 'Sign up' on the login page.")
    pdf.step(2, "Type your email (like name@email.com).")
    pdf.step(3, "Type a password (at least 6 letters/numbers). Remember it!")
    pdf.step(4, "Click 'Create Account'.")
    pdf.body(
        "What happens inside? The server checks your email is new, hides your password "
        "(like putting it in a locked safe using bcrypt), saves you in the database, "
        "and gives you a secret ticket called a JWT token."
    )
    pdf.h2("Step 5: Logging In")
    pdf.step(1, "Type your email and password.")
    pdf.step(2, "Click 'Log In'.")
    pdf.step(3, "If correct, you go to the Dashboard (home page).")
    pdf.body(
        "The secret ticket (token) is saved in your browser. Every time you add or "
        "view an expense, you show this ticket so the server knows it is really you."
    )

    # Page 6 - Dashboard
    pdf.add_page()
    pdf.h1("Step 6: The Dashboard (Home Page)")
    pdf.body("After login, you see the main page. Here is what each part does:")
    pdf.h2("Add Expense Form")
    pdf.step(1, "Pick a Category - Food, Transport, Shopping, Bills, etc.")
    pdf.step(2, "Type the Amount - how much money you spent (like 5.50).")
    pdf.step(3, "Add Comments - optional note (like 'pizza with friends').")
    pdf.step(4, "Click 'Add Expense'.")
    pdf.body("Your new expense appears in the table below!")
    pdf.h2("Total Expenses")
    pdf.body("Shows the sum of ALL your spending. Like adding every number in your notebook.")
    pdf.h2("Expense Table")
    pdf.body("A list of everything you spent, newest first. Each row has:")
    pdf.step(1, "Category and Amount")
    pdf.step(2, "Created At - when you first added it")
    pdf.step(3, "Updated At - when you last changed it")
    pdf.step(4, "Edit button - change an expense")
    pdf.step(5, "Delete button - remove an expense (asks 'Are you sure?' first)")

    # Page 7 - Edit delete chart
    pdf.h1("Step 7: Editing an Expense")
    pdf.step(1, "Click the 'Edit' button on a row.")
    pdf.step(2, "The form at the top fills with that expense's info.")
    pdf.step(3, "Change what you want.")
    pdf.step(4, "Click 'Save Changes'. Or click 'Cancel Edit' to stop.")
    pdf.h1("Step 8: Deleting an Expense")
    pdf.step(1, "Click 'Delete' on a row.")
    pdf.step(2, "A popup asks if you are sure.")
    pdf.step(3, "Click OK - the expense is gone from the list and database.")

    pdf.add_page()
    pdf.h1("Step 9: The Pie Chart")
    pdf.body(
        "A pie chart is a circle split into colored slices. Each slice shows how much "
        "you spent in one category. Bigger slice = more money spent there."
    )
    pdf.step(1, "Click 'Pie Chart' button on the dashboard.")
    pdf.step(2, "The website asks the server for category totals.")
    pdf.step(3, "The server adds up amounts per category (Food + Food + Food...).")
    pdf.step(4, "JavaScript draws colored slices using CSS (no extra apps needed!).")
    pdf.step(5, "A list below shows each category, amount, and percentage.")
    pdf.tip("Example: If you spent $30 on Food and $70 total, Food is 42.9% of the pie.")

    # Page 8 - Logout and flow
    pdf.h1("Step 10: Logging Out")
    pdf.step(1, "Click 'Logout'.")
    pdf.step(2, "Your secret ticket is erased from the browser.")
    pdf.step(3, "You go back to the Login page.")
    pdf.body("Next time, log in again with your email and password.")

    pdf.h1("Step 11: The Full Journey (All Steps Together)")
    pdf.box(
        "1. Start server (npm start)\n"
        "2. Open browser -> localhost:3000\n"
        "3. Sign up or Log in\n"
        "4. Add expenses on Dashboard\n"
        "5. Edit or Delete if needed\n"
        "6. View Pie Chart\n"
        "7. Logout when done"
    )

    # Page 9 - Tech simple
    pdf.add_page()
    pdf.h1("Step 12: What Tools Built This? (Simple List)")
    pdf.body("These are the building blocks - like LEGO pieces:")
    pdf.step(1, "HTML - builds the pages (buttons, forms, text).")
    pdf.step(2, "CSS - makes it pretty (colors, spacing, layout).")
    pdf.step(3, "JavaScript - makes buttons DO things.")
    pdf.step(4, "Node.js - runs the server program on the computer.")
    pdf.step(5, "Express - helps the server answer requests quickly.")
    pdf.step(6, "SQLite - small database that remembers your data.")
    pdf.step(7, "JWT - your secret login ticket.")
    pdf.step(8, "bcrypt - locks your password so nobody can read it.")

    pdf.h1("Step 13: Important Rules to Remember")
    pdf.step(1, "Always use http://localhost:3000 - do not double-click the HTML file.")
    pdf.step(2, "Keep npm start running while you use the website.")
    pdf.step(3, "Your password is never saved as plain text - only a scrambled version.")
    pdf.step(4, "Each user only sees their own expenses - the server checks your ticket.")
    pdf.step(5, "Categories: Food, Transport, Shopping, Bills, Entertainment, Health, Other.")

    pdf.h1("You Did It!")
    pdf.body(
        "Now you know how the Expense Management website works from start to finish. "
        "Try each step on your computer. The best way to learn is by doing!"
    )
    pdf.tip("Ask a grown-up to help you run npm start the first time.")

    pdf.output(str(OUTPUT))
    print(f"PDF created: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
