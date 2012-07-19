from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.snip.models import Snippet
from app.snip.forms import snipForm
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name


mod = Blueprint('account', __name__, url_prefix='/snippets')


@mod.route('/add/', methods=['GET', 'POST'])
def login():
    form = snipForm(request.form)

    if form.validate_on_submit():
        snip = Snippet(form.name.data, "html", form.code.data)
        db.session.add(snip)
        db.session.commit()
        flash('Snipeet added', 'success-message')
    return render_template("snip/addSnip.html", form=form)


@mod.route('/view/', methods=['GET', 'POST'])
def view():
    snippet = Snippet.query.filter_by(id=2).first()
    code =  highlight(snippet.code, PythonLexer(), HtmlFormatter())
    return render_template("snip/Snip.html", snippet=snippet, code=code)
