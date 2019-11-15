from flask import Flask, render_template
import actionsconfig

app = Flask(__name__)

@app.route("/")
def index():
    return "Placeholder page. Currently these are the available pages:<br><a href='/actions'>Actions</a>"

@app.route("/actions")
def actions():
    return render_template("actions.html", ras_actions=actionsconfig.ras_actions) 


@app.route("/actions/<string:name>/")
def runDefinedFunc(name):
    return actionsconfig.ras_actions[name]["func"](name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')