## HTTP header viewer

When configuring an application behind a reverse proxy, sometimes you need to check the HTTP headers passed to the application.

This container prints all http headers in the response body.

# Sample output : 

    15:10 [~] $ curl http://localhost:8080
    Accept: */*
    User-Agent: curl/7.64.1

# Usage : 

Run docker image directly : `docker run mirakl/http-headers-viewer`

Build & run : `make run`

