import datetime
import logging

from flask import Flask, jsonify, request

from libs import zone_service, record_service, constants
from libs.db_client import DBClient

"""
CRUD records
ACL on IAM

"""


app = Flask(__name__)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(filename)s:%(lineno)d %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def write_file(path, data):
    with open(path, "a") as f:
        f.write(f"\n{data}")


@app.route("/zones", methods=["GET", "POST"])
def zones_endpoint():
    if request.method == "GET":
        zones = zone_service.get_zones()
        return jsonify(zones)
    else:
        req_data = request.get_json(force=True)
        name = req_data.get("name")
        owner = req_data.get("owner")
        zone_service.add_one_zone(name, owner)
        return "ok\n"


@app.route("/zones/<zname>", methods=["GET", "DELETE", "PUT"])
def zone_single_endpoint(zname):
    if request.method == "DELETE":
        zone_service.delete_one_zone(zname)
        return "ok\n"
    elif request.method == "GET":
        zone = zone_service.get_one_zone(zname)
        if zone:
            return jsonify(zone)
        return {}
    elif request.method == "PUT":
        req_data = request.get_json(force=True)
        owner = req_data.get("owner")
        zone_service.update_one_zone(zname, owner)
        return "ok\n"
    else:
        return f"invalid method {request.method}", 400


@app.route("/records", methods=["GET", "POST"])
def records_endpoint():
    if request.method == "POST":
        req_data = request.get_json(force=True)
        record_name = req_data.get("rname")
        zone_name = req_data.get("zname")
        record_value = req_data.get("rval")
        record_type = req_data.get("rtype")
        ttl = req_data.get("ttl")
        owner = req_data.get("owner")

        record_service.add_one_record(record_name, zone_name, record_type, record_value, ttl, owner)
        return "ok\n"
    else:
        records = record_service.get_records()
        return jsonify(records)


@app.route("/healthcheck", methods=["GET"])
def healthcheck_endpoint():
    db_health = DBClient.healthcheck()
    data = {
        "db_health": db_health,
        "msg": f"Running version {constants.VERSION}",
        "date": f"{datetime.datetime.utcnow().isoformat()[0:19]}Z",
    }
    return jsonify(data)


def main():
    DBClient.init("coredns")
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)


if __name__ == "__main__":
    main()
