from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from .config import config
from .login_manager import login_manager
from .db import db
from flask_bootstrap import Bootstrap
from .routes import routes_bp
from .apology import apology
app = Flask(__name__)

# db config
app.config.from_object(config)
db.__init__(app)

# login config
login_manager.init_app(app)

# sesion config
Session(app)

#bootstrap config
Bootstrap(app)

'''
 / route is for student
 /admin route is for admin
 /teacher route is for teacher

'''
# routes

# import routes

app.register_blueprint(routes_bp)



@app.errorhandler(404)
def page_not_found(e):
    return apology("page not found", 404)


if __name__ == '__main__':
    app.run(debug=True)