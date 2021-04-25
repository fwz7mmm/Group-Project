#coding=utf8

from datetime import datetime
import json
from flask import render_template, request, abort,send_from_directory,url_for
from . import app

@app.errorhandler(404)
def page_not_found(error):
    title = error
    message = error.description
    return render_template('errors.html',
                           title=title,
                           message=message)


@app.errorhandler(500)
def internal_server_error(error):
    title = error
    message = error.description
    return render_template('errors.html',
                           title=title,
                           message=message)













