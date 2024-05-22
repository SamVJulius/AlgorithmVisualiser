from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        selected_algorithm = request.form.get('algorithm')
        return redirect(url_for('index', algorithm=selected_algorithm))
    return render_template('form.html')

@app.route('/visualize')
def index():
    algorithm = request.args.get('algorithm', 'bubbleSort')
    return render_template('index.html', algorithm=algorithm)

if __name__ == '__main__':
    app.run(debug=True)
