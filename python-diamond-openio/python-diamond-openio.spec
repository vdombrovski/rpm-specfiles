Name:           python-diamond-openio
Version:        0.4
Release:        2%{?dist}
Summary:        Diamond collector for OpenIO SDS

License:        Apache v2
URL:            http://openio.io
Source0:        openiosds.py

#BuildRequires:  
Requires:       python-diamond,python-urllib3
Requires:       openio-sds-server

%description
Diamond collector for OpenIO SDS object storage solution.


%prep
#%setup -q


%build


%install
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datarootdir}/diamond/collectors/openiosds
%{__install} -m 644 %{SOURCE0} ${RPM_BUILD_ROOT}%{_datarootdir}/diamond/collectors/openiosds/openiosds.py


%files
%{_datarootdir}/diamond/collectors/openiosds


%changelog
* Mon Aug 29 2016 Romain Acciari <romain.acciari@openio.io> - 0.4-2%{?dist}
- Remove python-oiopy
* Thu May 26 2016 Romain Acciari <romain.acciari@openio.io> - 0.4-1%{?dist}
- New release updated by Vladimir Dombrovski
* Thu May 26 2016 Romain Acciari <romain.acciari@openio.io> - 0.3-1%{?dist}
- New release updated by Florent Vennetier
* Wed Mar 02 2016 Romain Acciari <romain.acciari@openio.io> - 0.2-1%{?dist}
- New release
* Fri Jan 29 2016 Romain Acciari <romain.acciari@openio.io> - 0.1-1%{?dist}
- Initial release
