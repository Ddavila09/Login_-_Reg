from login_reg import app
from flask import render_template, request, redirect, session


from login_reg.models.user_model import User

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/new_user', methods=['POST'])
def new_user():
        
    if not User.validate(request.form):
        return redirect('/')
    
    
    User.register(request.form)
    
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    
    
    
    found_user = User.validate_login(request.form)
    
    if found_user:
        
        session['uid'] = found_user.id
        
        
        return redirect('/dashboard')
    else:
        return redirect('/')
    
    



@app.route('/dashboard')
def dashboard():
    
    if 'uid' not in session:
        return redirect('/')
    
    
    return render_template("dashboard.html", user = User.get_one(session['uid']))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')