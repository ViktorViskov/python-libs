from controller_sqlite import Controller


c = Controller()
c.get_address_by_user_login("rj")
print(c.address_count())
