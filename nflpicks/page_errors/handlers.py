from flask import Blueprint,render_template

page_errors = Blueprint('page_errors',__name__)

@page_errors.app_errorhandler(404)
def error_404(error):
    return render_template('page_errors/404.html'), 404


@page_errors.app_errorhandler(403)
def error_403(error):
    return render_template('page_errors/403.html') , 403
