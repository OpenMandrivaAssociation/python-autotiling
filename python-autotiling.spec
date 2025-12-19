Name:		python-autotiling
Version:	1.9.3
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/a/autotiling/autotiling-%{version}.tar.gz
Summary:	Automatically switch the horizontal/vertical window split orientation in sway and i3
URL:		https://pypi.org/project/autotiling/
License:	GPL-3.0-or-later
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Automatically switch the horizontal/vertical window split orientation in sway and i3

%files
%{_bindir}/autotiling
%{py_sitedir}/autotiling
%{py_sitedir}/autotiling-*.*-info
