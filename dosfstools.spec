Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:	4.1
Release:	3
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
%autosetup -p1

%build
%configure --sbindir=/sbin --enable-compat-symlinks
%make_build CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" CC=%{__cc}

%install
%make_install

%files
%doc %{_docdir}/%{name}
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
