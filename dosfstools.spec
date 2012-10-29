%bcond_without	uclibc

Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:        3.0.13
Release:        2
Source0:	http://www.daniel-baumann.ch/software/dosfstools/%{name}-%{version}.tar.bz2
License:	GPLv3+
URL:		http://www.daniel-baumann.ch/software/dosfstools/
Group:		File tools
%if %{with uclibc}
BuildRequires:	uClibc-devel >= 0.9.33.2-15
%endif

%description
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.


%package -n	uclibc-%{name}
Summary:	Utilities to create and check MS-DOS FAT filesystems (uClibc build)
Group:		File tools

%description -n	uclibc-%{name}
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.

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

%make PREFIX=%{_prefix} CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

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
/sbin/fsck.msdos
/sbin/fsck.vfat
/sbin/dosfsck
/sbin/dosfslabel
%{_mandir}/man8/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/sbin/mkdosfs
%{uclibc_root}/sbin/mkfs.msdos
%{uclibc_root}/sbin/mkfs.vfat
%{uclibc_root}/sbin/fsck.msdos
%{uclibc_root}/sbin/fsck.vfat
%{uclibc_root}/sbin/dosfsck
%{uclibc_root}/sbin/dosfslabel
%endif
