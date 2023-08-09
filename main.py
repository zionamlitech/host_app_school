from flask import Flask, render_template

app = Flask(__name__)

infos = [
  {
    'id': 1,
    'name': 'kwame',
    'age': 5
  },
  {
    'id': 2,
    'name': 'kwasi',
    'age': 17
  }, 
  {
    'id': 3,
    'name': 'sesse',
    'age': 25
  }
]


@app.route("/")
def school():
  return render_template('/home.html',info=infos)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)