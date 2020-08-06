import sys
sys.path.append("..")
from tools import req
from tools import dbconnect
import json

rq = req.REQ()
qry = dbconnect.DBConnect()

# Method to create a new product with empty payload
def test_ng_create_product():
    print "Running TC1 : Test product endpoint with empty payload"
    global product_id 
    global name
    global price

    name = ""
    price = ""

    input_data = {}

    # POST the new product
    # post(endpoint, data)
    res = rq.post("products", input_data)
    
    #print res
    print json.dumps(res)    

    response_code = res[0]
    response_body = res[1]

    assert response_code == 400, "Test Case 1: empty payload, Expected: 400, Actual: {act}".format(act=response_code)

    assert response_body == -1, "Test Case 1: empty payload, no content found"
 
    status_code = response_body["data"]["status"]
    assert status_code == 400, "Status code = 400 please make sure to have a valid body"
 
    exp_error_msg = "Content, title, and excerpt are empty."
    act_error_msg = response_body["message"]
 
    assert exp_error_msg == act_error_msg, "Error!! Content is empty, please make sure to have a valid body"
 
    exp_error_code = "empty_content"
    act_error_code = response_body["code"]
    print(act_error_code)
 
    assert exp_error_code == act_error_code, "Error!! Code: empty_content, please make sure to have a valid body"

    # EOT
    print("Negate testcase 1 passed. Empty payload given and verified")

# Method to create a new product with missing name key
def test2_ng_create_product(): 
    print "Running TC2 : Test product endpoint with missing name key"
    global product_id 
    global name
    global price

    name = ""
    price = "99.99"

    input_data = { 
            #"name": name,
            "type": "simple",
            "regular_price": price
        }

    # POST the new product
    # post(endpoint, data)
    res = rq.post("products", input_data)
    
    #print res
    print json.dumps(res)    

    response_code = res[0]
    response_body = res[1]

    assert response_code == 400, "Test Case 2: empty title, Expected: 400, Actual: {act}".format(act=response_code)

    assert response_body == -1, "Test Case 2: empty title"
 
    status_code = response_body["data"]["status"]
    assert status_code == 400, "Status code = 400 please make sure to have a valid body"
 
    exp_error_msg = "Content, title, and excerpt are empty."
    act_error_msg = response_body["message"]
 
    assert exp_error_msg == act_error_msg, "Error!! Content is empty, please make sure to have a valid body"
 
    exp_error_code = "empty_content"
    act_error_code = response_body["code"]
    print(act_error_code)
 
    assert exp_error_code == act_error_code, "Error!! Code: empty_content, please make sure to have a valid body"

    # EOT
    print("Negate testcase 1 passed. Empty payload given and verified")


# Method to create a new product with empty name key
def test3_ng_create_product():
    print "Running TC3 : Test product endpoint with empty name key"



# Run test cases
#test_ng_create_product()
#test2_ng_create_product()
test3_ng_create_product()
#test_ng_verify_new_product_db()