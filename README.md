How to make a Debian binary package
===================================

Download a Mercury srcdist tarball, then run:

    make_deb /path/to/mercury-srcdist-VERSION.tar.gz

You can customise the grades in debian/rules.


How to make an RPM binary package
=================================

Download a Mercury srcdist tarball into ~/rpmbuild/SOURCES (or similar),
then run:

    make_rpm ~/rpmbuild/SOURCES/mercury-srcdist-VERSION.tar.gz

You can customise the grades in mercury-compiler.spec.
