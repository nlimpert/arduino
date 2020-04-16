%bcond_without check

# https://github.com/arduino/arduino-builder
%global goipath         github.com/arduino/arduino-builder
Version:                1.5.2

%gometa

%global common_description %{expand:
A command line tool for compiling Arduino sketches.}

%global golicenses      LICENSE.txt
%global godocs          README.md CONTRIBUTING.md\\\
                        hardware/platform.keys.rewrite.txt

Name:           arduino-builder
Release:        1%{?dist}
Summary:        A command line tool for compiling Arduino sketches

License:        GPLv2
URL:            https://www.arduino.cc/
Source0:        arduino-builder-1.5.2.tar.gz

Provides:       bundled(golang(github.com/arduino/arduino-cli)) = c1dcf01822e9
Provides:       bundled(golang(github.com/arduino/go-paths-helper)) = 1.0.1
Provides:       bundled(golang(github.com/arduino/go-properties-orderedmap)) = 00365bfa6b40
Provides:       bundled(golang(github.com/go-errors/errors)) = 1.0.1
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 1.4.2

%description
%{common_description}

%gopkg

%prep
%autosetup

mkdir -p _build
ln -fs `pwd`/vendor _build/src
ln -fs `pwd` vendor/github.com/arduino/arduino-builder

%build
export GOPATH=`pwd`/_build

%gobuild -o _build/bin/arduino-builder %{goipath}

%install
export GOPATH=`pwd`/_build

%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp _build/bin/*        %{buildroot}%{_bindir}/

%if %{with check}
%check
export GOPATH=`pwd`/_build

%gocheck
%endif

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md hardware/platform.keys.rewrite.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Apr 13 2020 ElXreno <elxreno@gmail.com> - 1.5.2-1
- Initial package

