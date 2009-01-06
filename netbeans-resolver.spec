%define nb_              netbeans
%define nb_org           %{nb_}.org
%define nb_ver           6.5
%define patched_resolver_ver 1.1
%define patched_resolver xml-commons-resolver-%{patched_resolver_ver}

Name:           %{nb_}-resolver
Version:        %{nb_ver}
Release:        %mkrel 1
Summary:        Resolver subproject of xml-commons patched for NetBeans

Group:          Development/Java
License:        ASL 2.0
URL:            http://xml.apache.org/commons/

Source0: http://mirrors.dedipower.com/ftp.apache.org/xml/commons/%{patched_resolver}.zip
# see http://hg.%{nb_org}/main/file/721f72486327/o.apache.xml.resolver/external/readme.txt
Patch0: %{name}-%{version}.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires:  jpackage-utils
BuildRequires:  java >= 1.6.0
BuildRequires:  ant

Requires:       jpackage-utils
Requires:       java >= 1.6

%description
Resolver subproject of xml-commons, version %{patched_resolver_ver} with a patch for NetBeans.

%prep
%setup -q -n %{patched_resolver}
# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf docs

%patch0 -p1 -b .sav

%build
ant -f resolver.xml jar

%install
rm -rf $RPM_BUILD_ROOT

# Jars
%define orig_jar build/resolver.jar
%define i_jardir %{_javadir}
%define br_jardir %{buildroot}%{i_jardir}
%{__mkdir_p} %{br_jardir}
%{__cp} -p %{orig_jar} %{br_jardir}/%{name}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_javadir}/*

