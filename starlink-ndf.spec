Summary:	NDF - NDF (N-dimensional Data Format) data structure routines
Summary(pl):	NDF - funkcje do struktur danych NDF (N-wymiarowego formatu danych)
Name:		starlink-ndf
Version:	1.5_8.218
Release:	2
License:	non-commercial use and distribution (see NDF_CONDITIONS)
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/ndf/ndf.tar.Z
# Source0-md5:	33103b5672be45d20a33727b055ef139
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_NDF.html
BuildRequires:	gcc-g77
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-ary-devel
BuildRequires:	starlink-ast-devel
BuildRequires:	starlink-par-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
The Extensible N-Dimensional Data Format (NDF) is a format for storing
bulk data in the form of N-dimensional arrays of numbers. It is
typically used for storing spectra, images and similar datasets with
higher dimensionality. The NDF format is based on the Hierarchical
Data System HDS and is extensible; not only does it provide a
comprehensive set of standard ancillary items to describe the data, it
can also be extended indefinitely to handle additional user-defined
information of any type.

%description -l pl
NDF (N-Dimensional Data Format - n-wymiarowy format danych) to format
s³u¿±cy do przechowywania danych w postaci n-wymiarowych tablic liczb.
Jest zwykle u¿ywany do przechowywania widm, obrazów i podobnych
zbiorów danych o wiêkszej liczbie wymiarów. Format NDF jest oparty na
hierarchicznym systemie danych HDS i jest rozszerzalny; nie tylko
dostarcza kompletnego zbioru standardowych elementów pomocniczych do
opisu danych, ale mo¿e byæ tak¿e nieskoñczenie rozszerzany do obs³ugi
dodatkowych zdefiniowanych przez u¿ytkownika informacji dowolnego
typu.

%package devel
Summary:	Header files for NDF libraries
Summary(pl):	Pliki nag³ówkowe bibliotek NDF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	starlink-ary-devel
Requires:	starlink-ast-devel
Requires:	starlink-par-devel

%description devel
Header files for NDF libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek NDF.

%package static
Summary:	Static Starlink NDF libraries
Summary(pl):	Statyczne biblioteki Starlink NDF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink NDF libraries.

%description static -l pl
Statyczne biblioteki Starlink NDF.

%prep
%setup -q -c

sed -i -e "s/ -O2\\? / %{rpmcflags} /;s/ ld -shared -soname / g77 -shared \\\$\\\$3 -Wl,-soname=/" mk
sed -i -e "s/\\('-L\\\$(STAR_\\)LIB) /\\1SHARE) /;s/-lerr /-lerr_standalone -last /;s/-lerr_adam /&-last -lpar_adam -ltask_adam /" makefile

%build
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir} \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NDF_CONDITIONS ndf.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/ssn*
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/ndf_dev
%attr(755,root,root) %{stardir}/bin/ndf_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
