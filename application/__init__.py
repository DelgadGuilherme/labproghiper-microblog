from flask import Flask
import os

templates_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__,template_folder=templates_folder,static_folder=static_folder)


from application.controller import hello_controller