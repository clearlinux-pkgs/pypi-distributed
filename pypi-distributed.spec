#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-distributed
Version  : 2022.5.2
Release  : 112
URL      : https://files.pythonhosted.org/packages/6d/73/9a508e0c0f44b38a3fcec8ed45809da32f84c1ec898c1d54a2b62d186a92/distributed-2022.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/73/9a508e0c0f44b38a3fcec8ed45809da32f84c1ec898c1d54a2b62d186a92/distributed-2022.5.2.tar.gz
Summary  : Distributed scheduler for Dask
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-distributed-bin = %{version}-%{release}
Requires: pypi-distributed-license = %{version}-%{release}
Requires: pypi-distributed-python = %{version}-%{release}
Requires: pypi-distributed-python3 = %{version}-%{release}
Requires: PyYAML
Requires: cloudpickle
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cloudpickle

%description
Distributed
===========
|Test Status| |Longitudinal Report (full)| |Longitudinal Report (short)| |Coverage| |Doc Status| |Discourse| |Version Status| |NumFOCUS|

%package bin
Summary: bin components for the pypi-distributed package.
Group: Binaries
Requires: pypi-distributed-license = %{version}-%{release}

%description bin
bin components for the pypi-distributed package.


%package license
Summary: license components for the pypi-distributed package.
Group: Default

%description license
license components for the pypi-distributed package.


%package python
Summary: python components for the pypi-distributed package.
Group: Default
Requires: pypi-distributed-python3 = %{version}-%{release}

%description python
python components for the pypi-distributed package.


%package python3
Summary: python3 components for the pypi-distributed package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pypi-distributed package.


%prep
%setup -q -n distributed-2022.5.2
cd %{_builddir}/distributed-2022.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653610173
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-distributed
cp %{_builddir}/distributed-2022.5.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-distributed/f016083f7994387778fdc4beb07d80240f8bbd54
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dask-scheduler
/usr/bin/dask-ssh
/usr/bin/dask-worker

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-distributed/f016083f7994387778fdc4beb07d80240f8bbd54

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
