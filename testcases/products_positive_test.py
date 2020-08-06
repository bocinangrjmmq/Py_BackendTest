import sys
sys.path.append("..")
from tools import req
from tools import dbconnect
import json

rq = req.REQ()
qry = dbconnect.DBConnect()

# Method to create a new product
def test_create_product():
    print "Running TC1 : Test product endpoint with basic payload"
    global product_id 
    global name
    global price

    name = "TEST2 TITLE"
    price = "99.99"

    input_data = {
        "name": name,
        "type": "simple",
        "regular_price": price
    }

    # POST the new product
    # post(endpoint, data)
    res = rq.post("products", input_data)
    response_code = res[0]
    response_body = res[1]

    assert response_code == 201, "Not expected return code, Expected: 201, Actual: {act}".format(act=response_code)

    product_id = response_body["id"]
    response_name = response_body["name"]
    response_price = response_body["regular_price"]
    
    assert response_name == name, "The product name in response is not the same as the created one, Expected: {name}, Actual: {response_name}".format(name, response_name)
    assert response_price == price, "The product price in response is not the same as the created one, Expected: {price}, Actual: {response_price}".format(price, response_price)
    print "Created id is: {}".format(product_id)

    # EOT
    print "The test_create_product test PASSED"


def test_verify_new_product_db():
    # Get info form DB
    select_query = '''SELECT id, post_title, meta_value, post_type FROM wp633.ak_posts
            INNER JOIN ak_postmeta ON ak_posts.id = ak_postmeta.post_id
            WHERE post_id = {} AND meta_key = "_price";'''.format(product_id)

    qry_response = qry.select("wp633", select_query)

    print qry_response

    # Extract DB data
    #db_id = qry_response[0][0]
    db_name = qry_response[0][1]
    db_regular_price = qry_response[0][2]
    db_type = qry_response[0][3]

    # Verify the title (product name) in DB as expected
    assert db_name == name, "The product name in DB is not as expected. DB name {}".format(db_name)

    # Verify the post type is as expected
    assert db_type == "product", "The product type in DB is not as expected. DB name {}".format(db_type)

    # Verify the product price is as expected
    assert db_regular_price == price, "The product price in DB is not as expected. DB name {}".format(db_regular_price)

    # EOT
    print "Products positive test case, verify product creared in DB, PASSED"

# Run test cases
test_create_product()
test_verify_new_product_db()

