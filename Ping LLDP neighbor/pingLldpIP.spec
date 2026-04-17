Summary: Ping LLDP neighbor scripts for Arista EOS
Name: pingLldpIP
Version: 1.0.3
Release: 1
License: Apache-2.0
Group: EOS/Extension
BuildArch: noarch
Source0: pingLldpIP.tar.gz
Requires: Eos-release >= 2:4.33.0

%description
EOS scripts to ping LLDP neighbors via system name or management IP address.
Intended for use with EOS event-handler for automatic connectivity verification.

%prep
%setup -q -n pingLldpIP

%build

%install
install -d $RPM_BUILD_ROOT/usr/bin
install -m 755 ping_lldp_neighbor-sysName.py $RPM_BUILD_ROOT/usr/bin/
install -m 755 ping_lldp_neighbor-mgmtAddress.py $RPM_BUILD_ROOT/usr/bin/

%files
%defattr(-,root,root,-)
/usr/bin/ping_lldp_neighbor-sysName.py
/usr/bin/ping_lldp_neighbor-mgmtAddress.py

%changelog
* Wed Apr 16 2026 Westley Dion <westley.dion@arista.com> - 1.0.3-1
- Refactor scripts: remove unused import, f-strings, interface as parameter, add LLDP guard to sysName script

* Wed Apr 16 2026 Westley Dion <westley.dion@arista.com> - 1.0.2-3
- Auto-update README with current SWIX version on build

* Wed Apr 16 2026 Westley Dion <westley.dion@arista.com> - 1.0.2-2
- Remove latest.swix symlink from build output

* Wed Apr 16 2026 Westley Dion <westley.dion@arista.com> - 1.0.2-1
- Update CLAUDE.md and workflow documentation

* Wed Apr 16 2026 Westley Dion <westley.dion@arista.com> - 1.0.1-1
- Handle missing LLDP management address gracefully in ping_lldp_neighbor-mgmtAddress.py

* Wed Apr 16 2026 Westley Dion <westley.dion@arista.com> - 1.0.0-1
- Initial packaging
