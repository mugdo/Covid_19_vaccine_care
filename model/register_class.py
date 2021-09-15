import mongoengine

class Register(mongoengine.Document):
        nid = mongoengine.IntField()
        center=mongoengine.StringField()
        reg_date=mongoengine.DateField()
        def to_json(self):
                return{"nid" : self.nid,
                "center": self.center,
                "reg_date": self.reg_date,
                 }