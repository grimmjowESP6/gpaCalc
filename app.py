from flask import Flask, render_template, request

app = Flask(__name__)

# Default credit structure for 8 semesters
DEFAULT_8_SEM_CREDITS = [19.5, 19.5, 25.5, 21.5, 21.5, 21.5, 23.0, 8.0]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sgpa", methods=["GET", "POST"])
def sgpa_calc():
    sgpa = None
    percentage = None
    entries = []
    num_subjects = request.form.get("num_subjects", type=int)

    if request.method == "POST" and "calculate" in request.form:
        try:
            tgc = 0
            tc = 0
            num_subjects = int(request.form.get("num_subjects", 0))
            for i in range(1, num_subjects + 1):
                g = float(request.form.get(f"gp_{i}", 0))
                c = float(request.form.get(f"credit_{i}", 0))
                entries.append({"name": f"Subject {i}", "grade": g, "credit": c})
                tgc += g * c
                tc += c
            if tc > 0:
                sgpa = tgc / tc
                percentage = (sgpa - 0.75) * 10  # Percentage formula[cite: 2]
        except (ValueError, ZeroDivisionError):
            pass

    return render_template(
        "sgpa.html",
        num_subjects=num_subjects,
        sgpa=sgpa,
        percentage=percentage,
        entries=entries,
    )


@app.route("/cgpa", methods=["GET", "POST"])
def cgpa_calc():
    cgpa = None
    percentage = None
    entries = []
    num_semesters = request.form.get("num_semesters", type=int)
    default_credits = (
        DEFAULT_8_SEM_CREDITS if num_semesters == 8 else [None] * (num_semesters or 0)
    )

    if request.method == "POST" and "calculate" in request.form:
        try:
            tgc = 0
            tc = 0
            num_semesters = int(request.form.get("num_semesters", 0))
            for i in range(1, num_semesters + 1):
                g = float(request.form.get(f"sgpa_{i}", 0))
                # Use hardcoded credit if 8 semesters, else read from form
                if num_semesters == 8:
                    c = DEFAULT_8_SEM_CREDITS[i - 1]
                else:
                    c = float(request.form.get(f"credit_{i}", 0))

                entries.append({"name": f"Semester {i}", "grade": g, "credit": c})
                tgc += g * c
                tc += c
            if tc > 0:
                cgpa = tgc / tc
                percentage = (cgpa - 0.75) * 10  # Percentage formula[cite: 1]
        except (ValueError, ZeroDivisionError):
            pass

    return render_template(
        "cgpa.html",
        num_semesters=num_semesters,
        cgpa=cgpa,
        percentage=percentage,
        entries=entries,
        default_credits=default_credits,
    )


if __name__ == "__main__":
    app.run(debug=True)
