from datetime import datetime

user_data = []


class User:
    """ model class for users """
    def __init__(self, **kwargs):
        self._id = len(user_data)+1
        self.firstname = kwargs["firstname"]
        self.lastname = kwargs["lastname"]
        self.othernames = kwargs["othernames"]
        self.email = kwargs["email"]
        self.phone_number = kwargs["phone_number"]
        self.username = kwargs["username"]
        self.registered = datetime.now()
        self.is_admin = False

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