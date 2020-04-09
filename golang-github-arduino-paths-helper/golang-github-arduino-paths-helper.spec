# Generated by go2rpm 1
%bcond_without check

# https://github.com/arduino/go-paths-helper
%global goipath         github.com/arduino/go-paths-helper
Version:                1.0.1

%gometa

%global common_description %{expand:
A golang library to simplify handling of paths.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A golang library to simplify handling of paths

License:        GPLv2
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu Apr 09 17:43:14 +03 2020 ElXreno <elxreno@gmail.com> - 1.0.1-1
- Initial package

