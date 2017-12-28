from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SearchBar

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='SignIn', form=form)

@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': "Karthik"}
    searchBar = SearchBar()
    return render_template('index.html', title='Home', user=user, form=searchBar)
