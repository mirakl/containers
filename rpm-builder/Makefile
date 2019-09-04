VERSION=0.1
NAME=rpm-builder
REMOTE=mirakl/$(NAME)

default: build

build:
	docker build . -t $(NAME)

push: build
	docker tag $(NAME) $(REMOTE)
	docker tag $(NAME) $(REMOTE):$(VERSION)
	docker push $(REMOTE)

clean:
	rm -rf target/*

example-simple-binary: clean build
	docker run -v $(CURDIR)/examples/simple-binary:/source -v $(CURDIR)/target:/rpm $(NAME)

example-multi-stage: clean
	docker build examples/multi-stage/ -t $(NAME)-multi-stage-example
	docker run -v $(CURDIR)/target:/rpm $(NAME)-multi-stage-example
