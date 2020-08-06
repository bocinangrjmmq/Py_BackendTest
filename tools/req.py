from woocommerce import API

class REQ:
    def __init__(self):
        adm_consumer_key = 'ck_f5fcf679cc65d438ba8188e867610e18a6486ee5'
        adm_consumer_secret = 'cs_4c312c0392d86938a4469c432ba15aa78977bb3f'

        self.wcapi = API(
            url="http://127.0.0.1/ak_store/",
            consumer_key= adm_consumer_key,
            consumer_secret= adm_consumer_secret,
            wp_api=True,
            version="wc/v2")

    # def test_api(self):
    #     print self.wcapi.get("").json()

    def post(self, endpoint, data):
        result = self.wcapi.post(endpoint, data)
        
        resp_code = result.status_code
        resp_body = result.json()
        resp_url = result.url 

        return [resp_code, resp_body, resp_url]

    def get(self, endpoint):
        result = self.wcapi.get(endpoint)

        resp_code = result.response_code
        resp_body = result.json()
        resp_url = result.url 

        return [resp_code, resp_body, resp_url]

    

# test1 = REQ()
# test1.test_api()