%define _disable_ld_no_undefined 1

%if %mandriva_branch == Cooker
# Cooker
%define release  4
%else
# Old distros
%define subrel 2
%define release  1
%endif

%define saversion 4.2.1

%define tlsdir		%{_sysconfdir}/pki/tls/%{name}

%define build_mysql	1
%define build_pgsql	0
%define build_monitor	1
%define build_exiscan	1
%define build_spf2	0
%define build_srs_alt	0
%define build_sqlite3	1
%define build_ldap	1
%define build_sasl2	1
%define build_logrotate	1

%define build_certs	1
%define altpriority 	40

# commandline overrides:
# rpm -ba|--rebuild --define 'with_xxx'
%{?_with_mysql: %{expand: %%global build_mysql 1}}
%{?_without_mysql: %{expand: %%global build_mysql 0}}
%{?_with_pgsql: %{expand: %%global build_pgsql 1}}
%{?_without_pgsql: %{expand: %%global build_pgsql 0}}
%{?_with_monitor: %{expand: %%global build_monitor 1}}
%{?_without_monitor: %{expand: %%global build_monitor 0}}
%{?_with_exiscan: %{expand: %%global build_exiscan 1}}
%{?_without_exiscan: %{expand: %%global build_exiscan 0}}
%{?_with_spf2: %{expand: %%global build_spf2 1}}
%{?_without_spf2: %{expand: %%global build_spf2 0}}
%{?_with_srs_alt: %{expand: %%global build_srs_alt 1}}
%{?_without_srs_alt: %{expand: %%global build_srs_alt 0}}
%{?_with_sqlite3: %{expand: %%global build_sqlite3 1}}
%{?_without_sqlite3: %{expand: %%global build_sqlite3 0}}
%{?_with_ldap: %{expand: %%global build_ldap 1}}
%{?_without_ldap: %{expand: %%global build_ldap 0}}
%{?_with_sasl2: %{expand: %%global build_sasl2 1}}
%{?_without_sasl2: %{expand: %%global build_sasl2 0}}
%{?_with_logrotate: %{expand: %%global build_logrotate 1}}
%{?_without_logrotate: %{expand: %%global build_logrotate 0}}

%define alternatives_install_cmd update-alternatives --install %{_sbindir}/sendmail mta %{_sbindir}/sendmail.exim %{altpriority} --slave %{_prefix}/lib/sendmail mta-in_libdir %{_sbindir}/sendmail.exim --slave %{_bindir}/mailq mta-mailq %{_bindir}/mailq.exim --slave %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.exim --slave %{_bindir}/rmail mta-rmail %{_bindir}/rmail.exim --slave %{_sysconfdir}/aliases mta-etc_aliases %{_sysconfdir}/exim/aliases

Summary:		The exim mail transfer agent
Name:			exim
Version:		4.76
Release:		%{release}
License:		GPLv2+
Group:			System/Servers
URL:			http://www.exim.org
Source0:		ftp://ftp.exim.org/pub/exim/exim4/%{name}-%{version}.tar.gz
Source1:		ftp://ftp.exim.org/pub/exim/exim4/%{name}-%{version}.tar.gz.asc
# http://www.exim.org/pub/exim/exim4/config.samples.tar.bz2
Source2:		exim-4.43-config.samples.tar.bz2
Source3:		ftp://ftp.exim.org/pub/exim/exim4/exim-html-%{version}.tar.gz
Source4:		ftp://ftp.exim.org/pub/exim/exim4/exim-html-%{version}.tar.gz.asc
# http://sa-exim.sourceforge.net/
Source5:		http://prdownloads.sourceforge.net/sa-exim/sa-exim-%{saversion}.tar.gz
#Source6:		eximconfig.bz2
Source7:		exim-README.urpmi
Source20:		exim.aliases
Source21:		exim.init
Source22:		exim.sysconfig
Source23:		exim.logrotate
Source24:		exim.pam
Source25:		exim_monitor-16x16.png
Source26:		exim_monitor-32x32.png
Source27:		exim_monitor-48x48.png
Source28:		exim-4.63-auth_pop3_imap.embedded_perl
Source29:		exim-4.63-sasl2_smtpd.conf
Source30:		exim-4.63-logrotate_eximstats
Source31:		exim-4.63-cron_exicyclog_eximstats
Source32:		exim-4.63-sysconfig
Patch0:			exim-4.69-mdv-config.patch
Patch3:			exim-4.22-install.patch
Patch5:			exim-4.43-dontoverridecflags.diff
Patch7:			exim-4.69-configure.default.patch
Patch8:			sa-exim-4.2.1-fix-str-fmt.patch
Requires(pre):		rpm-helper
Requires:		perl(Net::IMAP::Simple)
Requires:		openssl
Requires:		apache-mod_socache_shmcb
Provides:		mail-server
Provides:		sendmail-command
Conflicts:		postfix
Conflicts:		sendmail
Conflicts:		qmail
BuildRequires:		tcp_wrappers-devel
BuildRequires:		pam-devel
BuildRequires:		openssl-devel
BuildRequires:		lynx
BuildRequires:		links
BuildRequires:		pcre-devel
BuildRequires:		perl-devel
BuildRequires:		db-devel >= 4.2
%if %{build_monitor}
BuildRequires:		pkgconfig(x11)
BuildRequires:		pkgconfig(xaw7)
BuildRequires:		pkgconfig(xext)
BuildRequires:		pkgconfig(xmu)
BuildRequires:		pkgconfig(xt)
%endif
%if %{build_mysql}
BuildRequires:		mysql-devel
%endif
%if %{build_pgsql}
BuildRequires:		postgresql-devel
%endif
%if %{build_spf2}
BuildRequires:		libspf2-devel
%endif
%if %{build_srs_alt}
BuildRequires:		srs_alt-devel
%endif
%if %{build_sqlite3}
BuildRequires:		sqlite3-devel >= 3.2.2
%endif
%if %{build_ldap}
BuildRequires:		openldap-devel >= 2.0.11
Requires:		openldap >= 2.0.11
%endif
%if %{build_sasl2}
BuildRequires:		sasl-devel = 2.1.25 >= 2.0
%endif

