%define name libindicate-qt
%define version 0.2.5
%define release %mkrel 1
%define summary Library for applications to raise flags on DBus
%define major 1
%define libname %mklibname indicate-qt %{major}
%define develname %mklibname indicate-qt -d

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/libindicate-qt/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
License:	LGPLv3
Group:		System/Libraries
URL:		https://launchpad.net/libindicate-qt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libindicate-devel
BuildRequires:	qt4-devel
BuildRequires:	cmake

%description
This project provides a set of Qt bindings for libindicate, the
indicator system developed by Canonical Desktop Experience team.

#-----------------------------------------------------------------------


%package -n	%{libname}
Summary:	Qt Bindings for libindicate
Group:		System/Libraries

%description -n	%{libname}
Qt Bindings for libindicate


%files -n %{libname}
%defattr(-,root,root)
%doc COPYING COPYING.LIB.LGPL.2.1 COPYING.LIB.LGPL.3 NEWS
%{_libdir}/libindicate-qt.so.%{major}*


#-----------------------------------------------------------------------

%package -n	%{develname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n	%{develname}
%defattr(-,root,root)
%{_libdir}/libindicate-qt.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/indicate-qt.pc

#-----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_qt4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
%__rm -rf %{buildroot}
