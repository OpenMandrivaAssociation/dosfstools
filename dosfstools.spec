Summary:	Utilities to create and check MS-DOS FAT filesystems
Name:		dosfstools
Version:        2.11
Release:        %mkrel 9
Source0:	ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/dosfstools/%{name}-%{version}.src.tar.bz2
Patch0:		dosfstools-2.7-argfix.patch
Patch1:		dosfstools-2.11-assumeKernel26.patch
Patch3:		dosfstools-2.11-fortify.patch
Patch4:		dosfstools-2.11-label.patch
License:	GPL
URL:		ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/dosfstools
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
%patch0 -p1 -b .argfix
%patch1 -p1 -b .assumeKernel26
%patch3 -p1 -b .fortify
%patch4 -p1 -b .label

%build
%make PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
cp dosfsck/README README.fsck
cp mkdosfs/README README.mkdosfs
%makeinstall PREFIX=$RPM_BUILD_ROOT MANDIR=$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES TODO README.fsck README.mkdosfs
/sbin/mkdosfs
/sbin/mkfs.msdos
/sbin/mkfs.vfat
/sbin/fsck.msdos
/sbin/fsck.vfat
/sbin/dosfsck
/sbin/dosfslabel
%{_mandir}/man8/*
