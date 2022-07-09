
coredns-build:
	docker-compose build coredns

coredns-up:
	docker-compose up

coredns-ssh:
	docker exec -it coredns bash

db-up:
	docker run --name db -p 27017:27017 -d mongo mongod

db-ssh:
	docker exec -it db bash

health:
	@curl -s localhost:8080/healthcheck | jq

# ZONE=foobar.com make add-zone
add-zone:
	@curl -d '{"name": "${ZONE}", "owner": "ed"}' -X POST localhost:8080/zones

get-zones:
	@curl localhost:8080/zones

# RECORD=ed.foobar.com VAL=1.1.1.1 TYPE=A make add-record
add-record:
	@curl -d '{"rname": "${RECORD}", "rtype": "${TYPE}", "rvalue": "${VAL}", "ttl": 60}' -X POST localhost:8080/records

get-records:
	@curl localhost:8080/records
