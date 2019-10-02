import os, json, redis, rq
from datetime import datetime, timedelta
from time import time
from flask import current_app, url_for
from bereshet import db
#from bereshet.models.element import Element, Name

#enum mechaber_type = litvak, kabbalist, chassid, ... 
#enum mechaber_period = rishon, acharon ... 

#class Mechaber(Element):
class Mechaber(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    mechabername = db.Column(db.String(64), index=True, unique=True)

    # SQL table elements
    #name = Name(...)
    #date_birth =
    #date_death =
    #place_birth =
    #place_death =
    #places_lived = 
    #links =
    #picture
    #relationships
    #most_known_for
    #mechaber_type
    #mechaber_period
    # sefarim/works = # list of sefer_ids -> to compute
    # mekorot_author # mekorot they authored
    # mekorot_about # mekorot about them

    #def name(self):
    #    return self.name.most_given_name

    def __repr__(self):
        return '<Mechaber {}>'.format(self.mechabername)

    #def to_dict(self):
    #    data = {
    #        'id': self.id,
    #        'username': self.username,
    #        'last_seen': self.last_seen.isoformat() + 'Z',
    #        'about_me': self.about_me,
    #        'post_count': self.posts.count(),
    #        'follower_count': self.followers.count(),
    #        'followed_count': self.followed.count(),
    #        '_links': {
    #            'self': url_for('api.get_user', id=self.id),
    #            'followers': url_for('api.get_followers', id=self.id),
    #            'followed': url_for('api.get_followed', id=self.id),
    #            'avatar': self.avatar(128)
    #        }
    #    }
    #    return data

    def to_dict(self):
        data = {
            'id': self.id,
            'mechabername': self.mechabername
        }
        return data

    def from_dict(self, data):
        for field in data:
            setattr(self, field, data[field])

