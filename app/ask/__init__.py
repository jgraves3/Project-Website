from flask import Blueprint

bp = Blueprint('ask', __name__)

from app.ask import forms, routes 