%description
Exim is a mail transport agent (MTA) developed at the University of
Cambridge for use on Unix systems connected to the Internet. In style
it is similar to Smail 3, but its facilities are more extensive, and
in particular it has options for verifying incoming sender and
recipient addresses, for refusing mail from specified hosts, networks,
or senders, and for controlling mail relaying. Exim is in production
use at quite a few sites, some of which move hundreds of thousands of
messages per day.

You can build %{name} with some conditional build swithes;

(ie. use with rpm --rebuild):
--with[out] mysql	MySQL lookup support (enabled)
--with[out] pgsql	PostgreSQL lookup support (disabled)
--with[out] monitor	The Exim Monitor (enabled)
--with[out] exiscan	SpamAssassin support (enabled)
--with[out] srs_alt	Experimental SRS support (disabled)
--with[out] spf2	Experimental SPF2 support (disabled)
--with[out] sqlite3	SQLite3 lookup support (enabled)
--with[out] ldap	LDAP lookup support (enabled)
--with[out] sals2	SASL2 auth support (disabled)
--with[out] logrotate	Logrotate  (enabled)

%if %{build_monitor}
%package		monitor
Summary:		X11 monitor application for exim
Group:			Monitoring
Requires:		%{name} >= %{version}-%{release}

%description		monitor
The Exim Monitor is an optional supplement to the Exim package. It
displays information about Exim's processing in an X window, and an
administrator can perform a number of control actions from the window
interface.
%endif

%package		plugins-SpamAssassin
Summary:		Exim SpamAssassin at SMTP time plugin
Group:			System/Servers
Requires:		%{name} >= %{version}-%{release}

%description 		plugins-SpamAssassin
Allows running SpamAssassin on incoming mail and rejection
at SMTP time as well as other nasty things like teergrubbing.

%package		doc
Summary:		Exim documentation
Group:			System/Servers

%description		doc
This package includes the Exim FAQ and Exim manual in HTML.


%prep

%setup -q -n %{name}-%{version} -a2 -a3 -a5

cp %{SOURCE7} README.urpmi

# fix strange attribs
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

# cvs cleanup
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
	if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch0 -p1 -b .config
%patch3 -p1 -b .install
%patch5 -p0 -b .dontoverridecflags
%patch7 -p0 -b .configure_default

# apply the SA-exim dlopen patch
cat sa-exim-%{saversion}/localscan_dlopen_exim_4.20_or_better.patch | patch -p1

pushd sa-exim-%{saversion}
%patch8 -p0 -b .str
popd

# pre-build setup
cp src/EDITME Local/Makefile
%if %{build_monitor}
cp exim_monitor/EDITME Local/eximon.conf
%endif

# Added BIN_DIRECTORY:
perl -pi -e 's|^BIN_DIRECTORY=/usr/exim/bin|BIN_DIRECTORY=%{_bindir}|g' Local/Makefile

# modify Local/Makefile for our builds
%if !%{build_mysql}
  perl -pi -e 's|^LOOKUP_MYSQL=yes|#LOOKUP_MYSQL=yes|g' Local/Makefile
  perl -pi -e 's|-lmysqlclient||g' Local/Makefile
  perl -pi -e 's|-I%{_includedir}/mysql||g' Local/Makefile
%endif
%if !%{build_pgsql}
  perl -pi -e 's|^LOOKUP_PGSQL=yes|#LOOKUP_PGSQL=yes|g' Local/Makefile
  perl -pi -e 's|-lpq||g' Local/Makefile
  perl -pi -e 's|-I%{_includedir}/pgsql||g' Local/Makefile
