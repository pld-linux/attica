#
# Conditional build:
#
%define		qt_ver		4.6.0
%define		snap		svn1058114

Summary:	Attica Library
Summary(pl.UTF-8):	Attica Library
Name:		attica
Version:	0.1
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Libraries
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	23b488f0dc23ca5d625105d5d227b42f
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
Attica library.

%description -l pl.UTF-8
Attica library.

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
%setup -q -n %{name}-%{version}-%{snap}

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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libattica.so.0
%attr(755,root,root) %{_libdir}/libattica.so.0.1.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libattica.so
%{_includedir}/attica
%{_libdir}/pkgconfig/libattica.pc
