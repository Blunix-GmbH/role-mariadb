.PHONY: help install molecule all clean

help:
	@echo "Available targets are:"
	@echo "- install  - install all dependencies"
	@echo "- molecule - run molecule tests"
	@echo "- clean    - clean up the workspace"

install:
	pip install -r requirements.txt

molecule:
	molecule test --all

all: install molecule

clean:
	rm -rf molecule/*/.molecule
	rm -rf molecule/*/tests/__pycache__
	find . -name \*.pyc -delete
