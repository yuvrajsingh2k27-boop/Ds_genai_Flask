from flask import Flask, request

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def home():
    # Get the 'name' query parameter from the URL
    user_name = request.args.get('name', default="Guest")
    upper_name = user_name.upper()

    return f"<h1>Hello, {upper_name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)