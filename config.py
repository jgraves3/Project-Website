import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'BeepBoopH00t@nDH0ll3R'
