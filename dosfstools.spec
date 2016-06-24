Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:	4.0
Release:	1
License:	GPLv3+
Group:		File tools
Url:		https://github.com/dosfstools/dosfstools
Source0:	https://github.com/dosfstools/dosfstools/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(libudev)

%description
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.

%prep
%setup -q

%build
%configure --enable-compat-symlinks
%make CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" CC=%{__cc}

%install
%makeinstall_std

%files
%doc %doc ChangeLog doc/README.*
/sbin/mkdosfs
/sbin/mkfs.msdos
/sbin/mkfs.vfat
/sbin/fatlabel
/sbin/fsck.fat
/sbin/mkfs.fat
/sbin/fsck.msdos
/sbin/fsck.vfat
/sbin/dosfsck
/sbin/dosfslabel
%{_mandir}/man8/*
%{_mandir}/de/man8/*
