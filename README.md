# Academic GPA & CGPA Calculator

A lightweight, modern web application built with **Flask**, **Bootstrap 5**, and packaged via **uv**. It allows university students to calculate their Semester Grade Point Average (**SGPA**), Cumulative Grade Point Average (**CGPA**), and convert them directly to official percentages.

---

## Features

- **Dynamic Form Generation**: Specify the number of subjects or semesters, and the form dynamically generates the required input fields.
- **Pre-configured 8-Semester Credit Scheme**: Automatically locks and pre-fills credits for 8-semester programs:
  - `S1`: 19.5 | `S2`: 19.5 | `S3`: 25.5 | `S4`: 21.5
  - `S5`: 21.5 | `S6`: 21.5 | `S7`: 23.0 | `S8`: 8.0
- **Clean Result View**: Once submitted, input tables disappear and are replaced with a clear breakdown of entered grades and calculated totals.
- **Percentage Conversion**: Automatically calculates equivalent percentages using standard conversion formulas.
- **Fully Responsive**: Designed with mobile-first Bootstrap components for smartphones, tablets, and desktops.

---

## Formulas Used

### 1. SGPA (Semester Grade Point Average)
$$\text{SGPA} = \frac{\sum_{i=1}^{n} (\text{Grade Point}_i \times \text{Credit}_i)}{\sum_{i=1}^{n} \text{Credit}_i}$$

### 2. CGPA (Cumulative Grade Point Average)
$$\text{CGPA} = \frac{\sum_{j=1}^{m} (\text{SGPA}_j \times \text{Credit}_j)}{\sum_{j=1}^{m} \text{Credit}_j}$$

### 3. Percentage Conversion
$$\text{Percentage} = (\text{GPA} - 0.75) \times 10$$

---

## Tech Stack

- **Backend**: [Python](https://www.python.org/) & [Flask](https://flask.palletsprojects.com/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (fast Python package installer & resolver)
- **Production Server**: [Gunicorn](https://gunicorn.org/)
- **Frontend / Styling**: HTML5, Jinja2, [Bootstrap 5](https://getbootstrap.com/)
- **Hosting**: [Render](https://render.com/)

---

## Project Structure

```text
gpaCalc/
│
├── app.py                  # Flask server logic & routes
├── pyproject.toml          # Project configuration & dependencies
├── uv.lock                 # Deterministic dependency lockfile
├── requirements.txt        # Production deployment dependency list
│
└── templates/              # Jinja2 presentation templates
    ├── base.html           # Navbar & layout frame
    ├── index.html          # Landing page
    ├── sgpa.html           # Subject-level SGPA calculator
    └── cgpa.html           # Semester-level CGPA calculator
```

---

## Local Development Setup

### 1. Prerequisites
Install `uv` if you haven't already:
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repository
```bash
git clone https://github.com/<YOUR-USERNAME>/gpaCalc.git
cd gpaCalc
```

### 3. Install Dependencies
```bash
uv sync
```

### 4. Run the Development Server
```bash
uv run python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Production Deployment (Render)

1. Push your repository to GitHub.
2. Link your repository in [Render.com](https://render.com) as a **Web Service**.
3. Use the following configuration:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: `Free`

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to adapt and customize it for your institution's grading system!