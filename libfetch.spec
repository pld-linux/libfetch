Summary:	libfetch provides a high-level interface for retreiving and uploading files using Uniform Resource Locators
Name:		libfetch
Version:	2.26
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://gogglesmm.googlecode.com/files/%{name}-%{version}-arch.tar.gz
# Source0-md5:	256b7875cddb348d35a6a1817819a76f
Patch0:		makefile-user-cflags.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a high-level interface for retreiving and uploading files
using Uniform Resource Locators.

%package devel
Summary:	Header files for libfetch library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libfetch library.

%prep
%setup -q
%patch0 -p1
sed -i "s@^Q.*=.*@Q =@g" Makefile.linux

%build
%{__make} -f Makefile.linux \
	USERCFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	LD="%{__ld}" \
	AR="%{__ar}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f Makefile.linux install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%{_mandir}/man3/fetch.*
%{_libdir}/lib*.a
%{_includedir}/fetch.h
