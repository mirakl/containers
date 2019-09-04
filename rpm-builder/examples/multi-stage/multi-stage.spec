Name:          outyet
Version:       0.1
Release:       1
Summary:       A web server that answers the question: "Is Go 1.x out yet?"
License:       Apache License 2.0
URL:           https://github.com/golang/example

%description
https://github.com/golang/example/blob/master/README.md

%install
%add_bin outyet

%files
%{_bindir}/outyet

%changelog
* Wed Sep 4 2019 Mathieu Agar <magar@mirakl.com> 0.1
- Install a golang example binary with rpm-builder
