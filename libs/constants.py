import os

# constants
VERSION = "1.0.0"
ROOT_ZONE = os.environ.get("ROOT_ZONE", "http://localhost:8080")


class HTTP:
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"
