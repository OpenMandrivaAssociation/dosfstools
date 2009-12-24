Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:        3.0.7
Release:        %mkrel 1
Source0:	http://www.daniel-baumann.ch/software/dosfstools/%{name}-%{version}.tar.bz2
License:	GPLv3+
URL:		http://www.daniel-baumann.ch/software/dosfstools/
Group:		File tools
Obsoletes:	mkdosfs-ygg
Provides:	mkdosfs-ygg = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.

%prep

%setup -q

%build
%make PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
%make DESTDIR=%{buildroot} install-bin install-man PREFIX=%{_prefix} SBINDIR=/sbin

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %doc ChangeLog doc/README.*
/sbin/mkdosfs
/sbin/mkfs.msdos
/sbin/mkfs.vfat
/sbin/fsck.msdos
/sbin/fsck.vfat
/sbin/dosfsck
/sbin/dosfslabel
%{_mandir}/man8/*
