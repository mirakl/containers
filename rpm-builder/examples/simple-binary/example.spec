Name:          sample-app
Version:       0.1
Release:       1
Summary:       This binary is a simple cli tool
License:       Owned by Mirakl
URL:           https://github.com/mirakl/repository

%description
https://github.com/mirakl/repository/tree/master/README.md

%install
%add_bin example.sh

%files
%{_bindir}/example.sh

%changelog
* Wed Sep 4 2019 Mathieu Agar <magar@mirakl.com> 0.1
- The first version of the sample spec file
