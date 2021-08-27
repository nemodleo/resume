import sys, os

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer # Added
#from flaskext.markdown import Markdown

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.json'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
#markdown_manager = Markdown(app, extensions=['fenced_code'], output_format='html5',)

@app.route("/")
def index():
    infos = pages.get_or_404("info")
    return render_template('index.html', infos=infos)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=10000)