Name:		python-autotiling
Version:	1.9.3
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/a/autotiling/autotiling-%{version}.tar.gz
Summary:	Automatically switch the horizontal/vertical window split orientation in sway and i3
URL:		https://pypi.org/project/autotiling/
License:	GPL-3.0-or-later
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Automatically switch the horizontal/vertical window split orientation in sway and i3

%files
%{_bindir}/autotiling
%{py_sitedir}/autotiling
%{py_sitedir}/autotiling-*.*-info
