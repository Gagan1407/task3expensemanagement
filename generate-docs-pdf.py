#!/usr/bin/env python3
"""Generate complete code documentation PDF for Expense Management."""

from fpdf import FPDF
from pathlib import Path

OUTPUT = Path(__file__).parent / "docs" / "Expense-Management-Code-Documentation.pdf"


class DocPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 8, "Expense Management - Complete Code Documentation", align="C")
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def title_page(self):
        self.add_page()
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(15, 52, 96)
        self.ln(50)
        self.cell(0, 12, "Expense Management", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 16)
        self.set_text_color(60, 60, 60)
        self.cell(0, 10, "Complete Code Documentation", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(20)
        self.set_font("Helvetica", "", 12)
        self.multi_cell(0, 7, (
            "This document explains every part of the Expense Management application: "
            "project structure, backend API, database, authentication, frontend UI, "
            "JavaScript logic, CSS styling, and how all components work together."
        ), align="C")
        self.ln(30)
        self.set_font("Helvetica", "", 11)
        self.cell(0, 8, "Tech Stack: Node.js, Express, SQLite, JWT, HTML/CSS/JavaScript", align="C")

    def h1(self, text):
        self.ln(4)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(15, 52, 96)
        self.multi_cell(self.epw, 9, text)
        self.ln(2)

    def h2(self, text):
        self.ln(2)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(22, 33, 62)
        self.multi_cell(self.epw, 8, text)
        self.ln(1)

    def h3(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(40, 40, 40)
        self.multi_cell(self.epw, 7, text)
        self.ln(1)

    def body(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 6, text)
        self.ln(2)

    def bullet(self, text):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 6, f"- {text}")
        self.ln(1)

    def code_block(self, text):
        self.set_x(self.l_margin)
        self.set_font("Courier", "", 8)
        self.set_fill_color(245, 247, 250)
        self.set_text_color(20, 20, 20)
        for line in text.split("\n"):
            self.multi_cell(self.epw, 4.5, "  " + line[:100], fill=True)
        self.ln(3)

    def table_row(self, cols, bold=False):
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B" if bold else "", 9)
        widths = [42, 148]
        for i, col in enumerate(cols):
            self.cell(widths[i], 7, col[:75], border=1)
        self.ln()


def build_pdf():
    OUTPUT.parent.mkdir(exist_ok=True)
    pdf = DocPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.title_page()

    # 1. Overview
    pdf.add_page()
    pdf.h1("1. Project Overview")
    pdf.body(
        "Expense Management is a full-stack web application that lets users sign up, log in, "
        "add/edit/delete expenses, view a sorted expense table, and see a pie chart of spending "
        "by category. Each user only sees their own data."
    )
    pdf.h2("1.1 Architecture")
    pdf.body(
        "The app uses a client-server architecture. The browser loads HTML/CSS/JS from the "
        "frontend folder. JavaScript sends JSON requests to REST API endpoints (/api/*). "
        "Express (Node.js) handles those requests, validates JWT tokens, and reads/writes "
        "data in a SQLite database file (backend/expenses.db)."
    )
    pdf.h2("1.2 Project Structure")
    pdf.code_block(
        "Expense Management/\n"
        "  package.json          - Dependencies and npm scripts\n"
        "  backend/\n"
        "    index.js            - Express server and all API routes\n"
        "    auth.js             - JWT sign/verify and auth middleware\n"
        "    db.js               - SQLite database setup and tables\n"
        "    expenses.db         - Database file (created at runtime)\n"
        "  frontend/\n"
        "    index.html          - All UI pages (login, signup, dashboard, chart)\n"
        "    css/style.css       - Styling for the entire app\n"
        "    js/app.js           - Frontend logic and API calls"
    )

    # 2. Dependencies
    pdf.h1("2. Dependencies (package.json)")
    pdf.body("The project uses npm to manage these packages:")
    pdf.table_row(["Package", "Purpose"], bold=True)
    pdf.table_row(["express", "Web server framework for API routes"])
    pdf.table_row(["better-sqlite3", "Fast SQLite database driver"])
    pdf.table_row(["bcryptjs", "Hash and verify passwords securely"])
    pdf.table_row(["jsonwebtoken", "Create and verify JWT login tokens"])
    pdf.table_row(["cors", "Allow cross-origin requests"])
    pdf.ln(2)
    pdf.body("Scripts: npm start runs the server. npm run dev runs with auto-restart on file changes.")

    # 3. Database
    pdf.add_page()
    pdf.h1("3. Database Layer (backend/db.js)")
    pdf.body(
        "This file creates and configures the SQLite database. When the server starts, "
        "better-sqlite3 opens backend/expenses.db and runs CREATE TABLE IF NOT EXISTS "
        "statements so tables exist automatically."
    )
    pdf.h2("3.1 Users Table")
    pdf.bullet("id - Auto-increment primary key")
    pdf.bullet("email - Unique, required (stored lowercase)")
    pdf.bullet("password - Bcrypt hash, never plain text")
    pdf.bullet("created_at - Timestamp when account was created")
    pdf.h2("3.2 Expenses Table")
    pdf.bullet("id - Auto-increment primary key")
    pdf.bullet("user_id - Links expense to a user (foreign key)")
    pdf.bullet("category - e.g. Food, Transport, Bills")
    pdf.bullet("amount - Positive number (REAL type)")
    pdf.bullet("comments - Optional note text")
    pdf.bullet("created_at / updated_at - Timestamps")
    pdf.body(
        "The db object is exported and imported by index.js. All SQL uses prepared "
        "statements with ? placeholders to prevent SQL injection."
    )

    # 4. Authentication
    pdf.h1("4. Authentication (backend/auth.js)")
    pdf.h2("4.1 JWT Secret")
    pdf.body(
        "JWT_SECRET comes from environment variable or defaults to 'expense-tracker-secret-key'. "
        "In production, always set a strong JWT_SECRET environment variable."
    )
    pdf.h2("4.2 signToken(userId, email)")
    pdf.body(
        "Creates a JSON Web Token containing userId and email. Token expires in 7 days. "
        "Returned to the client after signup or login."
    )
    pdf.h2("4.3 authMiddleware")
    pdf.body(
        "Protects expense routes. Reads Authorization: Bearer <token> header, verifies "
        "the JWT, and attaches req.user = { userId, email }. Returns 401 if missing, "
        "invalid, or expired token."
    )

    # 5. Backend API
    pdf.add_page()
    pdf.h1("5. Backend API (backend/index.js)")
    pdf.body(
        "Express app listens on PORT (default 3000). Uses cors() and express.json(). "
        "Serves frontend static files. All API routes start with /api."
    )
    pdf.h2("5.1 Auth Routes")
    pdf.table_row(["Method", "Route / Description"], bold=True)
    pdf.table_row(["POST", "/api/auth/signup - Create account"])
    pdf.table_row(["POST", "/api/auth/login - Log in and get token"])
    pdf.table_row(["GET", "/api/health - Server health check"])
    pdf.ln(2)
    pdf.h3("Signup flow:")
    pdf.bullet("Validate email and password (min 6 chars)")
    pdf.bullet("Normalize email to lowercase")
    pdf.bullet("Hash password with bcrypt (10 rounds)")
    pdf.bullet("Insert into users table; return JWT + email")
    pdf.bullet("400 if email already exists")
    pdf.h3("Login flow:")
    pdf.bullet("Find user by email")
    pdf.bullet("Compare password with bcrypt.compareSync")
    pdf.bullet("Return JWT + email or 401 Invalid email or password")

    pdf.h2("5.2 Expense Routes (all require authMiddleware)")
    pdf.table_row(["Method", "Route / Description"], bold=True)
    pdf.table_row(["GET", "/api/expenses - List user expenses (newest first)"])
    pdf.table_row(["POST", "/api/expenses - Add new expense"])
    pdf.table_row(["PUT", "/api/expenses/:id - Update expense"])
    pdf.table_row(["DELETE", "/api/expenses/:id - Delete expense"])
    pdf.table_row(["GET", "/api/expenses/stats/by-category - Pie chart data"])
    pdf.ln(2)
    pdf.body(
        "Every expense query filters by user_id from the JWT so users cannot access "
        "each other's data. Update sets updated_at to current time. Delete returns 404 "
        "if expense not found or belongs to another user."
    )

    # 6. Frontend HTML
    pdf.add_page()
    pdf.h1("6. Frontend HTML (frontend/index.html)")
    pdf.body(
        "Single HTML file with four logical pages, toggled visible/hidden by JavaScript. "
        "No page reloads when switching views."
    )
    pdf.h2("6.1 Pages")
    pdf.bullet("page-login - Email/password login form")
    pdf.bullet("page-signup - New account registration")
    pdf.bullet("page-home - Dashboard: add expense form, total, expense table")
    pdf.bullet("page-chart - Pie chart and category breakdown list")
    pdf.h2("6.2 Key Elements")
    pdf.bullet("form-login / form-signup - Authentication forms")
    pdf.bullet("form-expense - Add or edit expense (category dropdown, amount, comments)")
    pdf.bullet("expense-table - tbody filled dynamically by JavaScript")
    pdf.bullet("pie-chart - CSS conic-gradient pie chart")
    pdf.bullet("error-* elements - Show validation and API error messages")
    pdf.body(
        "Categories: Food, Transport, Shopping, Bills, Entertainment, Health, Other."
    )

    # 7. Frontend CSS
    pdf.add_page()
    pdf.h1("7. Frontend CSS (frontend/css/style.css)")
    pdf.body("Modern, clean UI with card-based layout and responsive design.")
    pdf.h2("7.1 Layout and Theme")
    pdf.bullet(".hidden - display:none for page switching")
    pdf.bullet(".card - White rounded boxes with shadow")
    pdf.bullet(".auth-card - Centered login/signup card (max 400px)")
    pdf.bullet("body - Light gray background (#f0f4f8)")
    pdf.bullet("Primary color #0f3460, danger/error #e94560")
    pdf.h2("7.2 Components")
    pdf.bullet(".btn-primary / .btn-secondary / .btn-danger - Button styles")
    pdf.bullet(".form-row - 3-column grid (1 column on mobile)")
    pdf.bullet("table - Expense list with hover highlight")
    pdf.bullet(".total-amount - Large bold total display")
    pdf.bullet(".pie - 220px circle for conic-gradient chart")
    pdf.bullet(".dot - Color legend dots next to chart labels")

    # 8. Frontend JavaScript
    pdf.add_page()
    pdf.h1("8. Frontend JavaScript (frontend/js/app.js)")
    pdf.h2("8.1 Helper Functions")
    pdf.bullet("showPage(name) - Hide all .page, show page-{name}")
    pdf.bullet("showError(id, msg) - Display error message in element")
    pdf.bullet("getToken / setAuth / clearAuth - localStorage JWT management")
    pdf.bullet("formatDate / formatMoney - Display formatting")
    pdf.bullet("api(path, method, body) - fetch wrapper for /api calls with Bearer token")

    pdf.h2("8.2 api() Function")
    pdf.body(
        "Central function for all backend communication. Sends JSON, attaches Authorization "
        "header if token exists, parses JSON response, throws Error with server message on failure."
    )

    pdf.h2("8.3 loadExpenses()")
    pdf.body(
        "Fetches GET /api/expenses, calculates total, builds table rows with Edit/Delete "
        "buttons, wires click handlers. Edit populates the form; Delete confirms then calls DELETE."
    )

    pdf.h2("8.4 loadChart()")
    pdf.body(
        "Fetches GET /api/expenses/stats/by-category. Builds CSS conic-gradient pie chart "
        "and legend list with percentages. Uses COLORS array for segment colors."
    )

    pdf.h2("8.5 Event Handlers")
    pdf.bullet("Login/Signup forms - POST to /api/auth/login or signup, save token, go to home")
    pdf.bullet("Expense form - POST new or PUT edit based on editId variable")
    pdf.bullet("Logout - Clear localStorage, show login page")
    pdf.bullet("Chart/Back buttons - Switch between home and chart pages")

    pdf.h2("8.6 Startup")
    pdf.body(
        "On load: checkServer() pings /api/health. If token in localStorage, restore session "
        "and load expenses. Otherwise show login page."
    )

    # 9. Data Flow
    pdf.add_page()
    pdf.h1("9. Complete Data Flow")
    pdf.h2("9.1 User Registration")
    pdf.code_block(
        "Browser -> POST /api/auth/signup {email, password}\n"
        "Server -> hash password -> INSERT users -> sign JWT\n"
        "Browser <- {token, email} -> save to localStorage -> show dashboard"
    )
    pdf.h2("9.2 Adding an Expense")
    pdf.code_block(
        "Browser -> POST /api/expenses + Bearer token\n"
        "Server -> authMiddleware -> validate -> INSERT expenses\n"
        "Browser <- {expense} -> reload table and total"
    )
    pdf.h2("9.3 Viewing Chart")
    pdf.code_block(
        "Browser -> GET /api/expenses/stats/by-category + Bearer token\n"
        "Server -> GROUP BY category, SUM(amount)\n"
        "Browser <- {stats} -> draw pie chart with conic-gradient"
    )

    # 10. Security
    pdf.h1("10. Security Features")
    pdf.bullet("Passwords hashed with bcrypt - never stored in plain text")
    pdf.bullet("JWT tokens expire after 7 days")
    pdf.bullet("All expense routes require valid token")
    pdf.bullet("SQL uses parameterized queries (prepared statements)")
    pdf.bullet("Each user can only access their own expenses (user_id filter)")

    # 11. How to Run
    pdf.h1("11. How to Run")
    pdf.code_block(
        "npm install\n"
        "npm start\n"
        "Open http://localhost:3000"
    )
    pdf.body(
        "Important: Always use the server URL. Opening index.html directly in the browser "
        "will fail because /api requests have no server to connect to."
    )

    pdf.h1("12. API Request/Response Examples")
    pdf.h3("Signup Request:")
    pdf.code_block('POST /api/auth/signup\n{"email":"user@example.com","password":"secret12"}')
    pdf.h3("Signup Response (201):")
    pdf.code_block('{"token":"eyJhbG...","email":"user@example.com"}')
    pdf.h3("Create Expense Request:")
    pdf.code_block(
        'POST /api/expenses\n'
        'Authorization: Bearer <token>\n'
        '{"category":"Food","amount":25.50,"comments":"Lunch"}'
    )

    pdf.output(str(OUTPUT))
    print(f"PDF created: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
