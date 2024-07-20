from flask import Flask, render_template,jsonify

app = Flask(__name__)


Task=[
  {"Category":1, "title":"Learn Python", "done":False,"details":"Learn Matplotlib","Deadline":"2023-01-01"},
  {"Category":2, "title":"Learn Web D", "done":True,"details":"Learn Flask"},
]

Meetings=[
  {"Topic":"Robob AI", "Date":"2023-01-01", "Time":"10:00"},
  {"Topic":"SAE", "Date":"2023-01-01", "Time":"12:00"},
]

@app.route("/api/json")
def list_tasks():
  return jsonify(Task)

@app.route('/')
def hello_world():
    return render_template('home.html',tasks=Task,meet=Meetings)


if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)