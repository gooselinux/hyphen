Name:      hyphen
Summary:   A text hyphenation library
Version:   2.4
Release:   5.1%{?dist}
Source:    http://downloads.sourceforge.net/hunspell/hyphen-%{version}.tar.gz
Group:     System Environment/Libraries
URL:       http://hunspell.sf.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPLv2+ or MPLv1.1
BuildRequires: perl, patch

%description
Hyphen is a library for high quality hyphenation and justification.

%package devel
Requires: hyphen = %{version}-%{release}
Summary: Files for developing with hyphen
Group: Development/Libraries

%description devel
Includes and definitions for developing with hyphen

%package en
Requires: hyphen
Summary: English hyphenation rules
Group: Applications/Text
BuildArch: noarch

%description en
English hyphenation rules.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
en_US_aliases="en_AG en_AU en_BS en_BW en_BZ en_CA en_DK en_GB en_GH en_HK en_IE en_IN en_JM en_NA en_NZ en_PH en_SG en_TT en_ZA en_ZW"
for lang in $en_US_aliases; do
        ln -s hyph_en_US.dic hyph_$lang.dic
done
popd


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README README.hyphen README.nonstandard TODO
%{_libdir}/*.so.*
%dir %{_datadir}/hyphen

%files en
%defattr(-,root,root,-)
%{_datadir}/hyphen/hyph_en*.dic

%files devel
%defattr(-,root,root,-)
%{_includedir}/hyphen.h
%{_libdir}/*.so
%{_bindir}/substrings.pl

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Caolan McNamara <caolanm@redhat.com> - 2.4-4
- make hyphen-en a noarch subpackage

* Fri Jun 12 2009 Caolan McNamara <caolanm@redhat.com> - 2.4-3
- extend coverage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 02 2008 Caolan McNamara <caolanm@redhat.com> - 2.4-1
- latest version

* Tue Feb 19 2008 Caolan McNamara <caolanm@redhat.com> - 2.3.1-1
- latest version

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3-2
- Autorebuild for GCC 4.3

* Mon Nov 12 2007 Caolan McNamara <caolanm@redhat.com> - 2.3-1
- initial version
