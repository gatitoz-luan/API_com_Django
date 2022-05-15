from flask import Flask, request
from flask_cors import CORS, cross_origin
from .src import payment

app = Flask(__name__)
CORS(app)

@app.route('/api/calculateloan', methods=["POST"])
def calculateloan():
    body = request.get_json()

    if("carprice" not in body):
        return "Error - Must be have carprice parameter in request body", 400 
    if("downpayment" not in body):
        return "Error - Must be have downpayment parameter in request body", 400
    if("tradeinvalue" not in body):
        return "Error - Must be have tradeinvalue parameter in request body", 400
    if("lengthofloan" not in body):
        return "Error - Must be have lengthofloan parameter in request body", 400
    if("rate" not in body):
        return "Error - Must be have rate parameter in request body", 400

    rate = body["rate"]
    nper = body['lengthofloan']
    pv = -(body['carprice'] - (body['downpayment'] + body['tradeinvalue']))
    fv = 0

    monthlyPayment =  payment.payment(rate, nper, pv, fv, 1)
    monthlyPayment = round(monthlyPayment, 2)

    totalInterestPaid = (monthlyPayment * nper) + pv
    totalInterestPaid = round(totalInterestPaid, 2)

    totalLoanAndInterestPaid = monthlyPayment * nper
    totalLoanAndInterestPaid = round(totalLoanAndInterestPaid, 2)

    response = {}
    response["status"] = 200
    response["message"] = "success"
    response["carprice"] = body["carprice"]
    response["downpayment"] = body["downpayment"]
    response["totalLoan"] = pv * -1
    response["tradeinvalue"] = body["tradeinvalue"]
    response["totalInterestPaid"] = totalInterestPaid
    response["totalLoanAndInterestPaid"] = totalLoanAndInterestPaid
    response["monthlyPayment"] = monthlyPayment
    
    return response

def generateResponse(status, message, contentName=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message
    if(contentName and content):
        response[contentName] = content
    
    return response
