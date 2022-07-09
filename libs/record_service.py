
from libs.db_client import DBClient
from libs.db_models import Record


def add_one_record(rname, zname, rtype, rval, ttl, owner):
    record = Record(rname, zname, rtype, rval, owner, ttl=ttl)
    DBClient.insert("records", record.__dict__)


def get_records():
    zones = DBClient.query("records")
    return zones
