from flask import Flask, render_template, request, redirect, url_for, session
import pickle
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# Load the machine learning model
with open('xgboost.pkl', 'rb') as file:
    model = pickle.load(file)

# User data for authentication
users = {
    'admin': generate_password_hash('admin')  # Hashed password for admin
}

@app.route("/", methods=["GET", "POST"])
def home():
    
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("IM IN LOGINN HEYY!!!!!!!!!!!!!")
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('input_page'))  # Redirect to home after successful login
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

# @app.route("/input", methods=["POST", "GET"])
# def input_page():
#     if 'username' not in session:
#         return redirect(url_for('login'))

#     if request.method == "POST":
#         try:
#             Age= int(request.form["Age"])
#             Sex= int(request.form['Sex'])
#             Cp= int(request.form['Cp'])
#             Trestbps = int(request.form[' Trestbps '])
#             Chol = int(request.form['Chol'])
#             Fbs = int(request.form['Fbs'])
#             restecg=int(request.form['restecg'])
#             Thalch = int(request.form['Thalch'])
#             exang=int(request.form['exang'])
#             Oldpeak = int(request.form['Oldpeak'])
#             Slope = int(request.form['Slope'])
#             ca= int(request.form['ca'])
#             thal= int(request.form['thal'])
            
            

#             result = model.predict([[Age, Sex, Cp, Trestbps, Chol, Fbs,restecg, Thalch,exang, Oldpeak,Slope,ca,thal]])
#             res = "High Chance of heart attack" if result[1] == 0 else "Low chance of heart attack"
#             return redirect(url_for('result'))
#         except Exception as e:
#             return str(e)  
#     return render_template("input.html")
@app.route("/input", methods=["POST", "GET"])
def input_page():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        try:
            Age = int(request.form["Age"])
            Sex = int(request.form['Sex'])
            Cp = int(request.form['Cp'])
            Trestbps = int(request.form['Trestbps'])
            Chol = int(request.form['Chol'])
            Fbs = int(request.form['Fbs'])
            Restecg = int(request.form['Restecg'])
            Thalch = int(request.form['Thalch'])
            Exang = int(request.form['Exang'])
            Oldpeak = float(request.form['Oldpeak'])
            Slope = int(request.form['Slope'])
            Ca = int(request.form['Ca'])
            Thal = int(request.form['Thal'])

            result = model.predict([[Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalch, Exang, Oldpeak, Slope, Ca, Thal]])
            res = "High Chance of Heart Attack" if result[0] == 1 else "Low Chance of Heart Attack"
            return render_template('result.html', result=res)
        except Exception as e:
            return str(e)  
    return render_template("input.html")


@app.route("/result")
def result():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("result.html")

@app.route("/chart")
def chart():
   
    
    return render_template("chart.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template("home.html")

if __name__ == '__main__':
    app.run(port=5003, debug=True)

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   