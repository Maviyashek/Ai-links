from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# this is default username and password
user_pass = {'username': 'username', 'password': 'password'}


@app.route("/", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    if username == user_pass['username'] and password == user_pass['password']:
      return redirect(url_for('welcome', username=username))
    else:
      return "Invalid credentials"

  return render_template('login.html')


@app.route("/Ai_links/<username>")
def welcome(username):
  return render_template('welcome.html', username=username)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
