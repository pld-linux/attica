#
# Conditional build:
#
%define		qt_ver		4.6.1
%define		snap		svn1060455

Summary:	Attica Library - implementation of Open Collaboration Services API for Qt
Summary(pl.UTF-8):	Attica Library - implementacja API Serwisów Otwartej Współpracy dla Qt
Name:		attica
Version:	0.1.2
Release:	1
License:	GPL
Group:		X11/Libraries
# svn co svn://anonsvn.kde.org/home/kde/trunk/kdesupport/attica/
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
Source0:	ftp://ftp.kde.org/pub/kde/stable/attica/%{name}-%{version}.tar.bz2
# Source0-md5:	8b4207dbc0a826d422632bdb9c50d51a
URL:		http://kde.org
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtNetwork-devel >= %{qt_ver}
BuildRequires:	QtXml-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Attica is a Qt library that implements the Open Collaboration Services API.
It grants easy access to the services such as querying information about persons and contents.

%description -l pl.UTF-8
Attica jest biblioteką Qt, która implementuje API Serwisów Otwartej Współpracy.
Pozwala na łatwy dostęp do serwisów takich jak zapytania o informacje o osobach i treściach.

%package devel
Summary:        Header files for attica library
Summary(pl.UTF-8):      Pliki nagłówkowe biblioteki attica
Group:          Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for attica library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki attica.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

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
%attr(755,root,root) %ghost %{_libdir}/libattica.so.?
%attr(755,root,root) %{_libdir}/libattica.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libattica.so
%{_includedir}/attica
%{_libdir}/pkgconfig/libattica.pc
