#
# RPM (Red Hat Package Manager) spec file
# for the Mercury implementation.
# 
# Copyright (C) 1999, 2001, 2002 The University of Melbourne
#
# Please send bugfixes or comments to <mercury-bugs@cs.mu.oz.au>.
#

Summary:      The logic/functional programming language Mercury
Name:         mercury-compiler
Version:      @VERSION_WITH_UNDERSCORES@
Release:      1
Packager:     The Mercury Group <mercury@cs.mu.oz.au>
Vendor:	      The Mercury Group <mercury@cs.mu.oz.au>
Copyright:    GPL and LGPL
Group: 	      Development/Languages
Provides:     mercury 
Requires:     gcc make
Source:       ftp.mercury.cs.mu.oz.au:/pub/mercury/@MAYBE_BETA@mercury-compiler-@VERSION@.tar.gz
URL:	      http://www.cs.mu.oz.au/mercury/

%description
Mercury is a modern logic/functional programming language, which combines
the clarity and expressiveness of declarative programming with advanced
static analysis and error detection features.  Its highly optimized
execution algorithm delivers efficiency far in excess of existing logic
programming systems, and close to conventional programming
systems. Mercury addresses the problems of large-scale program
development, allowing modularity, separate compilation, and numerous
optimization/time trade-offs.

This package includes the compiler, profiler, debugger, documentation, etc.
It does NOT include the "extras" distribution; that is available
from <http://www.cs.mu.oz.au/mercury/download/release.html>.

%changelog
* Sun Feb  8 2004 Fergus Henderson <fjh@cs.mu.oz.au>
- Update to support RedHat 8.0 and Mercury > 0.11.
  In particular:
    use /usr/share/man and /usr/share/info instead of /usr/man and /usr/info;
    use ".1*" instead of ".1" for man pages in order to allow for the
        possibility of them being compressed;
    set INSTALL_PREFIX when doing make install;
    set MERCURY_COMPILER when doing make install,
        in order to allow installing from the source .tar.gz without
	needing an already-installed Mercury compiler;
    mention new files added since Mercury 0.10.

* Thu Oct 16 2002 Fergus Henderson <fjh@cs.mu.oz.au>
- Modify the way the spec file is generated to support building
  RPMS for ROTD releases.

* Wed Apr 04 2001 Fergus Henderson <fjh@cs.mu.oz.au>
- Delete the "Red Hat Contrib Net" stuff, since RHCN seems to have disappeared
  from the face of the earth.

* Fri Feb 19 1999 Fergus Henderson <fjh@cs.mu.oz.au>
- Initial version.

%prep
%setup -n mercury-compiler-@VERSION@

%build
sh configure --prefix=/usr
make

%install
PLATFORM=`./config.guess`
MERCURY_COMPILER=$RPM_BUILD_ROOT%{_libdir}/mercury/bin/$PLATFORM/mercury_compile \
make install \
    INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
    INSTALL_MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
    INSTALL_INFO_DIR=$RPM_BUILD_ROOT%{_infodir}

%files
%doc README* 
%doc NEWS RELEASE_NOTES VERSION WORK_IN_PROGRESS HISTORY LIMITATIONS 
%doc INSTALL INSTALL_CVS 
%doc COPYING COPYING.LIB
%doc samples
/usr/bin/c2init
/usr/bin/canonical_grade
/usr/bin/info_to_mdb
/usr/bin/mdb
/usr/bin/mdemangle
/usr/bin/mfiltercc
/usr/bin/mercury.bat
/usr/bin/mercury_cleanup_install
/usr/bin/mercury_config
/usr/bin/mercury_update_interface
/usr/bin/mgnuc
/usr/bin/mkfifo_using_mknod
/usr/bin/mkinit
/usr/bin/ml
/usr/bin/mmake
/usr/bin/mmc
/usr/bin/mprof
/usr/bin/mprof_merge_runs
/usr/bin/mtags
/usr/bin/vpath_find
/usr/share/man/man1/c2init.1*
/usr/share/man/man1/mdb.1*
/usr/share/man/man1/mercury_config.1*
/usr/share/man/man1/mgnuc.1*
/usr/share/man/man1/ml.1*
/usr/share/man/man1/mmake.1*
/usr/share/man/man1/mmc.1*
/usr/share/man/man1/mprof.1*
/usr/share/man/man1/mprof_merge_runs.1*
/usr/share/man/man1/mtags.1*
/usr/share/info/mercury.info*
/usr/share/info/mercury_faq.info*
/usr/share/info/mercury_library.info*
/usr/share/info/mercury_ref.info*
/usr/share/info/mercury_trans_guide.info*
/usr/share/info/mercury_user_guide.info*
/usr/lib/mercury
