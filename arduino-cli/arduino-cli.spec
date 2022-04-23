Name:           arduino-cli
Epoch:          1
Version:        0.21.1
Release:        1%{?dist}
Summary:        Arduino command line tool 

License:        GPLv2+ and LGPLv2+ and CC-BY-SA
URL:            https://www.arduino.cc/
Source0:        https://github.com/arduino/arduino-cli/releases/download/%{version}/%{name}_%{version}_Linux_64bit.tar.gz

BuildArch:      x86_64

%description
Arduino is an open-source electronics prototyping platform based on
flexible, easy-to-use hardware and software. It's intended for artists,
designers, hobbyists, and anyone interested in creating interactive
objects or environments.

This package contains an IDE that can be used to develop and upload code
to the micro-controller.


%prep

tar -xzf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check

# Disabled because nothing provides org.fest.swing.*
# # Include requires jars to app/lib folder
# build-jar-repository -p app/test-lib/ \
#     jackson-databind \
#     junit
# 
# # Include library manually
# ln -s /usr/share/java/jackson-modules/jackson-module-mrbean.jar app/test-lib/jackson-module-mrbean.jar
# 
# pushd build
# ant test
# popd


%files
%{_bindir}/%{name}

%changelog
* Tue Apr 28 2020 ElXreno <elxreno@gmail.com> - 1:1.8.12-3
- Fixed running with fresh rsyntaxtextarea library

* Thu Apr 16 2020 ElXreno <elxreno@gmail.com> - 1:1.8.12-2
- Added doc subpackage to requires

* Mon Apr 13 2020 ElXreno <elxreno@gmail.com> - 1:1.8.12-1
- Updated to version 1.8.12

* Mon Apr 13 2020 ElXreno <elxreno@gmail.com> - 1:1.8.5-12
- Fixed run script. RHBZ#1823195

* Sat Apr 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.8.5-11
- Re-add Epoch so package isn't a downgrade

* Tue Apr 07 2020 ElXreno <elxreno@gmail.com> - 1:1.8.5-10
- Set proper java package

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Gianluca Sforna <giallu@gmail.com> - 1:1.8.5-6
- Fix #1518055 by requiring java = 1:1.8.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Peter Oliver <rpm@mavit.org.uk> - 1:1.8.5-4
- Consistenty use appstream ID to ensure inclusion in, e.g., Gnome Software.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.8.5-2
- Remove obsolete scriptlets

* Tue Oct 10 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.8.5-1
- update to 1.8.5
- add versioned require for arduino-builder
- fix buider usage by adding an empty tools-builder directory

* Thu Aug 24 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.8.4-1
- update to 1.8.4

* Wed Aug 23 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.8.3-1
- update to 1.8.3, based off Tom Callaway patches

* Wed Jul 26 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.7-2
- re-uploaded all sources

* Mon Jul 24 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.7-1
- update to 1.6.7
- rebase patches

