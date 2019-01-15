from datetime import datetime 
import uuid

my_red_flags = []


class Redflag:

    def __init__(self, createdBy, _type, place, status, Images, Videos, comment):

        self._id = len(my_red_flags) + 1
        self.createdOn = datetime.now()
        self.createdBy = createdBy
        self.type = _type
        self.location = place
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment

    def format_record(self):

        return {

            "id": self._id,
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "type": self.type,
            "location": self.location,
            "status": self.status,
            "Images": self.Images,
            "Videos": self.Videos,
            "comment": self.comment
        }



class User:

    def __init__(self, firstname, lastname, othernames, email, phone_number, username, registered, is_admin):
        self._id = int(uuid.uuid4())
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
    
