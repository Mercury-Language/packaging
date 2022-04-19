How to make a Debian binary package
===================================

The Debian/.deb packages are published at
on the [Mercury Downloads](http://dl.mercurylang.org/deb/) site.
This repository and README.md file documents how they're built.

Read all the instructions before you begin.  This will cover building
packages and maintaining the repository.  It won't explain how Debian
packages are/should be built (see the
[Debian Policy Manual](https://www.debian.org/doc/debian-policy/)),
how the various tools work,
how the Mercury build system works or
how GPG keys should be managed;
all that can be found elsewhere.

About this repo
---------------

Mercury releases have not always had a regular schedule.  In this repository
we will track packaging for the ROTD builds and use branches to track
releases & backports.

Setup the tools
---------------

You will need some Debian tools to make Debian packages.

    apt install build-essential \
      devscripts \
      pbuilder \
      fakeroot \
      dput \
      debian-keyring \
      debian-archive-keyring \
      debian-ports-archive-keyring

And if you plan to maintain the repository, then also install

    apt install reprepro rsync

Investigate each of the files in debian\_conf and install them or their
contents as necessary.

### bashrc

Copy the contents of bashrc into your ~/.bashrc file, modify it as necessary
to set your name and e-mail address.  The dquilt alias works with
.dquiltrc-dpkg below.

### quiltrc-dpkg

Quilt is a tool for managing a series of patches.  It's used to patch the
source for a package before building it, to fix any bugs, apply backports
etc.

Configuration file used with the dquilt alias for the quilt patch management
tool.  This simply configures quilt for use with debian packages, by
providing some sensible defaults.  The 'd' in 'dquilt' is for Debian.

### pbuilderrc

pbuilder is a "Personal Builder" it is used to build debian packages in a
chroot, ensuring that they can be built cleanly & don't have any extra
dependencies.

This file can be coppied to ~/.pbuilderrc more-or-less verbatim, but read it
anyway and get a sense for what it can do, particularly since it's a shell
script!  Set the username, any distribution codenames that may have changed
since I wrote this, and your mirror sites.

You may need to create some directories in /var/cache/pbuilder.
Particularly the hooks and result directories.

   sudo mkdir /var/cache/pbuilder/hooks /var/cache/pbuilder/result

Copy C10shell into /var/cache/pbuilder/hooks  The C hooks are executed if a
build fails, you can use them, for example this one, to determine why the
build failed.

   sudo cp C10shell /var/cache/pbuilder/hooks/

### sudoers

pbuilder (normally) needs sudo access, but it also needs access to some
environment variables.  Edit your sudoers file.  Remeber to use the visudo
command.

    sudo visudo -f /etc/sudoers.d/pbuilder

Add to the Command alias section:

    Cmnd_Alias  PBUILDER = /usr/sbin/pbuilder, /usr/bin/pdebuild, /usr/bin/debuild-$
    Defaults!PBUILDER       env_keep+="DIST ARCH"

And add to the user privilege specification section:

    # User privilege specification
    paul    ALL=(ALL) PBUILDER

Change "paul" to your username.

Don't make a mistake and get locked out of sudo access.

### Setup chroots

Setup any chroots you need.

    ARCH=amd64 DIST=sid sudo pbuilder --create

Hopefully you have an amd64 system, which means you can build either amd64
or i386 packages and chroots.

### Setup dput

Depending on whether you're maintaining the Mercury repository, or just
building packages and sending them to someone else you'll want to use a
different dput configuration.  I've included my ~/.dput.cf which assumes I'm
maintaining the repository myself over a local NFS mount.  Copy it and edit
the path or else check the manual and write your own configuration.

Each stanza refers to a repository.  Right now there is only one,
mercury-stable, I plan to add mercury-snapshot in the future.


Build packages
--------------

Download a Mercury srcdist tarball, extract it and rename the root
directory to give it a sensible name. Then tar it back up again with the new
special name.  Normally you can simply move a tarball to the correct name,
but the Mercury tarballs include "srcdist" in the name, and we don't want
that in the package name so we remove it.

    tar -zxf mercury-srcdist-14.01.1.tar.gz
    mv mercury-{srcdist-,}14.01.1
    tar -zcf mercury_14.01.1.orig.tar.gz

Or for ROTDs, note also -J for xz compression:

    tar -Jxf ~/hdd/mercury/dl1/rotd/mercury-srcdist-rotd-2020-05-31.tar.xz
    mv mercury-srcdist-rotd-2020-05-31/ mercury-rotd-20200531/
    tar -Jcf mercury-rotd_20200531.orig.tar.xz mercury-rotd-20200531/

Copy the debian directory from this repository into place and add a new
changelog entry.

    cp -r packaging/debian mercury-14.01.1/debian
    cd mercury-14.01.1
    dch -v 14.01.1-1

Check that patches apply properly, in a loop do:

    // Apply patch
    dquilt push -f

    // Fix the rejects
    ...

    // remove reject files.
    ...

    // Update patch
    dquilt refresh

Unapply all patches (optional):

    dquilt pop -a

Build the source package

    cd ..
    dpkg-source -b mercury-14.01.1

Use this to build a new source package and binary packages for amd64.

    ARCH=amd64 DIST=jessie sudo pbuilder build mercury_14.01.1-1.dsc

A new source package will be built in this step, even though we built one
above.  We do this because now the .changes file generated by
this step will refer to the source package's checksum.  It can be uploaded
in the same step.

Note: If you want to practice on some other software with a much shorter
build time, try the "hello" package.  You can get its source package with:

    apt-get source hello

Sign and upload these packages

    pushd /var/cache/pbuilder/result/
    debsign mercury_14.01.1-1_amd64.changes
    dput mercury mercury_14.01.1-1_amd64.changes
    popd

mercury is the name of the package repository to send the package to.
Note that the command doesn't say which distribution within the repository
to add it to.  It figures this out from the changelog file within the source
package that created these packages.

Use the newly generated source package, replacing the one generated in the
first step.  This is needed so that the .changes file for the i386 packages
contains the right hash for the source package.  The --binary-arch option
tells it not to regenerate the source or architecture independent packages.

    cp /var/cache/pbuilder/result/mercury_14.01.1-1.dsc \
        /var/cache/pbuilder/resxult/mercury_14.01.1-1.debian.tar.xz .
    ARCH=i386 DIST=jessie sudo pbuilder build --binary-arch mercury_14.01.1-1.dsc

Sign and upload these packages.

    pushd /var/cache/pbuilder/result/
    debsign mercury_14.01.1-1_i386.changes
    dput mercury mercury_14.01.1-1_i386.changes
    popd


### Bumping the version number

If you've made changes to the debian packages, either by updating the
upstream version or by adding patches via dquilt, then bump the version
number.  You'll need to change debian/changelog, but also debian/control and
the version patch (in dquilt).

Generally the sid release should get the "root" version number and other
releases, such as jessie, are backports of this version and hence have
"jessieN" at the end.


### Converting an rotd package to a release package:

The files in debian/ are setup to build an -rotd package.  To build a
non-rotd package follow the steps above but before building the source
package you also must:

 * Rename package names in debian/control
 * Rename the lastest package name in debian/changelog, the version may
   move backwards, dch will give a warning but the -b flag will ignore the
   warning.
 * Rename the various .install and other files:

    for name in mercury-rotd*; do
        mv $name $(echo $name | sed -e 's/-rotd//');
    done


### Adding a new version of a distro

These are breif notes, I'll fill them out next time I need to do this.  But
what I can recall right now.

 * Update ~/.pbuilderrc and the repository copy.
 * Make a new pbuilder image (or two for different architectures).
 * Make packages, remember to set the distro line in their changelog.
 * Add the packages to reprepro's configuration, update it in the repository
   also.
 * Run `reprepro createsymlinks`
 * Run `dput` and `repreprp processincoming` as normal


Update the repository
---------------------

To setup the repository the first time:
The repository is setup by creating a base directory and copying the files
The basedir is found by the REPREPRO\_BASE\_DIR variable in my .bashrc from
debian\_conf/reprepro/ into a conf/ subdirectory.  Also create an incoming
and temp directories.  When you first use the repository (after the first
processincoming) then you may also need to execute:

    reprepro export
    reprepro createsymlinks

dput will put package files into the incoming directory, mercury is the name
of the repository to use (from ~/.dput.cf):

    dput mercury new_package.changes

The command

    reprepro processincoming mercury

Will process these files adding them to the repository and rebuilding
indexes.  gpg will prompt you to resign the updated Release files.  Because
of the need for gpg signing this must be run locally, this is why we do not
run it on deimos and instead it runs on my workstation.  (Unless we had a
shared key and such).

I rsync the local copy onto the webserver:

    rsync -av --del --exclude db --exclude incoming --exclude temp \
        --exclude conf --exclude lists deb/ deimos:/srv/dl1/deb/

The excluded files simply don't need to be shared.  Likewise if I were
sharing this over HTTP (this is how dl2 is configured) I would need to
exclude these files in my apache configuration.

