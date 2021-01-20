from flask import Flask
import views
from database import Database
from car import Car

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["PORT"] = 8080
    app.add_url_rule("/",view_func=views.home_page)
    app.add_url_rule("/loginCompany", view_func=views.login_company)
    app.add_url_rule("/loginCustomer", view_func=views.login_customer)
    app.add_url_rule("/homepageCompany", view_func=views.homepage_company, methods=["GET", "POST"])

    db = Database()
    app.config["db"] = db
    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)