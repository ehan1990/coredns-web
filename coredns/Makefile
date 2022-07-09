
build:
	docker build -t edwhan/coredns:latest .

run:
	docker run -d --rm --network host --name coredns edwhan/coredns:latest

ssh:
	docker exec -it coredns bash
