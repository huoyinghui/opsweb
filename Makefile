NAME = app_api

all: build

.PHONY : build run

build:
	docker build -t api . -f Dockerfile

run:
	docker run -it --rm -p 8000:8000 -v `pwd`/log:/app/log api
