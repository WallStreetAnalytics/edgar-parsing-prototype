from mongoengine import Document, StringField


class Company(Document):
    blob = StringField(required=True)

    # add more fields so the above can be parsed into a more
    # granular structure
