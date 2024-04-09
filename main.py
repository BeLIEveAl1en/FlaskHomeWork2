from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form.get('name')
    email = request.form.get('email')
    response = make_response(redirect('/greet'))
    response.set_cookie('name', name)
    response.set_cookie('email', email)
    return response


@app.route('/greet')
def greet():
    name = request.cookies.get('name')
    if name:
        return render_template('welcome.html', name=name)
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('name', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
