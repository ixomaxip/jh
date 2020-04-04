.PHONY: ci


ci:
	docker-compose build $@
down logs ps restart create:
	docker-compose $@
push pull:
	docker-compose $@ ci
log:
	docker-compose logs -f ci | ccze -A

R=docker-compose run --rm
run-ci:
	$R ci
run-sh:
	docker-compose run --rm ci sh
up:
	docker-compose up -d ci

ID=`docker-compose ps -q`
sh:
	docker exec -it $(ID) bash
diff:
	docker diff $(ID)