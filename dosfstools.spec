%bcond_without	uclibc

Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:	3.0.26
Release:	1
License:	GPLv3+
Group:		File tools
Url:		http://www.daniel-baumann.ch/software/dosfstools/
Source0:	http://daniel-baumann.ch/files/software/dosfstools/%{name}-%{version}.tar.xz
%if %{with uclibc}
BuildRequires:	uClibc-devel >= 0.9.33.2-15
%endif

%description
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.

%if %{with uclibc}
%package -n	uclibc-%{name}
Summary:	Utilities to create and check MS-DOS FAT filesystems (uClibc build)
Group:		File tools

%description -n	uclibc-%{name}
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.
%endif

%prep
%setup -q
%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
%setup_compile_flags
%if %{with uclibc}
%make -C .uclibc CC=%{uclibc_cc} PREFIX=%{uclibc_root}%{_prefix} CFLAGS="%{uclibc_cflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
%endif

%make PREFIX=%{_prefix} CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" CC=%{__cc}

%install
%if %{with uclibc}
make DESTDIR="%{buildroot}" -C .uclibc install-bin SBINDIR=%{uclibc_root}/sbin
%endif

%makeinstall_std install-bin install-man PREFIX=%{_prefix} SBINDIR=/sbin

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

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/sbin/fatlabel
%{uclibc_root}/sbin/fsck.fat
%{uclibc_root}/sbin/mkfs.fat
%endif
