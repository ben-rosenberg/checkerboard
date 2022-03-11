from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

# It would be cool to render an error page instead of simply returning
# a string.
@app.route('/<num_rows>')
def rows(num_rows):
    if not num_rows.isnumeric():
        return 'Error: Please enter an integer'
    return render_template('index.html', num_rows=int(num_rows))

@app.route('/<num_rows>/<num_columns>')
def rows_and_columns(num_rows, num_columns):
    if not num_rows.isnumeric() or not num_columns.isnumeric():
        return 'Error: Inputs must be positive integers'
    return render_template(
        'index.html', num_rows=int(num_rows), num_columns=int(num_columns))

# I have no idea how to check that the input is a valid color
# Is there a way to avoid the code repetition here? I feel like I'm missing
# something obvious.
@app.route('/<num_rows>/<num_columns>/<color1>')
def rows_columns_color1(num_rows, num_columns, color1):
    if not num_rows.isnumeric() or not num_columns.isnumeric():
        return 'Error: First two inputs must be positive integers'
    return render_template(
        'index.html', num_rows=int(num_rows), 
        num_columns=int(num_columns), color1=color1)

@app.route('/<num_rows>/<num_columns>/<color1>/<color2>')
def rows_columns_color1_color2(num_rows, num_columns, color1, color2):
    if not num_rows.isnumeric() or not num_columns.isnumeric():
        return 'Error: First two inputs must be positive integers'
    return render_template(
        'index.html', num_rows=int(num_rows), 
        num_columns=int(num_columns), color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug = True);