%endif
%if !%{build_monitor}
  perl -pi -e 's|^EXIM_MONITOR=|#EXIM_MONITOR=|g' Local/Makefile
%endif

%ifarch amd64 x86_64
  perl -pi -e 's|X11\)/lib|X11\)/lib64|g' OS/Makefile-Linux
%endif

%if %{build_exiscan}
  perl -pi -e 's|^# WITH_CONTENT_SCAN=.*|WITH_CONTENT_SCAN=yes|g' Local/Makefile
  perl -pi -e 's|^# WITH_OLD_DEMIME=.*|WITH_OLD_DEMIME=yes|g' Local/Makefile
%endif

# the spf stuff won't build
%if %{build_spf2}
  perl -pi -e 's|^# EXPERIMENTAL_SPF=.*|EXPERIMENTAL_SPF=yes\nCFLAGS += -DHAVE_NS_TYPE\nLDFLAGS += -L%{_libdir} -lspf2|g' Local/Makefile
%endif

%if %{build_srs_alt}
  perl -pi -e 's|^# EXPERIMENTAL_SRS=.*|EXPERIMENTAL_SRS=yes\nLDFLAGS += -L%{_libdir} -lsrs_alt|g' Local/Makefile
%endif

%if %{build_ldap}
perl -pi -e 's|^# LOOKUP_LDAP=yes|LOOKUP_LDAP=yes|g' Local/Makefile
perl -pi -e 's|^# LDAP_LIB_TYPE=OPENLDAP2|LDAP_LIB_TYPE=OPENLDAP2|' Local/Makefile
perl -pi -e 's|^LOOKUP_INCLUDE=|LOOKUP_INCLUDE=-I%{_includedir}/ldap |' Local/Makefile
perl -pi -e 's|^LOOKUP_LIBS=|LOOKUP_LIBS=-L%{_libdir} -llber -lldap |' Local/Makefile
%endif

%if %{build_sqlite3}
perl -pi -e 's|^# LOOKUP_SQLITE=yes|LOOKUP_SQLITE=yes|g' Local/Makefile
perl -pi -e 's|^LOOKUP_INCLUDE=|LOOKUP_INCLUDE=-I/usr/include |g' Local/Makefile
perl -pi -e 's|^LOOKUP_LIBS=|LOOKUP_LIBS=-L%{_libdir} -lsqlite3 |g' Local/Makefile
%endif

%if %{build_sasl2}
  perl -pi -e 's|^# CYRUS_SASLAUTHD_SOCKET=/var/run/saslauthd/mux|CYRUS_SASLAUTHD_SOCKET=/var/lib/sasl2/mux|' Local/Makefile
  perl -pi -e 's|^# AUTH_LIBS=-lsasl2|AUTH_LIBS=-L%{_libdir} -lsasl2|' Local/Makefile
%endif

# Remove references to Interbase (-lgds):
perl -pi -e 's|-lgds||g' Local/Makefile

# support the SMTP STARTTLS:
perl -pi -e 's|-L/usr/openssl/lib -lssl -lcrypto|-L%{_libdir} -lssl -lcrypto|' Local/Makefile

# enable all of them
perl -pi -e "s|^# AUTH_CYRUS_SASL=yes|AUTH_CYRUS_SASL=yes|g" Local/Makefile
perl -pi -e "s|^# AUTH_DOVECOT=yes|AUTH_DOVECOT=yes|g" Local/Makefile

# fix stray borked libdir
perl -pi -e "s|/usr/lib\b|%{_libdir}|g" Local/Makefile

# unpack some other stuff
mkdir -p mandriva
#cp %{SOURCE6} mandriva/eximconfig
cp %{SOURCE20} mandriva/exim.aliases
cp %{SOURCE21} mandriva/exim.init
cp %{SOURCE22} mandriva/exim.sysconfig
cp %{SOURCE23} mandriva/exim.logrotate
cp %{SOURCE24} mandriva/exim.pam

# copy icons
cp %{SOURCE25} exim_monitor-16x16.png
cp %{SOURCE26} exim_monitor-32x32.png
cp %{SOURCE27} exim_monitor-48x48.png

mkdir -p exim_tmp
# embedded perl
cp -f %{SOURCE28} exim_tmp/exim_auth_pop3_imap.embedded_perl
cp -f %{SOURCE29} exim_tmp/exim_sasl2_smtpd.conf
cp -f %{SOURCE30} exim_tmp/exim_logrotate_eximstats
cp -f %{SOURCE31} exim_tmp/exim_cron_exicyclog_eximstats
cp -f %{SOURCE32} exim_tmp/exim_sysconfig

