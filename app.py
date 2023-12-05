from flask import Flask
import portfolio

app = Flask(__name__)

app.register_blueprint(portfolio.bp)

if __name__ == '__main__':
    app.run(debug=True, port=5022)