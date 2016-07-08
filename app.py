import os
from jinja2 import Template
from flask import Flask

app = Flask(__name__)

identity = {
    "name": os.environ.get('NAME', "Abacus"),
    "location": os.environ.get('LOCATION', "India"),
    "function": os.environ.get('FUNCTION', "all"),
}

ans_template = Template("""
<html>
  <head><title>{{action}} - {{name}}</title></head>
  <body align="center">
    <h1>{{action}}</h1>
    <h1>{{a}} {{opp}} {{b}} = {{ans}}</h1>
    <br />
    <h2>Powered by {{name}}, {{location}}</h2>
  </body>
</html>
""")

reject_template = Template("""
<html>
  <head><title>Sorry - {{name}}</title></head>
  <body align="center">
    <h1>Sorry, I can only perform {{function}}!</h1>
    <br />
    <h2>Powered by {{name}}, {{location}}</h2>
  </body>
</html>
""")


@app.route("/")
def hello():
    return "<h1 align='center'>Hello from %s, %s!</h1>" % (identity["name"], identity["location"])


@app.route("/add/<int:a>/<int:b>/")
def add(a, b):
    if identity["function"].lower() in ["addition", "all"]:
        values = {
            "a": a,
            "b": b,
            "ans": a + b,
            "action": "Addition",
            "opp": "+",
        }
        values.update(identity)
        return ans_template.render(**values)
    else:
        return reject_template.render(**identity)


@app.route("/sub/<int:a>/<int:b>/")
def sub(a, b):
    if identity["function"].lower() in ["subtraction", "all"]:
        values = {
            "a": a,
            "b": b,
            "ans": a - b,
            "action": "Subtraction",
            "opp": "-",
        }
        values.update(identity)
        return ans_template.render(**values)
    else:
        return reject_template.render(**identity)


@app.route("/mul/<int:a>/<int:b>/")
def mul(a, b):
    if identity["function"].lower() in ["multiplication", "all"]:
        values = {
            "a": a,
            "b": b,
            "ans": a * b,
            "action": "Multiplication",
            "opp": "X",
        }
        values.update(identity)
        return ans_template.render(**values)
    else:
        return reject_template.render(**identity)


@app.route("/div/<int:a>/<int:b>/")
def div(a, b):
    if identity["function"].lower() in ["division", "all"]:
        values = {
            "a": a,
            "b": b,
            "ans": a / b,
            "action": "Division",
            "opp": "%",
        }
        values.update(identity)
        return ans_template.render(**values)
    else:
        return reject_template.render(**identity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
