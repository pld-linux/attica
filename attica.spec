#
# Conditional build:
#
%define		qt_ver		4.8.0

Summary:	Attica Library - implementation of Open Collaboration Services API for Qt
Summary(pl.UTF-8):	Attica Library - implementacja API Serwisów Otwartej Współpracy dla Qt
Name:		attica
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Libraries
# svn co svn://anonsvn.kde.org/home/kde/trunk/kdesupport/attica/
Source0:	ftp://ftp.kde.org/pub/kde/stable/attica/%{name}-%{version}.tar.bz2
# Source0-md5:	2de3a49d79884ed3ce9df491bf35a86b
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtNetwork-devel >= %{qt_ver}
BuildRequires:	QtXml-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.8.0
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Attica is a Qt library that implements the Open Collaboration Services
API. It grants easy access to the services such as querying
information about persons and contents.

%description -l pl.UTF-8
Attica jest biblioteką Qt, która implementuje API Serwisów Otwartej
Współpracy. Pozwala na łatwy dostęp do serwisów takich jak zapytania o
informacje o osobach i treściach.

%package devel
Summary:	Header files for attica library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki attica
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for attica library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki attica.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/ldconfig
%postun	-p	/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libattica.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libattica.so.0.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libattica.so
%{_includedir}/attica
%{_pkgconfigdir}/libattica.pc
