from flask import Flask
from prime_numbers import get_prime_numbers
from flask import render_template, request

app = Flask(__name__)
app.debug = True


limit = 1000


@app.route('/')
def home():
    offset = 1
    return render_template ('home.html', limit=limit)


@app.route('/numbers/')
@app.route('/numbers/<offset>')
def prime_numbers(offset = 1):
    number = request.args.get('number', None)
    if offset == 1 and number is not None:
        offset = int(number)
    prime_numbers = get_prime_numbers(int(offset), 1000)
    next_ = prime_numbers[-1] + 1
    end = prime_numbers[-1]
    return render_template ('numbers.html', end = end, next_=next_, limit=limit, offset=offset , numbers=prime_numbers)


if __name__ == '__main__':
    app.run()
