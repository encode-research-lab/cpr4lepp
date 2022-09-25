import os
import sys

from flask import Flask


project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)
app.config['SECRET_KEY'] = 'cpr4llp' #need to update it

from route import *

#application = app

if __name__ == '__main__':
    app.run(port=8580, debug=True)
