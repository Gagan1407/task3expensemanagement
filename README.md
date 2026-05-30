# Expense Management

Simple expense tracker with login, expense CRUD, and a category pie chart.

## Project structure

| Folder | Purpose |
|--------|---------|
| `backend/` | API, database, login (JWT) — not exposed directly |
| `frontend/` | HTML, CSS, JavaScript — served to the browser |

## Run

```bash
npm install
npm start
```

Open **http://localhost:3000**

> Do not open HTML files directly in the browser. Always use the URL above so the API works.

## Use the app

1. **Sign up** with email and password (min 6 characters)
2. **Add expenses** — category, amount, optional comments
3. **View table** — sorted by newest first
4. **Edit / Delete** — buttons on each row
5. **Pie Chart** — category breakdown (no internet needed)

## Deploy online

This app needs a **Node.js server** (`npm start`). It serves both the website and `/api/*`.

**Netlify will not work** for this project if you only publish the `frontend` folder — login and expenses will fail because the API is missing.

### Deploy on Render (recommended)

1. Push this repo to GitHub: [Gagan1407/task3expensemanagement](https://github.com/Gagan1407/task3expensemanagement)
2. Go to [render.com](https://render.com) and sign in with GitHub
3. Click **New +** → **Blueprint**
4. Select the `task3expensemanagement` repository
5. Render reads `render.yaml` automatically — click **Apply**
6. Wait for the deploy to finish, then open the URL Render gives you (e.g. `https://task3expensemanagement.onrender.com`)

### Manual Render setup (if not using Blueprint)

| Setting | Value |
|---------|--------|
| Environment | Node |
| Build command | `npm install` |
| Start command | `npm start` |

## Commands

| Command | Description |
|---------|-------------|
| `npm start` | Start the app |
| `npm run dev` | Start with auto-restart on code changes |

## Clear all data

Delete the database file and restart:

```bash
rm -f backend/expenses.db
npm start
```

Then log out in the browser (or clear site data for localhost).
