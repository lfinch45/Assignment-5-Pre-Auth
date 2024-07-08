class Credentials:

    def __init__(self, url, username, password, customer_id=None, city_born=None, email=None):
        self.url = url
        self.username = username
        self.password = password
        self.customer_id = customer_id
        self.city_born = city_born # For IndianaMCD
        self.email = email # For Artera, MHS, PHP, and TurningPoint