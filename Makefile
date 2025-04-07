#docker run -it --rm --network host -v "$(pwd)":/app -w /app python:3.6-slim bash -c "pip3 install -r requirements.txt && exec bash"
IMAGE := python:3.11-slim
WORKDIR := /app

.PHONY: run
run:
	docker run -it --rm \
		--network host \
		-v "$(PWD)":$(WORKDIR) \
		-w $(WORKDIR) \
		$(IMAGE) bash

.PHONY: shell
shell:
	@echo "Spawning Python shell in Docker..."
	docker run -it --rm \
		--network host \
		-v "$(PWD)":$(WORKDIR) \
		-w $(WORKDIR) \
		$(IMAGE) python

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make run     - Start a bash shell in Python 3.5 container with current dir mounted"
	@echo "  make shell   - Start a Python shell directly"

# TODO
# Add a command here to install current module
# pip install -e .
