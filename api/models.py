from datetime import datetime

my_red_flags = []


class Redflag:

    def __init__(self, createdBy, _type, place, status, Images, Videos, comment):

        self.id = len(my_red_flags) + 1
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

            "id": self.id,
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "type": self.type,
            "location": self.location,
            "status": self.status,
            "Images": self.Images,
            "Videos": self.Videos,
            "comment": self.comment
        }
