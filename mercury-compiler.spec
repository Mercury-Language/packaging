#
# RPM (Red Hat Package Manager) spec file
# for the Mercury implementation.
#
# Copyright (C) 1999, 2001, 2002, 2013 The University of Melbourne
#

# Define VERSION and VERSION_WITH_UNDERSCORES with rpmbuild.

Name:         mercury-compiler
Version:      %{VERSION_WITH_UNDERSCORES}
Release:      1
License:      GPL-2.0+ and LGPL-2.0+
Summary:      The logic/functional programming language Mercury
Url:          http://mercurylang.org/
Group:        Development/Languages/Other
Provides:     mercury
Requires:     gcc make
BuildRequires: bison flex
Source:       mercury-srcdist-%{VERSION}.tar.gz

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
It does NOT include the "extras" distribution.

%prep
%setup -n mercury-srcdist-%{VERSION}

%build
sh configure --prefix=/usr
make PARALLEL=%{?_smp_mflags}

%install
PLATFORM=`./config.guess`
MERCURY_COMPILER=$RPM_BUILD_ROOT%{_libdir}/mercury/bin/$PLATFORM/mercury_compile \
make install \
    PARALLEL=%{?_smp_mflags} \
    INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
    INSTALL_MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
    INSTALL_INFO_DIR=$RPM_BUILD_ROOT%{_infodir}

# Don't need these.
rm $RPM_BUILD_ROOT%{_prefix}/bin/*.bat

%post
%install_info --info-dir=%{_infodir} %{_infodir}/mercury.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/mercury.info.gz

%files
%defattr(-,root,root)
%doc README*
%doc NEWS RELEASE_NOTES VERSION WORK_IN_PROGRESS HISTORY LIMITATIONS
%doc COPYING COPYING.LIB
/usr/bin/c2init
/usr/bin/canonical_grade
/usr/bin/info_to_mdb
/usr/bin/mcov
/usr/bin/mdb
/usr/bin/mdemangle
/usr/bin/mdice
/usr/bin/mdprof
/usr/bin/mdprof_cgi
/usr/bin/mdprof_create_feedback
/usr/bin/mdprof_dump
/usr/bin/mdprof_report_feedback
/usr/bin/mdprof_test
/usr/bin/mercury_compile
/usr/bin/mercury_config
/usr/bin/mercury_profile
/usr/bin/mercury_update_interface
/usr/bin/mfiltercc
/usr/bin/mgnuc
/usr/bin/mkfifo_using_mknod
/usr/bin/mkinit
/usr/bin/mkinit_erl
/usr/bin/ml
/usr/bin/mmake
/usr/bin/mmc
/usr/bin/mprof
/usr/bin/mprof_merge_runs
/usr/bin/mslice
/usr/bin/mtags
/usr/bin/mtc
/usr/bin/mtc_diff
/usr/bin/mtc_union
/usr/bin/prepare_install_dir
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

%changelog
* Mon Apr 15 2013 Peter Wang <novalazy@gmail.com>
- See git history.

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

# vim: sts=4 sw=4 et:
