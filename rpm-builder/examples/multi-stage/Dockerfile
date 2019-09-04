# First half is building the binary
FROM golang:latest

WORKDIR /tmp/golang
RUN git clone https://github.com/golang/example.git
WORKDIR /tmp/golang/example/outyet
RUN go build .

# Second half is packaging the binary in a RPM
FROM mirakl/rpm-builder

COPY --from=0 /tmp/golang/example/outyet/outyet ${SOURCE_DIR}
COPY multi-stage.spec ${SOURCE_DIR}
