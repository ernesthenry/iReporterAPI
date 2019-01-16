
user_data = []


class User:
    """ model class for users """
    def __init__(
        self, firstname, lastname, othernames, email, phone_number, username, registered, is_admin
        ):
        self._id = len(user_data)+1
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.registered = registered
        self.is_admin = is_admin

    def format_user_record(self):
        return {
        'id': self._id, 
        'firstname': self.firstname, 
        'lastname': self.lastname, 
        'othernames': self.othernames, 
        'email': self.email,
        'phoneNumber': self.phone_number, 
        'username': self.username, 
        'registered': self.registered, 
        'isAdmin': self.is_admin
    }