import os
from jinja2 import Template
from flask import Flask
from flask import request

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

loc_reject_template = Template("""
<html>
  <head><title>Sorry - {{name}}</title></head>
  <body align="center">
    <h1>Sorry, I can only serve requests for {{location}}!</h1>
    <br />
    <h2>Powered by {{name}}, {{location}}</h2>
  </body>
</html>
""")


def get_location():
    return request.args.get('loc', 'india').lower()


@app.route("/")
def hello():
    return "<h1 align='center'>Hello from %s, %s!</h1>" % (identity["name"], identity["location"])


@app.route("/add/<int:a>/<int:b>/")
def add(a, b):
    req_location = get_location()
    if identity["function"].lower() not in ["addition", "all"]:
        return reject_template.render(**identity)
    elif identity["location"].lower() != "india" and req_location != identity["location"].lower():
        return loc_reject_template.render(**identity)
    else:
        values = {
            "a": a,
            "b": b,
            "ans": a + b,
            "action": "Addition",
            "opp": "+",
        }
        values.update(identity)
        return ans_template.render(**values)


@app.route("/sub/<int:a>/<int:b>/")
def sub(a, b):
    req_location = get_location()
    if identity["function"].lower() not in ["subtraction", "all"]:
        return reject_template.render(**identity)
    elif identity["location"].lower() != "india" and req_location != identity["location"].lower():
        return loc_reject_template.render(**identity)
    else:
        values = {
            "a": a,
            "b": b,
            "ans": a - b,
            "action": "Subtraction",
            "opp": "-",
        }
        values.update(identity)
        return ans_template.render(**values)


@app.route("/mul/<int:a>/<int:b>/")
def mul(a, b):
    req_location = get_location()
    if identity["function"].lower() not in ["multiplication", "all"]:
        return reject_template.render(**identity)
    elif identity["location"].lower() != "india" and req_location != identity["location"].lower():
        return loc_reject_template.render(**identity)
    else:
        values = {
            "a": a,
            "b": b,
            "ans": a * b,
            "action": "Multiplication",
            "opp": "X",
        }
        values.update(identity)
        return ans_template.render(**values)


@app.route("/div/<int:a>/<int:b>/")
def div(a, b):
    req_location = get_location()
    if identity["function"].lower() not in ["division", "all"]:
        return reject_template.render(**identity)
    elif identity["location"].lower() != "india" and req_location != identity["location"].lower():
        return loc_reject_template.render(**identity)
    else:
        values = {
            "a": a,
            "b": b,
            "ans": a / b,
            "action": "Division",
            "opp": "%",
        }
        values.update(identity)
        return ans_template.render(**values)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
