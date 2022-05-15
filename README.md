# :car: Car Loan Api

Car Loan is a RESTful API written in Python. The main objective is to calculate auto loans in a simple and fast way.

**[https://carloan.netlify.app/](https://carloan.netlify.app/)**

## Installation

To install Car Loan, you need to clone car-loan-api repository and set your workspace.

1. You can use the command below to clone the car-loan-api repository on your terminal

```sh
$ git clone https://github.com/WilliamSilveiraF/car-loan-api.git
```

2. Then install all project dependencies

```sh
$ pip install -r requirements.txt
```

## Unitary Tests

Run the commands below to execute the tests
```sh
$ cd app
```
```sh
$ python3 -m unittest test_app.py
```

## Quick start

```sh
# Run the below command in repository root to execute the project on your local machine
$ python3 wsgi.py
```
The application will be ready on port `http://localhost:5000/`

## Deploy

We have a demo api running on heroku `https://car-loan-api.herokuapp.com/`, you can use this url to consume the api too

## Requests

```python
# Route: POST https://car-loan-api.herokuapp.com/api/calculateloan
payload = {
  "carprice": 50000,  #required
  "downpayment": 0,   #required
  "tradeinvalue": 0,  #required
  "lengthofloan": 18, #required
  "rate": 0.06        #required
}
```

```python
# Return
{
  "carprice": 50000,
  "downpayment": 0,
  "message": "success",
  "monthlyPayment": 2897.1,
  "status": 200,
  "totalInterestPaid": 2147.8,
  "totalLoan": 50000,
  "totalLoanAndInterestPaid": 52147.8,
  "tradeinvalue": 0
}
```

##  Developed by
- [WilliamSilveiraF](https://github.com/WilliamSilveiraF)
- [Luan Costa](https://github.com/gatitoz-luan)
