%define patched_resolver_ver 1.2
%define patched_resolver xml-commons-resolver-%{patched_resolver_ver}

Name:    netbeans-resolver
Version: 6.7.1
Release: %mkrel 1
Summary: Resolver subproject of xml-commons patched for NetBeans

Group:   Development/Java
License: ASL 1.1
URL:     http://xml.apache.org/commons/

Source0: http://www.apache.org/dist/xml/commons/%{patched_resolver}.zip

# see http://hg.netbeans._org/main/file/721f72486327/o.apache.xml.resolver/external/readme.txt
Patch0: %{name}-%{version}-nb.patch
Patch1: %{name}-%{version}-resolver.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: java-devel >= 1.6.0
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: dos2unix
BuildRequires: java-rpmbuild >= 0:1.5.32

Requires: jpackage-utils
Requires: java >= 1.6.0

%description
Resolver subproject of xml-commons, version %{patched_resolver_ver} with 
a patch for NetBeans.

%prep
%setup -q -n %{patched_resolver}
# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
%{__rm} -rf docs

%patch0 -p1 -b .sav
%patch1 -p1 -b .sav

dos2unix KEYS >x && mv x KEYS
dos2unix LICENSE.resolver.txt >x && mv x LICENSE.resolver.txt

%build
%{ant} -f resolver.xml jar

%install
%{__rm} -rf %{buildroot}

# JARs
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/resolver.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_javadir}/*
%doc LICENSE.resolver.txt KEYS

