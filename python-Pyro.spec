#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	Pyro
Summary:	PYthon Remote Objects module
Summary(pl.UTF-8):	PYthon Remote Objects
Name:		python-%{module}
Version:	3.16
Release:	2
License:	MIT
Group:		Development/Languages/Python

# http://pypi.python.org/packages/source/P/Pyro/Pyro-3.16.tar.gz#md5=59d4d3f4a8786776c9d7f9051b8f1a69
Source0:	http://pypi.python.org/packages/source/P/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	59d4d3f4a8786776c9d7f9051b8f1a69
URL:		http://www.xs4all.nl/~irmen/pyro3/
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyro is short for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use.

%description -l pl.UTF-8
Pyro jest skrótem od Pythonowe zdalne objetky. Jest zawasnowanym i
poteżnym systemem zarządania zdalnymi objektami napisanym całkowice w
Pythonie. Jest zaprojektowany aby być bardzo łatwym w użyciu.

%prep
%setup -q -n %{module}-%{version}

# fix #!%{_bindir}/env python -> #!%{_bindir}/python:
# %{__sed} -i -e '1s,^#!.*python,#!%{__python},' %{name}.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/pyro-es
%attr(755,root,root) %{_bindir}/pyro-esd
%attr(755,root,root) %{_bindir}/pyro-genguid
%attr(755,root,root) %{_bindir}/pyro-ns
%attr(755,root,root) %{_bindir}/pyro-nsc
%attr(755,root,root) %{_bindir}/pyro-nsd
%attr(755,root,root) %{_bindir}/pyro-wxnsc
%attr(755,root,root) %{_bindir}/pyro-xnsc

%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/ext
%{py_sitescriptdir}/%{module}/ext/*.py[co]
%dir %{py_sitescriptdir}/%{module}/EventService
%{py_sitescriptdir}/%{module}/EventService/*.py[co]
%dir %{py_sitescriptdir}/%{module}/test
%{py_sitescriptdir}/%{module}/test/*.py[co]


%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
