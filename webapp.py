from flask import Flask, render_template_string, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="post">
        <input type="number" step="any" name="a" placeholder="First number" required>
        <select name="op">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" step="any" name="b" placeholder="Second number" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["op"]

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                error = "Invalid operation"
        except ValueError:
            error = "Please enter valid numbers"
        except ZeroDivisionError as e:
            error = str(e)

    return render_template_string(HTML, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
