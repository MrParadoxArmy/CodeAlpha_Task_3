import subprocess
import flask
from flask import Flask, request, render_template
import os
import pickle

app = Flask(__name__)

# Vulnerable Code (SQL Injection)
# Assuming you're using SQLAlchemy or similar
# user_input = request.args.get('user_id')
# query = "SELECT * FROM users WHERE id = {}".format(user_input) # BAD
# Recommendation: Use parameterized queries
# query = "SELECT * FROM users WHERE id = :user_id"
# result = db.session.execute(query, {'user_id': user_input})

# Vulnerable Code (Command Injection)
def ping(host):
    command = "ping -c 3 " + host  # BAD
    # Recommendation: Use subprocess.run with proper sanitization
    command = ['ping', '-c', '3', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# Vulnerable Code (XSS)
@app.route('/xss', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        comment = request.form['comment']
        # BAD: return "<div>" + comment + "</div>"
        # GOOD:
        return render_template('xss.html', comment=comment)
    return render_template('xss.html', comment='')

# xss.html
# <div >{{ comment | e }}</div>  # e is the escape filter

# Vulnerable Code (CSRF) - Flask Example
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

@app.route('/transfer', methods=['POST'])
def transfer():
    # Requires CSRF token in the form
    amount = request.form['amount']
    # Transfer logic

# Vulnerable Code (Insecure Deserialization)
@app.route('/deserialize', methods=['POST'])
def deserialize():
    data = request.form['data']
    # BAD: obj = pickle.loads(data)
    # Recommendation: Avoid using pickle with untrusted data
    return "Deserialization attempted"

if __name__ == '__main__':
    app.run(debug=True)