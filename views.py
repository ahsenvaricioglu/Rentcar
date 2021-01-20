from flask import render_template, current_app, request, redirect, url_for
from car import Car

def home_page():
    return render_template("base.html")

def login_company():
    return render_template("login_company.html")

def login_customer():
    return render_template("login_customer.html")

def car_list():
    return render_template("car_list_company.html")

def homepage_company():
    return render_template("homepage_company.html")

