
%define		module	linda

Summary:	Simple Python implementation of a linda system
Summary(pl.UTF-8):	Prosta implementacja systemu linda w Pythonie
Name:		python-%{module}
Version:	0.4
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://www-users.cs.york.ac.uk/~aw/pylinda/dist/%{module}-%{version}.tar.gz
# Source0-md5:	a6cda49e64e7d247e3f11939646e18d0
URL:		http://www-users.cs.york.ac.uk/~aw/pylinda
BuildRequires:	python-devel >= 1:2.3
Requires:	python >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linda is an widely studied distributed computing environment, centered
around the notion of a tuple space. A tuple space is a bag (also
called a multi-set) of tuples. A tuple is an ordered, typed chunk of
data. Tuple spaces exist independently of processes in the system, and
the data placed into a tuple space also exist independently. See
"Generative communication in Linda" (1985) and "Multiple tuple spaces
in Linda" both by David Gelernter for more information on Linda.

PyLinda is a simple implementation of a linda system, however it also
includes several of the more recently proposed extensions to Linda in
the form of multiple tuple spaces, garbage collection, sane
non-blocking primitives and bulk tuple operations.

This package contains pylinda libraries, which are necessary for
running pylinda servers and developing client programs.

%description -l pl.UTF-8
Linda jest poddawanym głębokiej analizie środowiskiem komputerowego
przetwarzania danych, skupiającym się na notacji przestrzeni krotek.
Przestrzeń krotek jest zbiorem (a właściwie - multizbiorem) krotek.
Krotka jest uporządkowanym i utypowionym zestawem danych. Przestrzenie
krotek istnieją w systemie niezależnie od procesów, a dane umieszczone
w przestrzeni krotek także są niezależne od procesów. Więcej
informacji można znaleźć w dziełach "Generative communication in
Linda" (1985) i "Multiple tuple spaces in Linda" autorstwa Davida
Gelerntera.

PyLinda jest prostą implementacją środowiska Linda. Pomimo swojej
prostoty zawiera jednak pewną liczbę najczęściej spotykanych
rozszerzeń Lindy, takich jak wielokrotne przestrzenie krotek,
odśmiecanie pamięci, rozsądnie zaprojektowane nieblokujące operacje
pierwotne oraz całą masę złożonych operacji na krotkach.

Ten pakiet zawiera biblioteki pakietu pylinda, niezbędne do
uruchomienia serwerów oraz rozwijania programów klienckich pylindy.

%package -n pylinda-server
Summary:	Server program for pylinda computing environment
Summary(pl.UTF-8):	Program serwera środowiska pylinda
Group:		Applications/Science
Requires:	%{name} = %{version}-%{release}

%description -n pylinda-server
This package contains server program for pylinda computing
environment.

%description -n pylinda-server -l pl.UTF-8
Program serwera środowiska pylinda.

%package doc
Summary:	Documentation for pylinda computing environment
Summary(pl.UTF-8):	Dokumentcja środowiska pylinda
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for pylinda computing
environment.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację środowiska pylinda.

%package examples
Summary:	Example programs for pylinda computing environment
Summary(pl.UTF-8):	Programy przykładowe do środowiska pylinda
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for pylinda computing
environment.

%description examples -l pl.UTF-8
Pakiet zawierający programy przykładowe do środowiska pylinda.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version},%{_bindir}}

%py_install \
	--install-lib=%{py_sitedir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a linda_server.py $RPM_BUILD_ROOT%{_bindir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/pylinda

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitedir}/linda

%files doc
%defattr(644,root,root,755)
%doc doc/html/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n pylinda-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/linda_server.py
