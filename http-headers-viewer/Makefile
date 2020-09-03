VERSION=0.1
NAME=http-headers-viewer
REMOTE=mirakl/$(NAME)

default: build

build:
	docker build . -t $(NAME)

push: build
	docker tag $(NAME) $(REMOTE)
	docker tag $(NAME) $(REMOTE):$(VERSION)
	docker push $(REMOTE)

run: build
	docker run $(NAME)
