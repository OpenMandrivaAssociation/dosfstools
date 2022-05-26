Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:	4.2
Release:	5
License:	GPLv3+
Group:		File tools
Url:		https://github.com/dosfstools/dosfstools
Source0:	http://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/dosfstools/dosfstools/issues/111
BuildRequires:	pkgconfig(libudev)
BuildRequires:	gettext-devel

%description
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.

%prep
%autosetup -p1

%build
%configure \
	--enable-compat-symlinks

%make_build CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -Oz" CC=%{__cc}

%install
%make_install

%files
%doc %{_docdir}/%{name}
%{_sbindir}/*
%doc %{_mandir}/man8/*
