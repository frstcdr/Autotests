.PHONY: run-all-tests

run-tests:
	@echo "Tests will be run now..."
	@docker-compose up -d --build
	@docker-compose exec pytest bash


tests-cleanup:
	@echo Containers used for the project will be removed now.
	@docker-compose down && docker system prune -f --volumes
	@echo All unused containers are removed.



.DEFAULT_GOAL := help
