import sys
sys.path.append("..")
from tools import req
from tools import dbconnect
from datetime import datetime
import json
import string, random


rq = req.REQ()
qry = dbconnect.DBConnect()

# Method to create random info for a new Customer
def generate_random_info():
    info = {}

    # Generate random email and username
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    info['email'] = "api_user_" + stamp + "@gmail.com"
    info['username'] = "backend."+ stamp

    # Generate random first name and last name 
    all_letters = string.lowercase
    info['first_name'] = "".join(random.sample(all_letters, 8))
    info['last_name'] = "".join(random.sample(all_letters, 8))

    print("The generater email : {}".format(info['email']))
    print("The generater user name : {}".format(info['username']))
    print("The generater first : {}".format(info['first_name']))
    print("The generater last name : {}".format(info['last_name']))

    return info

# Method to test the creation of a new customer from the random data
def test_create_customer():
    print "Running TC1 : Test customer endpoint with random info"

    global username
    global email

    # Generate random user info
    user_info = generate_random_info()
    email = user_info['email']
    username = user_info['username']
    first_name = user_info['first_name']
    last_name = user_info['last_name']

    input_data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "username" : username,
        "billing": {
            "first_name": first_name,
            "last_name": last_name,
            "company": "",
            "address_1": "969 Market",
            "address_2": "",
            "city": "San Francisco",
            "state": "CA",
            "postcode": "94103",
            "country": "US",
            "email": email,
            "phone": "(555) 555-5555"
        },
        "shipping": {
            "first_name": first_name,
            "last_name": last_name,
            "company": "",
            "address_1": "969 Market",
            "address_2": "",
            "city": "San Francisco",
            "state": "CA",
            "postcode": "94103",
            "country": "US"
        }
    }
    # POST the new customer
    # post(endpoint, data)
    res = rq.post("customers", input_data)

    #print res

    response_code = res[0]
    response_body = res[1]

    assert response_code == 201, "Not expected return code, Expected: 201, Actual: {act}".format(act=response_code)

    customer_id = response_body["id"]
    response_email = response_body["email"]
    response_username = response_body["username"]
    response_first_name = response_body["first_name"]
    response_last_name = response_body["last_name"]
    
    assert response_email == email, "The customer's email in response is not the same as the created one, Expected: {}, Actual: {}".format(email, response_email)
    assert response_username == username, "The customer's price in response is not the same as the created one, Expected: {}, Actual: {}".format(response_username, username)
    assert response_first_name == first_name, "The customer's first name in response is not the same as the created one, Expected: {}, Actual: {}".format(response_first_name, first_name)
    assert response_last_name == last_name, "The customer's last name in response is not the same as the created one, Expected: {}, Actual: {}".format(response_last_name, last_name)
    print "Created customer id is: {}".format(customer_id)

    # EOT
    print "The test_create_customer test PASSED"

    # call DB test method
    test_customer_from_db(customer_id)

# Method to test data from the DataBasre
def test_customer_from_db(customer_id):
    print "Running TC2 : Test customer creation from database"

    query = '''SELECT user_login, user_email FROM wp633.ak_users WHERE id = {};'''.format(customer_id)

    res = qry.select('wp633', query)

    #print res

    user_login = res[0][0]
    user_email = res[0][1]

     # Verify the user_name in DB as expected
    assert user_login == username, "The customer username in DB is not as expected. DB name {}".format(user_login)

    # Verify the user_email is as expected
    assert user_email == email, "The customer email in DB is not as expected. DB name {}".format(user_email)

    # EOT
    print "Products positive test case, verify product creared in DB, PASSED"


# run test case
test_create_customer()