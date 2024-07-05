class Credentials:

    def __init__(self, url, username, password, customer_id=None):
        self.url = url
        self.username = username
        self.password = password
        self.customer_id = customer_id