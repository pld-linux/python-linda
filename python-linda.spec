
%include	/usr/lib/rpm/macros.python
%define		module linda

Summary:	Simple Python implementation of a linda system
Summary(pl):	Prosta implementacja systemu linda w Pythonie
Name:		python-%{module}
Version:	0.2
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://www-users.cs.york.ac.uk/~aw/pylinda/%{module}-%{version}.tar.gz
# Source0-md5:	396d2908f530293d8390638639eb3198
Patch0:		pylinda-server-first-line-path.patch
URL:		http://www-users.cs.york.ac.uk/~aw/pylinda
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
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

This package contains pylinda libraries, which are necessary for running
pylinda servers and developing client programs.

%description -l pl
Lidna jest poddawanym g³êbokiej analizie ¶rodowiskiem komputerowego
przetwarzania danych, skupiaj±cym siê na notacji przestrzeni krotek.
Przestreñ krotek jest zbiorem (a w³a¶ciwie - multizbiorem) krotek.
Krotka jest uporz±dkowanym i utypowionym zestawem danych. Przestrzenie
krotek istniej± w systemie niezale¿nie od procesów, a dane umieszczone
w przestrzeni krotek tak¿e s± niezale¿ne od procesów. Wiêcej
informacji mo¿na znale¼æ w dzie³ach "Generative communication in
Linda" (1985) i "Multiple tuple spaces in Linda" autorstwa Daviad
Gelerntera.

PyLinda jest prost± implementacj± ¶rodowiska Linda. Pomimo swojej
prostoty zawiera jednak pewn± liczbê najczê¶cie spotykanych rozszerzeñ
Lindy, takich jak wielokrotne przestrzenie krotek, od¶miecanie
pamiêci, rozs±dnie zaprojektowane nieblokuj±ce operacje pierwotne oraz
ca³± masê z³o¿onych operacji na krotkach.

Ten pakiet zawiera biblioteki pakietu pylinda, niezbêdne do
uruchomienia serwerów oraz rozwijania programów klienckich pylindy.

%package -n pylinda-server
Summary:	Server program for pylinda computing environment
Summary(pl):	Program serwera ¶rodowika pylinda
Group:		Applications/Science
Requires:	%{name} = %{version}-%{release}

%description -n pylinda-server
This package contains server program for pylinda computing
environment.

%description -n pylinda-server -l pl
Program serwera ¶rodowiska pylinda.

%package doc
Summary:	Documentation for pylinda computing environment
Summary(pl):	Dokumentcja ¶rodowiska pylinda
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for pylinda computing
environment.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê ¶rodowiska pylinda.

%package examples
Summary:	Example programs for pylinda computing environment
Summary(pl):	Programy przyk³adowe do ¶rodowiska pylinda
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for pylinda computing
environment.

%description examples -l pl
Pakiet zawieraj±cy programy przyk³adowe do ¶rodowiska pylinda.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version},%{_bindir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a linda_server.py $RPM_BUILD_ROOT%{_bindir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/pylinda

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/linda

%files doc
%defattr(644,root,root,755)
%doc doc/html/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n pylinda-server
%defattr(755,root,root,755)
%{_bindir}/linda_server.py
