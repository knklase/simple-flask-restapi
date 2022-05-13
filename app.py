
from flask import Flask, request, jsonify

from database import setup
from resources.tasks import task_bp


# create the Flask app
app = Flask(__name__)

setup.create_tables()

app.register_blueprint(task_bp)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)










