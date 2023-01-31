from app import app
from flask import render_template, request, redirect, url_for
from .pok_API import get_pokemon
from .forms import UserCreationForm, PoknameForm, LoginForm, ProfileForm, CatchForm
from .models import User, caught_pokemon
from flask_login import login_user, current_user, logout_user

@app.route('/')
def homePage():
    people = ['name', "Brandt", "Aubrey","Nicole"]
    text = "SENDING THIS FROM PYTHON!!!"
    
    return render_template('index.html', people = people, my_text = text, user = current_user)

@app.route('/catch', methods=["GET", "POST"])
def catch():
    form = CatchForm()
    if request.method == 'POST':
        if form.validate():
            pokname = form.pokname.data
            
            name,ability, base_experience, image = get_pokemon(pokname)

            caught=caught_pokemon(name, current_user.id, shiny=False)
            caught.saveToDB()
            message = "you caught a Pokemon"
            return render_template('catch.html', form = form, message=message, name=name, ability=ability, base_experience=base_experience, image=image )


    return render_template('catch.html', form = form )
    # if form.validate():
    
@app.route('/searchPage', methods=["GET", "POST"])
def searchPage():
    catchForm = CatchForm()
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

            return render_template('search.html', form = form, catchForm=catchForm, name=name, ability=ability, base_experience=base_experience, image=image )


    return render_template('search.html', form = form, catchForm = catchForm )


@app.route('/signup', methods=["GET", "POST"])
def signUpPage():
    form = UserCreationForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            user_name = form.user_name.data
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
    return redirect(url_for("homePage"), code=302)

@app.route('/profile', methods=["GET", "POST"])
def profile_page():
    form = ProfileForm()
    pokemon = caught_pokemon.query.filter_by(user_id=current_user.id).all()
    if request.method == "POST":
        pass
    return render_template('profile.html', form = form, pokemon = pokemon)


# @app.route('/catch/relase', methods=["GET, POST"])
# def my_pokemon():
#     form = PokeForm()
#     if request.method == "POST":
#         if form.validate():
#             poke_name = form.poke_name.data
#             base_experince = form.base_experince.data

#             catch = catch(poke_name, base_experince,)
#             catch.saveToDB()


#     return render_template('my_pokemon.html', form = form) 

    