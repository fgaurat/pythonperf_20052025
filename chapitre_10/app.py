from flask import Flask
from CustomerDAO import CustomerDAO
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/")
def index():
    dao = CustomerDAO('customers_db.db')
    customers = dao.findAll()
    html= "<table>"

    for customer in customers:
        html+=f"""
        <tr>
            <td>{customer.id}</td>
            <td>{customer.first_name}</td>
            <td>{customer.last_name}</td>
            <td>{customer.email}</td>
        </tr>        
"""
    html+="</table>"
    return html
