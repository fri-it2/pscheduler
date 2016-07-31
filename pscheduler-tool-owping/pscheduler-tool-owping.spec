#
# RPM Spec for pScheduler owping Tool
#

%define short	owping
Name:		pscheduler-tool-%{short}
Version:	0.0
Release:	1%{?dist}

Summary:	owping tool class for pScheduler
BuildArch:	noarch
License:	Apache 2.0
Group:		Unspecified

Source0:	%{short}-%{version}.tar.gz

Provides:	%{name} = %{version}-%{release}

Requires:	pscheduler-core
Requires:	python-pscheduler
Requires:	pscheduler-test-latency
Requires:	owamp-client
Requires:	owamp-server

BuildRequires:	pscheduler-rpm


%description
owping tool class for pScheduler


%prep
%if 0%{?el6}%{?el7} == 0
echo "This package cannot be built on %{dist}."
false
%endif

%setup -q -n %{short}-%{version}


%define dest %{_pscheduler_tool_libexec}/%{short}

%build
make \
     DESTDIR=$RPM_BUILD_ROOT/%{dest} \
     DOCDIR=$RPM_BUILD_ROOT/%{_pscheduler_tool_doc} \
     install

%post
if [ "$1" -eq 1 ]
then
  # TODO: Add firewall rules if necessary
  true
fi

%postun
if [ "$1" -eq 0 ]
then
  # TODO: Add firewall rules if necessary
  true
fi


%files
%defattr(-,root,root,-)
%{dest}
%{_pscheduler_tool_doc}/*
