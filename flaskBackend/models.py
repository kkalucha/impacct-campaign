from app import db

class Building(db.Model):
    __tablename__ = 'buildings'

    response = db.Column(db.Text())
    response_row = db.Column(db.Text())
    response_row_row = db.Column(db.Text())
    address = db.Column(db.Text())
    id = db.Column(db.Text())
    uuid = db.Column(db.Text())
    position = db.Column(db.Integer)
    building_id = db.Column(db.Integer)
    bin = db.Column(db.Integer)
    street_address = db.Column(db.Text(), primary_key=True)
    block = db.Column(db.Integer)
    lot = db.Column(db.Integer)
    borocode = db.Column(db.Integer)
    borough = db.Column(db.Text())
    zipcode = db.Column(db.Integer)
    latitude = db.Column(db.Numeric(8, 6))
    longitude = db.Column(db.Numeric(8, 6))
    community_board = db.Column(db.Integer)
    council_district = db.Column(db.Integer)
    census_tract = db.Column(db.Integer)
    bbl = db.Column(db.BigInteger)
    nta_neighborhood_tabulation = db.Column(db.Text())

    def __init__(self, street_address):
        self.street_address = street_address

    def __repr__(self):
        return '<address {}>'.format(self.street_address)
    
    def serialize(self):
        return {
            'street_address': self.street_address
        }