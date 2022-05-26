from flask import Flask
from search_bp import search_bp
from show_bp import show_bp
from upload_bp import upload_bp
from api_bp import api_bp

# creating the app
app = Flask(__name__)

# registering the blueprints that is the search_bp, show_bp, upload_bp, and api_bp
app.register_blueprint(search_bp)
app.register_blueprint(show_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(api_bp)



#main function
if __name__ == '__main__':
    app.run(debug=True)

