import mongoengine

class User(mongoengine.Document):
        nid = mongoengine.IntField()
        name=mongoengine.StringField()
        father=mongoengine.StringField()
        mother=mongoengine.StringField()
        date_of_barth= mongoengine.StringField()
        blood_group=mongoengine.StringField()
        address=mongoengine.StringField()
        def to_json(self):
                return{"nid" : self.nid,
                "name": self.name,
                "father": self.father,
                "mother" : self.mother,
                "blood_group" : self.blood_group,
                "address": self.address}