from app import app
from flask import render_template, request, redirect, url_for
from .pok_API import get_pokemon
from .forms import UserCreationForm, PoknameForm, LoginForm, ProfileForm
from .models import User
from flask_login import login_user, current_user, logout_user

@app.route('/')
def homePage():
    people = ['name', "Brandt", "Aubrey","Nicole"]
    text = "SENDING THIS FROM PYTHON!!!"
    
    return render_template('index.html', people = people, my_text = text, user = current_user)

@app.route('/searchPage', methods=["GET", "POST"])
def searchPage():
    form = PoknameForm()
    pokname = ""
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            pokname = form.pokname.data
    
            
            print(pokname)
            print('begin')
            name,ability, base_experience, image = get_pokemon(pokname)
            print('done')


            return render_template('search.html', form = form, name=name, ability=ability, base_experience=base_experience, image=image )


    return render_template('search.html', form = form )


@app.route('/signup', methods=["GET", "POST"])
def signUpPage():
    form = UserCreationForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            user_name = " "
            email = form.email.data
            password = form.password.data
            
            print(first_name, email, password)

            # add user to database
            user = User(first_name, last_name, user_name, email, password)
            print(user)

            user.saveToDB()

            # return render_template('signup.html', form = form )
            return redirect(url_for('loginPage'))


    return render_template('signup.html', form = form )

@app.route('/login', methods=["GET", "POST"])
def loginPage():
    form = LoginForm()
    error = ''
    if request.method == "POST":
        if form.validate():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user:
                if user.password == password:
                    login_user(user)
                    return redirect("/", code=302)

                else: 
                    error = 'wrong password'

            else: 
                error = 'username does not exist'
        else:
            error = 'invald form'
    
    return render_template('login.html', form = form, error = error)

@app.route('/logout', methods=["GET"])
def logoutRoute():
    logout_user()
    return redirect("/", code=302)

@app.route('/profile', methods=["GET"])
def profile_page():
    logout_user
            
    return redirect(url_for('loginPage'))


    