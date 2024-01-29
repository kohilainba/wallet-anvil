from ._anvil_designer import LoginTemplate
from anvil import *
#import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

class Login(LoginTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        # Get the login input (username, phone number, or email)
        login_input = self.text_box_1.text.strip()
      
        
        # Get the password
        password = self.text_box_2.text.strip()

        # Get the user based on login input
        user = anvil.server.call('get_user_for_login',login_input)

        # Check if user exists and password matches
        if user is not None and user['password'] == password:
            # Check if the user is banned
            if user['banned'] is not None and user['banned']:
                open_form('LOGIN.banned_form')
                return

            # # Check if the user is on hold/freeze
            # if user['hold'] is not None and user['hold']:
            #     alert("Your account is on hold/freeze. Please try again later.", title="Account On Hold")
            #     return

            user_type = user['usertype']

            if user_type == 'admin':
                open_form('admin', user=user)
            elif user_type == 'customer':
                open_form('customer', user=user)
        else:
            self.label_9.text = "Invalid login credentials"
            self.text_box_1.text = ''
            self.text_box_1.focus()
            self.text_box_2.text = ''
            self.text_box_2.focus()

    def button_2_click(self, **event_args):
        open_form('Signup')


# from ._anvil_designer import LoginTemplate
# from anvil import *

# class Login(LoginTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#     # Any code you write here will run before the form opens.
