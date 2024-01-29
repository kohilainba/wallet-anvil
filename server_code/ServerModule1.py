import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import anvil.server
from anvil import tables, app
import random
import uuid

@anvil.server.callable
def get_user_for_login(login_input):
  user_by_username = app_tables.wallet_users.get(username=login_input)
  if login_input.isdigit():
    phone_number = int(login_input)
    user_by_phone = app_tables.wallet_users.get(phone=phone_number)
    return user_by_phone
    # Continue with the rest of your code
  else:
    print("Invalid phone number. Please enter a numeric value.")
  user_by_email = app_tables.wallet_users.get(email=login_input)
  if user_by_username:
            return user_by_username
  if user_by_email:
            return user_by_email 
  else:
            return None

@anvil.server.callable
def add_info(email, username, password, pan, address, phone, aadhar):
    user_row = app_tables.wallet_users.add_row(
        email=email,
        username=username,
        password=password,
        pan=pan,
        address=address,
        phone=phone,
        aadhar=aadhar,
        usertype='customer',
        confirm_email=True,
        user_limit=(100000),
        last_login = datetime.now()
    )
    return user_row

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
