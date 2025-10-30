from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Tapin Backend API Root'

# TODO: Implement user registration, authentication, password reset (with encrypted passwords)
# TODO: Implement listings CRUD endpoints
# TODO: Add API documentation and error handling

if __name__ == '__main__':
    app.run(debug=True)
