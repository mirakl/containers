# rpm-builder

This container allows you to package binaries in a RPM file.    

## Usage : 

Build your binary as usual, and move to the folder containing it.

Write a simple rpmspec file : use the `%add_bin` macro to add a binary to the package.
All binaries must be listed in the `%files` macro.

Example of a basic rpmspec :
```
Name:          my-binary-app
Version:       0.1
Release:       1
Summary:       This binary is a simple cli tool
License:       Owned by Mirakl
URL:           https://github.com/mirakl/repository

%description
https://github.com/mirakl/repository/tree/master/README.md

%install
%add_bin my-binary

%files
%{_bindir}/my-binary

%changelog
* Wed Sep 4 2019 Mathieu Agar <magar@mirakl.com> 0.1
- This is fake changelog for the first version
```

Run the docker image, assuming that the current folder contains the rpmspec and the binary :
```
docker run -v $(pwd):/source -v /tmp:/rpm mirakl/rpm-builder
```

The rpm file will be copied to the /tmp folder when the container run is over.

## Examples : 

Two use case examples are provided with this container : packaging a pre-built binary, and using a multi-stage Dockerfile to 
build and package the binaries.
 
### The simple binary build

The simplest case is to package an already-existing binary (here the [example.sh](examples/simple-binary/example.sh) shell script). 
Files can be found here : [simple-binary example](examples/simple-binary/)

You can use the provided Makefile target to build it :
```
make example-simple-binary
```

### The multi-stage docker build

The idea is to build your binaries from sources inside a container, and build the rpm in a second stage based on this image.
See the [Dockerfile](examples/multi-stage/Dockerfile).

You can use the provided Makefile target to build it :
```
make example-multi-stage
```
