
from libs.db_client import DBClient
from libs.db_models import Zone


def get_zones():
    zones = DBClient.query("zones")
    return zones


def get_one_zone(name):
    search = {"zone_name": name}
    zone = DBClient.query_one("zones", search)
    return zone


def delete_one_zone(name):
    q = {"zone_name": name}
    DBClient.delete_one("zones", q)


def add_one_zone(name, owner):
    zone = Zone(name, owner)
    DBClient.insert("zones", zone.__dict__)


def update_one_zone(name, owner):
    q = {"zone_name": name}
    new_val = {"$set": {"owner": owner}}
    DBClient.update_one("zones", q, new_val)
