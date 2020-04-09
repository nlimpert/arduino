# Generated by go2rpm 1
%bcond_without check

# https://github.com/codeclysm/extract
%global goipath         github.com/codeclysm/extract
Version:                2.2.0

%gometa

%global common_description %{expand:
A Go library to extract archives in zip, tar.gz or tar.bz2 formats.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go library to extract archives in zip, tar.gz or tar.bz2 formats

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/h2non/filetype)
BuildRequires:  golang(github.com/h2non/filetype/types)
BuildRequires:  golang(github.com/juju/errors)

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
* Thu Apr 09 17:57:22 +03 2020 ElXreno <elxreno@gmail.com> - 2.2.0-1
- Initial package