# prepare docs
mkdir -p doc/html
mv exim-html-%{version}/doc/html/spec_html/* doc/html/

%build
%serverbuild

make CC="gcc %ldflags" \
    CFLAGS="%optflags -fPIC" \
    RPM_OPT_FLAGS="%optflags -fPIC"

# build SA-exim
pushd sa-exim-%{saversion}
perl -pi -e 's|\@lynx|HOME=/ /usr/bin/lynx|g;' Makefile
perl -pi -e 's|/usr/lib/exim4/local_scan|%{_libdir}/exim|g' INSTALL
make clean

make \
    SACONF=%{_sysconfdir}/exim/sa-exim.conf \
    CFLAGS="%optflags" \
    LDFLAGS="-shared -fPIC %ldflags"
popd

%install
rm -rf %{buildroot}

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

# make some directories
install -d %{buildroot}%{_sysconfdir}/{pam.d,exim,sysconfig,cron.weekly}
install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}/exim
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}/var/spool/exim/{db,input,msglog}
install -d %{buildroot}/var/run/exim
install -d %{buildroot}/var/log/exim
install -d %{buildroot}/%{_menudir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{tlsdir}/{certs,private,dhparam}

%makeinstall_std

pushd build-`scripts/os-type`-`scripts/arch-type`
    for i in convert4r3 convert4r4 exicyclog exigrep \
    exim exim_checkaccess exim_dbmbuild exim_dumpdb exim_fixdb \
    exim_lock eximstats exim_tidydb exinext exipick exiqgrep \
    exiqsumm exiwhat; do
	install -m0755 $i %{buildroot}%{_bindir}/
    done

%if %{build_monitor}
    install -m0755 eximon %{buildroot}%{_bindir}/
    install -m0755 eximon.bin %{buildroot}%{_bindir}/
%endif

popd

# make some softlinks
ln -snf ../bin/exim %{buildroot}%{_prefix}/lib/sendmail.exim
ln -snf ../bin/exim %{buildroot}%{_sbindir}/exim
ln -snf exim %{buildroot}%{_sbindir}/sendmail.exim
ln -snf exim %{buildroot}%{_bindir}/mailq.exim
ln -snf exim %{buildroot}%{_bindir}/newaliases.exim
ln -snf exim %{buildroot}%{_bindir}/rmail.exim
ln -snf exim %{buildroot}%{_bindir}/rsmtp
ln -snf exim %{buildroot}%{_bindir}/rsmtp.exim
ln -snf exim %{buildroot}%{_bindir}/runq
ln -snf exim %{buildroot}%{_bindir}/runq.exim

# install SA-exim
install -m0644 sa-exim-%{saversion}/*.so %{buildroot}%{_libdir}/exim/
install -m0644 sa-exim-%{saversion}/*.conf %{buildroot}%{_sysconfdir}/exim/

pushd %{buildroot}%{_libdir}/exim
    ln -s sa-exim*.so sa-exim.so
popd

# install some other stuff
pushd mandriva
    install -m0644 exim.aliases %{buildroot}%{_sysconfdir}/exim/aliases
    install -m0755 exim.init %{buildroot}%{_initrddir}/exim
    install -m0644 exim.pam %{buildroot}%{_sysconfdir}/pam.d/smtp
popd

install -m0644 exim_tmp/exim_auth_pop3_imap.embedded_perl %{buildroot}%{_sysconfdir}/exim/exim_perl.pl
%if %{build_sasl2}
install -d %{buildroot}%{_sysconfdir}/sasl2
install -m0644 exim_tmp/exim_sasl2_smtpd.conf %{buildroot}%{_sysconfdir}/sasl2/smtpd.conf
%endif
%if %{build_logrotate}
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m0644 exim_tmp/exim_logrotate_eximstats %{buildroot}%{_sysconfdir}/logrotate.d/exim
%else
install -m0755 exim_tmp/exim_cron_exicyclog_eximstats %{buildroot}%{_sysconfdir}/cron.weekly/exim
%endif
install -m0644 exim_tmp/exim_sysconfig %{buildroot}%{_sysconfdir}/sysconfig/exim

install -m644 doc/exim.8 %{buildroot}%{_mandir}/man8/exim.8

# Alias /eximstats /var/www/eximstats for Apache
install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
cat > %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/eximstats.conf << EOF
Alias /eximstats /var/www/eximstats
<Directory /var/www/eximstats>
	Require all granted
	Options +Indexes
</Directory>
EOF

pod2man --center=EXIM --section=8 \
    %{buildroot}%{_bindir}/eximstats \
    %{buildroot}%{_mandir}/man8/eximstats.8

%if %{build_monitor}
# Mandriva Icons
install -m0644 exim_monitor-48x48.png %{buildroot}%{_liconsdir}/%{name}-monitor.png
install -m0644 exim_monitor-32x32.png %{buildroot}%{_iconsdir}/%{name}-monitor.png
install -m0644 exim_monitor-16x16.png %{buildroot}%{_miconsdir}/%{name}-monitor.png

#menu-xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}-monitor.desktop << EOXDG
[Desktop Entry]
Name=Exim Monitor
Comment=X11 monitor application for exim
Exec=%{_bindir}/eximon
Icon=%{name}-monitor
Terminal=false
Type=Application
Categories=Settings;Network;
EOXDG

%endif

# include more README files in %%doc
cp src/auths/README README.auths
cp src/lookups/README README.lookups
cp src/routers/README README.routers
cp src/transports/README README.transports
cp doc/README README.doc

# cleanup
rm -f %{buildroot}%{_bindir}/exim-%{version}*

%post
%_post_service exim
%{alternatives_install_cmd}

# scrub hints files - db files change format between builds so
# killing the hints can save an MTA crash later
[ -d /var/spool/exim/db ] && rm -f /var/spool/exim/db/*

# alternatives changes the mode of /usr/bin/exim so we have to chmod
chmod 4755 %{_bindir}/exim

# Define FQDN
FQDN=`hostname`
if [ "x${FQDN}" = "x" ]; then
    FQDN="localhost.localdomain"
fi
# fix primary_hostname
perl -pi -e "s|^# primary_hostname =|primary_hostname = $FQDN|" %{_sysconfdir}/%{name}/%{name}.conf

# disable cron job if build_logrotate enabled:
%if %{build_logrotate}
if [ -f "/etc/cron.weekly/exim" ]; then
    day=`date +%Y%m%d`
    mv /etc/cron.weekly/exim /etc/exim/cron.weekly_exim.backup.$day
fi
%endif

%if %{build_certs}
# Add dummy certficates
if [ ! -f "%{tlsdir}/certs/%{name}.pem" ]; then
    touch %{tlsdir}/{certs,private,dhparam}/%{name}.pem
    umask 077
    cat << EOF | openssl req -new -x509 -days 365 -nodes \
    -out %{tlsdir}/certs/%{name}.pem \
    -keyout %{tlsdir}/private/%{name}.pem &>/dev/null
MandrivaLand
MandrivaCountry
MandrivaCity
SMTP server on ${FQDN}
SMTP SSL/TLS key on ${FQDN}
${FQDN}
root@${FQDN}
EOF
    openssl dhparam -check -text -5 512 -out %{tlsdir}/dhparam/%{name}.pem &>/dev/null
    %__chown mail.root %{tlsdir}/{private,certs,dhparam}/%{name}.pem
    %__chmod 600 %{tlsdir}/{private,certs,dhparam}/%{name}.pem
fi
%endif

# necessary when we upgrade from a non-alternatives package
%triggerpostun -- exim
[ -e %{_sbindir}/sendmail.exim ] && %{alternatives_install_cmd} || :

%preun
%_preun_service exim
if [ "$1" = "0" ]; then
    update-alternatives --remove mta %{_sbindir}/sendmail.exim
fi

%postun
if [ "$1" -ge "1" ]; then
    /sbin/service exim condrestart > /dev/null 2>&1
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ACKNOWLEDGMENTS CHANGES LICENCE NOTICE README*
%doc doc/ChangeLog doc/*.upgrade doc/NewStuff doc/OptionLists.txt doc/README.SIEVE doc/dbm.discuss.txt
%doc doc/experimental-spec.txt doc/filter.txt doc/pcrepattern.txt doc/pcretest.txt doc/spec.txt
%doc util/unknownuser.sh build-Linux-*/transport-filter.pl util/cramtest.pl util/logargs.sh
%attr(0755,root,mail) %dir %{_sysconfdir}/exim
%attr(0755,root,root) %{_initrddir}/exim
%attr(0644,root,mail) %config(noreplace) %{_sysconfdir}/exim/exim.conf
%attr(0644,root,mail) %config(noreplace) %{_sysconfdir}/exim/aliases
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/exim
%attr(0644,root,mail) %config(noreplace) %{_sysconfdir}/exim/exim_perl.pl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/eximstats.conf
%if %{build_sasl2}
%attr(0644,root,mail) %config(noreplace) %{_sysconfdir}/sasl2/smtpd.conf
%endif
%if %{build_logrotate}
%attr(0644,root,mail) %config(noreplace) %{_sysconfdir}/logrotate.d/exim
%else
%attr(0755,root,root) %{_sysconfdir}/cron.weekly/exim
%endif
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/smtp
# SSL/TLS
%attr(0600,root,root) %dir %{tlsdir}/certs
%attr(0600,root,root) %dir %{tlsdir}/dhparam
%attr(0600,root,root) %dir %{tlsdir}/private
# end SSL/TLS
%attr(0755,root,root) %{_bindir}/convert4r3
%attr(0755,root,root) %{_bindir}/convert4r4
%attr(0755,root,root) %{_bindir}/exicyclog
%attr(0755,root,root) %{_bindir}/exigrep
%attr(0755,root,root) %{_bindir}/exim_checkaccess
%attr(0755,root,root) %{_bindir}/exim_dbmbuild
%attr(0755,root,root) %{_bindir}/exim_dumpdb
%attr(0755,root,root) %{_bindir}/exim_fixdb
%attr(0755,root,root) %{_bindir}/exim_lock
%attr(0755,root,root) %{_bindir}/eximstats
%attr(0755,root,root) %{_bindir}/exim_tidydb
%attr(0755,root,root) %{_bindir}/exinext
%attr(0755,root,root) %{_bindir}/exipick
%attr(0755,root,root) %{_bindir}/exiqgrep
%attr(0755,root,root) %{_bindir}/exiqsumm
%attr(0755,root,root) %{_bindir}/exiwhat
%attr(0755,root,root) %{_bindir}/rsmtp
%attr(0755,root,root) %{_bindir}/runq
%attr(4755,root,root) %{_bindir}/exim
%attr(0755,root,root) %{_sbindir}/exim
#%attr(0755,root,root) %{_sbindir}/eximconfig
# alternatives
%attr(0755,root,root) %{_sbindir}/sendmail.exim
%attr(0644,root,root) %{_prefix}/lib/sendmail.exim
%attr(0755,root,root) %{_bindir}/mailq.exim
%attr(0755,root,root) %{_bindir}/newaliases.exim
%attr(0755,root,root) %{_bindir}/rmail.exim
%attr(0755,root,root) %{_bindir}/rsmtp.exim
%attr(0755,root,root) %{_bindir}/runq.exim
%attr(0755,mail,mail) %dir %{_var}/spool/exim
%attr(0755,mail,mail) %dir %{_var}/spool/exim/db
%attr(0755,mail,mail) %dir %{_var}/spool/exim/input
%attr(0755,mail,mail) %dir %{_var}/spool/exim/msglog
%attr(0755,mail,mail) %dir %{_logdir}/exim
%attr(0755,mail,mail) %dir %{_var}/run/exim
%attr(0644,root,root) %{_mandir}/man8/exim.8*
%attr(0644,root,root) %{_mandir}/man8/eximstats.8*

