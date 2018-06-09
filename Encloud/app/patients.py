from app.models import Product
from pymongo import MongoClient
from datetime import datetime
import pdb

def setupdb():
    client = MongoClient("mongodb://Dennis:5a615e66d3c050eb@127.0.0.1:27017/admin")
    db = client.encloud
    return db


def newpatient(details):
    db = setupdb()
    db.patients.insert_one(details)


def insertprescription(id, pre_details):
    db = setupdb()
    pre_details['pid'] = id
    pre_details['datetime'] = datetime.now().replace(second=0,microsecond=0)
    db.prescription.insert_one(pre_details)


def deleterecord(key):
    db = setupdb()
    db.prescription.remove({'_id': key })


def updatekey(id, unset_key):
    db = setupdb()
    db.prescription.update_one({'_id': id}, {'$unset': {unset_key: ""}})


def getdetails(id,daterange=None):
    db = setupdb()
    if daterange is not None:
        sd, ed = map(lambda x: datetime.strptime(x, "%Y/%m/%d"), daterange.split('-'))
        ed = ed.replace(hour=23,minute=59,second=59)
        returnval = list(db.prescription.find({'pid': id, 'datetime': {'$lte': ed, '$gte': sd}}).sort('datetime', -1))
    else:
        returnval = list(db.prescription.find({'pid':id}).sort('datetime',-1))

    #For accordioview (Naming collapse for shrinking effect)
    for counter in range(0,len(returnval)):
        returnval[counter]['lc'] = counter

    return returnval

def getprescriptiondata(id,suffix):
    db = setupdb()
    returnval = db.prescription.find_one({'$and': [{'pid': id}, {'pending_'+suffix:1}]})
    return returnval