* Fri Jul 21 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.6-4
- allow arduino-builder to live in /usr/bin
- do not delete needed binary firmware files

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1:1.6.6-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Wed Jul 12 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.6-2
- update astyle patch for 3.0 (#1444550)

* Tue Jan 24 2017 Gianluca Sforna <giallu@gmail.com> - 1:1.6.6-1
- update to 1.6.6

* Sun Oct 30 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-10
- Fixed Bugzilla #1380938

* Thu Sep 22 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-9
- Fixed broken rawhide deps

* Sat Jul 16 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-8
- Fixed Bugzilla #1357005

* Sun Mar 13 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-7
- Fixed Bugzilla #1315104

* Sun Mar 13 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-6
- Fixed Bugzilla #1307326 FTBFS in Rawhide.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-4
- Fix Bugzilla #1296002

* Wed Dec 30 2015 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-3
- Fix the Arduino startup script and redirect system astyle libraries.

* Fri Dec 25 2015 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-2
- Update dependencies list to include newly packaged JSSC.

* Fri Dec 25 2015 Dennis Chen <barracks510@gmail.com> - 1:1.6.4-1
- Update to 1.6.4 and refactor most of the patches and spec file.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr  9 2015 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.6-2
- Passing the --directory argument to `git apply` is no longer required.

* Mon Apr  6 2015 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.6-1
- Update to 1.0.6.

* Tue Jul 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1:1.0.5-8
- optimize mimeinfo scriptlet

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-6
- Associate .ino files with the Arduino IDE.

* Thu Nov  7 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-5
- Force update of icon cache so that icon appears straight away.
- Add appdata.xml.

* Mon Aug  5 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-4
- Unversion documentation directory.

* Mon Aug  5 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-3
- Add arduino-build-platform.patch to allow building on ARM (rhbz 991988).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.5-1
- Update to 1.0.5.
- Remove bug891556.patch.
- Remove wifishield firmware for now, until I figure out whether it's
  reasonable/permissible to include.

* Sat Feb 16 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:1.0.1-4
- own /etc/arudino and /usr/share/arduino (bug 911931)

* Mon Feb 04 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:1.0.1-3
- ino needs to know the arduino version (bug 905681)

* Fri Feb 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com>
- define __AVR_LIBC_DEPRECATED_ENABLE__ (bug 891556)

* Sun Jul 22 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0.1-1
- Update to 1.0.1.
- Compress source with xz.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May  4 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-4
- Pass version number to "ant build" (fixes #815079).

* Sat Jan 14 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-3
- Change the default preferences so that we don't notify the user that a
  new upstream version has been released (#773519).

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan  2 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-2
- Add arduino-no-avrdude64.patch to prevent copying of (for us,
  unbundled) avrdude64.

* Mon Jan  2 2012 Peter Oliver <rpm@mavit.org.uk> - 1:1.0-1
- Update to 1.0 (#753103).
- Drop arduino-use-system-avrdude.patch and arduino-boards-txt.patch,
  since they're no-longer needed.
- Move preferences.txt to /etc.

* Mon Sep 12 2011 Peter Oliver <rpm@mavit.org.uk> - 0022-5
- Treat boards.txt and programmers.txt as config files (#726135).
- Make building with "fedpkg local" work.

* Fri Jul 15 2011 Peter Oliver <rpm@mavit.org.uk> - 0022-4
- Include missing examples (#722351).

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0022-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 31 2010 Peter Oliver <rpm@mavit.org.uk> - 0022-2
- Prompt the user if they are not a member of the required groups,
  rather than failing silently.

* Thu Dec 30 2010 Peter Oliver <rpm@mavit.org.uk> - 0022-1
- Update to 0022 release (#666309).
- Use the new upstream source tarball rather than git.
- Drop oro requirement and related patch, since it is no-longer used.

* Fri Dec 17 2010 Peter Oliver <rpm@mavit.org.uk> - 0021-2
- Patch boards.txt to use the "arduino" programmer type for Uno boards,
  allowing Fedora's version of avrdude to work with these boards.

* Thu Oct  7 2010 Peter Oliver <rpm@mavit.org.uk> - 0021-1
- New upstream release 0021.
- Add patch for new upstream icons.
- Override device scan in RXTX to allow use of Arduino Uno.

* Mon Sep 20 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-6
- Explictly mention documentation with doc macro.
- Move reference documentation into -doc package.

* Thu Sep  9 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-5
- Add missing BuildRequires.
- Use build-jar-repository to locate java libraries to build against.
- Eliminate cross-package symlinks.

* Wed Sep  8 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-4
- Make sure all jars are removed from the source bundle.
- Add missing documentation.

* Tue Sep  7 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-3
- Split into two packages, making the IDE optional to install.
- Build during the build phase not the install phase.
- More dependencies.

* Mon Sep  6 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-2
- Expanded dependencies.

* Sun Sep  5 2010 Peter Oliver <rpm@mavit.org.uk> - 0019-1
- Initial version.  Based in part on the Debian package.