%if %{build_monitor}
%files monitor
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/eximon
%attr(0755,root,root) %{_bindir}/eximon.bin
%{_iconsdir}/%{name}-monitor.png
%{_miconsdir}/%{name}-monitor.png
%{_liconsdir}/%{name}-monitor.png
%{_datadir}/applications/mandriva-%{name}-monitor.desktop
%endif

%files plugins-SpamAssassin
%defattr(-,root,root)
%doc sa-exim-%{saversion}/*.html sa-exim-%{saversion}/{ACKNOWLEDGEMENTS,CHANGELOG,INSTALL,LICENSE,TODO,contrib}
%doc sa-exim-%{saversion}/{README,README.greylisting,*.diff}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/exim/sa-exim.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/exim/sa-exim_short.conf
%dir %{_libdir}/exim
%attr(0644,root,root) %{_libdir}/exim/*

%files doc
%defattr(-,root,root)
%doc doc/html config.samples README.urpmi


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 4.76-3mdv2012.0
+ Revision: 772951
- relink against libpcre.so.1

* Wed Oct 05 2011 Oden Eriksson <oeriksson@mandriva.com> 4.76-2
+ Revision: 703054
- further build fixes
- 4.76 (fixes CVE-2011-1764)
- rework the spec file a bit

  + Per Ãyvind Karlsen <peroyvind@mandriva.org>
    - rebuild against db 5.1.25

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 4.72-7
+ Revision: 645794
- relink against libmysqlclient.so.18

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 4.72-6
+ Revision: 635345
- tighten BR

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 4.72-5mdv2011.0
+ Revision: 627221
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 4.72-4mdv2011.0
+ Revision: 626515
- rebuilt against mysql-5.5.8 libs

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 4.72-2mdv2011.0
+ Revision: 610407
- rebuild

* Sun Jun 06 2010 Oden Eriksson <oeriksson@mandriva.com> 4.72-1mdv2010.1
+ Revision: 547154
- 4.72 (fixes CVE-2010-2023, CVE-2010-2024)
- drop one upstream added patch and rediffed some

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 4.69-7mdv2010.1
+ Revision: 533154
- Rebuild for openssl 1.0.0.

* Thu Feb 18 2010 Oden Eriksson <oeriksson@mandriva.com> 4.69-6mdv2010.1
+ Revision: 507484
- rebuild

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 4.69-5mdv2010.1
+ Revision: 484302
- br db 4.8

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 4.69-4mdv2010.0
+ Revision: 437505
- rebuild

* Sat Mar 28 2009 Funda Wang <fwang@mandriva.org> 4.69-3mdv2009.1
+ Revision: 362036
- bump rel
- fix str fmt
- rediff default patch

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 4.69-2mdv2009.1
+ Revision: 311300
- rebuilt against mysql-5.1.30 libs

* Sat Nov 08 2008 Vincent Danen <vdanen@mandriva.com> 4.69-1mdv2009.1
+ Revision: 301175
- make the sendmail link in /usr/lib where it should be, not /usr/lib64

* Tue Sep 02 2008 Vincent Danen <vdanen@mandriva.com> 4.69-1mdv2009.0
+ Revision: 279286
- 4.69
- rediff P0 (config)
- drop P8 (openssl patch)
- add conflicts for postfix, sendmail, qmail
- bunzip sources

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 4.63-16mdv2009.0
+ Revision: 244998
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 23 2008 Thierry Vignaud <tv@mandriva.org> 4.63-14mdv2008.1
+ Revision: 157248
- rebuild with fixed %%serverbuild macro

* Mon Dec 24 2007 Oden Eriksson <oeriksson@mandriva.com> 4.63-13mdv2008.1
+ Revision: 137506
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Funda Wang <fwang@mandriva.org> 4.63-12mdv2008.1
+ Revision: 116158
- New license policy
- remove quotes characters in menu item

* Fri Sep 07 2007 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 4.63-11mdv2008.0
+ Revision: 81764
- Add requires perl-Net-IMAP-Simple (fixes #33281)

* Fri Jul 13 2007 Funda Wang <fwang@mandriva.org> 4.63-10mdv2008.0
+ Revision: 51839
- Remove unnecessary dependencies

* Wed Jul 04 2007 Andreas Hasenack <andreas@mandriva.com> 4.63-9mdv2008.0
+ Revision: 48270
- using serverbuild macro (-fstack-protector-all)


* Wed Mar 21 2007 Oden Eriksson <oeriksson@mandriva.com> 4.63-8mdv2007.1
+ Revision: 147277
- bunzip patches
- make it build against latest openssl (P8)
- rebuild

* Tue Nov 07 2006 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 4.63-7mdv2007.0
+ Revision: 77423
- Import exim

* Mon Oct 30 2006 Stéphane Téletchéa <steletch@mandriva.org> 4.63-7mdv2007.1
- Drop certificate generation
- From Serge Demonchaux:
	- the OPENSSLDIR has moved to /etc/pki/tls (openssl0.9.8-0.9.8b-2.2mdv2007.0)
	- fix requires in package exim-plugins-SpamAssassin
	- add test entry (exim.init)
	- add alias (/eximstats /var/www/eximstats) for apache
	- add P7 (/etc/exim/exim.conf) default mandriva config for exim-4.63:
	- fix path to tls certificates (certs,private,dhparam)
	- add more authentificators (saslauth, lookup sqlite and mysql, auth with perl)
	- add customized header
	- moved /etc/pam.d/exim to /etc/pam.d/smtp required to correct authentication with saslauthd
	- update begin init info to use saslauthd
	- update/clean exim.init (S21)
	- disabled old eximconfig (S6)
	- disabled P2 (exim-4.33-cyrus.patch) now in P7
	- add README.urpmi
	- fix buildrequires for pre 2007.0

* Thu Sep 28 2006 Stéphane Téletchéa <steletch@mandriva.org> 4.63-6mdv2007.0
- From Serge Demonchaux:
- /etc/exim/exim.conf:
	- add exim's embedded perl script at start
	- fix primary_hostname
	- add "@[] : localhost : localhost.localdomain : $primary_hostname"  as local_domains
	- fixe path to tls certificates (certs,private,dhparam)
	- enable spamassassin if spamd installed
	- add scripts for generating tls certificates (certs,private,dhparam)
	- implement "mta-pam" alternatives with sasl2 if sasl2 enabled
	- add sasl2 build option (enabled) to use cyrus-sasl + /etc/sasl2/smtpd.conf (cyrus-sasl config)
	- add exim's embedded perl script /etc/exim/exim_perl.pl (the Perl routine attempts the IMAP/POP3 login and returns the result to Exim).
	- add logrotate script with eximstats (enabled)
	- if logrotate disabled, install cron job with eximstats report
	- add new entry in /etc/sysconfig/exim
	- update alternatives_install_cmd to use mta-pam for sasl2 in alternatives

* Mon Sep 25 2006 Stéphane Téletchéa <steletch@mandriva.org> 4.63-5mdv2007.0
- fix SYSTEM_ALIASES_FILE macro
- translate some comments

* Fri Sep 15 2006 Stéphane Téletchéa <steletch@mandriva.org> 4.63-4mdv2007.0
- update spec file
- fix xdg menus for exim-monitor
- drop Corporate Server 2.1 since it is no more supported as of feb 28th 2006
- adapt exim.pam to use the Linux-PAM new format
- fix some permissions

* Tue Sep 12 2006 Serge Demonchaux <serge-sd3l@sd3l.homelinux.net> 4.63-3-1.20060mdk
- eximconfig (source6):
	- Adding MandivaLinux in "Received" message header;
	- Fixed aliases file path.
- exim.init (source21):
	Adding begin init info (MandrivaLinux 2007.0).

* Sat Sep 09 2006 Serge Demonchaux <serge-sd3l@sd3l.homelinux.net> 4.63-2-1.20060mdk
- Fixed %%{name}-doc description;
- Fixed spec file for Corporate Server 2.1;
- Rebuild with db4.2-devel.

* Thu Sep 07 2006 Serge Demonchaux <serge-sd3l@sd3l.homelinux.net> 4.63-1-1.20060sd3l
- SQLite3 3.3.6
- Enabled ldap build default (default mandriva build option).

* Thu Aug 31 2006 Serge Demonchaux <serge-sd3l@sd3l.homelinux.net> 4.63-0-1.20060sd3l
- exim 4.63
- disable Patch6

* Wed Apr 05 2006 Serge Demonchaux <serge-sd3l@sd3l.homelinux.net> 4.61-1-1.20060sd3l
- Patch6: apply the exim acl.c patch (only 4.60).
- build with db4.3-devel

* Wed Apr 05 2006 Serge Demonchaux <serge-sd3l@sd3l.homelinux.net> 4.61-0-1.20060sd3l
- exim 4.61

* Sun Feb 12 2006 Serge Demonchaux <serge-sd3l@sd3l.homelinux.net> 4.60-0-1.20060sd3l
- exim 4.60
- sa-exim-4.2.1
- perl 5.8.7
- SQLite3 3.2.2 (new in exim-4.6x)
- MyQSL-4.1.12
- added more build options:
	- with[out] ldap (disabled)
	- with[out] sqlite3 (enabled)
- new Patch0.
- new Patch4.

* Wed Nov 23 2005 Laurent MONTEL <lmontel@mandriva.com> 4.50-7
- Rebuild with new openssl

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 4.50-6mdk
- rebuilt against MySQL-5.0.15

* Wed Aug 31 2005 Oden Eriksson <oeriksson@mandriva.com> 4.50-5mdk
- rebuilt against new openldap-2.3.6 libs

* Mon Aug 01 2005 Marcel Pol <mpol@manddriva.org> 4.50-4mdk
- remove msec hack
- generate README.install.urpmi

* Wed Jul 13 2005 Michael Scherer <misc@mandriva.org> 4.50-3mdk
- fix provides

* Fri May 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 4.50-2mdk
- Rebuild for new perl

* Thu Mar 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.50-1mdk
- 4.50
- the exiscan patch is now integrated
- sa-exim-4.2
- use the %%mkrel macro
- added more build options
- dropped the CAN-2005-0022, CAN-2005-0023 patch, it's integrated

* Tue Feb 15 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.43-11mdk
- added P6 from rh (CAN-2005-0022, CAN-2005-0023)

* Mon Feb 07 2005 Buchan Milne <bgmilne@linux-mandrake.com> 4.43-10mdk
- rebuild for ldap2.2_7

* Fri Feb 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.43-9mdk
- rebuilt against new openldap libs

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.43-8mdk
- rebuilt against MySQL-4.1.x and system libs

* Tue Jan 04 2005 Marcel Pol <mpol@mandrake.org> 4.43-7mdk
- provides smtpdaemon
- build for 10.2

* Wed Dec 08 2004 Marcel Pol <mpol@mandrake.org> 4.43-6mdk
- buildrequires perl-devel

* Thu Nov 18 2004 Marcel Pol <mpol@mandrake.org> 4.43-5mdk
- fix build without monitor (Fengchou Li)

* Fri Nov 05 2004 Marcel Pol <mpol@mandrake.org> 4.43-4mdk
- fix build for 10.0

* Thu Nov 04 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.43-3mdk
- merged the most crucial fixes from into the package 
  by Marcel Pol into this package
- reviewed and fixed P0

* Thu Nov 04 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.43-2mdk
- added P4, use system pcre libs instead (debian)
- added P5, don't override cflags (debian)

* Wed Nov 03 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.43-1mdk
- initial mandrake package
- based on the annvix and fedora spec file and config but 
  with a little twist
- used the http://www.exim.org/images/exim-blue-ld-sml.png
  image as icon for the monitor sub package

* Sun Oct 31 2004 Marcel Pol <mpol@mandrake.org> 4.43-1mdk
- 4.43
- exiscan 4.43-28
- exim-html 4.40
- rediff P0
- build for 10.1 against db4.2
- add exipick to filelist
- make initscript readable (755)
- s/Copyright/License

