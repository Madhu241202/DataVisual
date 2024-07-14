from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from  . import mongo, bcrypt

main = Blueprint('main', __name__)


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='scrypt')

        user = mongo.db.users.find_one({'email': email})
        if user:
            flash('Email address already exists.', 'danger')
            return redirect(url_for('main.register'))

        mongo.db.users.insert_one({
            'username': username,
            'email': email,
            'password': hashed_password
        })
        flash('User created successfully!', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = mongo.db.users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login failed. Check your credentials.', 'danger')

    return render_template('login.html')


@main.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
    return render_template('resetpassword.html')


@main.route('/restPassword', methods=['GET', 'POST'])
def resetPassword():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        if password == confirmPassword:
            hashed_password = generate_password_hash(confirmPassword, method='scrypt')
            filter = {'email': email}
            newvalues = {"$set": {'password': hashed_password}}
            user = mongo.db.users.update_one(filter, newvalues)
            if user:
                flash('Password Updated Succssfully!', 'success')
                return render_template('login.html')
            else:
                flash('Password Updation failed.', 'danger')
        else:
            flash('Password match failed.', 'danger')

    return render_template('login.html')


@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@main.route('/data')
def data():
    data = mongo.db.dashboard.find()
    result = []
    topics_distribution ={}
    for item in data:
        result.append({
            'intensity': item['intensity'],
            'likelihood': item['likelihood'],
            'relevance': item['relevance'],
            'year': item['end_year'],
            'country': item['country'],
            'topics': item['topic'],
            'region': item['region'],
            'sector': item['sector']
        })

        topic = item['topic']
        if topic in topics_distribution:
            topics_distribution[topic] += 1
        else:
            topics_distribution[topic] = 1

    return jsonify(result=result, topics_distribution=topics_distribution)


