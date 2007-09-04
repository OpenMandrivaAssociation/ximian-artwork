Name:		ximian-artwork
Version: 0.2.34
Release: %mkrel 3
License:	GPL
BuildRoot:	%_tmppath/%{name}-%{version}-root
URL:		http://www.ximian.com/
Source0:	%name-%version.tar.bz2
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
Summary:	The Default Style for Ximian Desktop
Group: Graphical desktop/GNOME
Requires: gnome-icon-theme
Requires: gtk-engines2 >= 2.6.0
BuildRequires: intltool automake1.8

%description
ximian-artwork contains the default style configuration for the Ximian Desktop.
This package contains themes for GNOME2, gdm xmms and galeon.

%prep
%setup  -q
aclocal-1.8
intltoolize --force
autoconf
automake-1.8

%build
%configure2_5x
%make

%install
%makeinstall_std
rm %buildroot%{_libdir}/gtk/themes/engines/*a
# GTK2 industrial engine is now in gtk-engines2
rm %buildroot%{_libdir}/gtk-2.0/engines/*
rm -rf %buildroot%{_datadir}/themes/Industrial/gtk-2.0
cd %buildroot%_datadir/icons/gnome/32x32/apps
#gw remove the icons already present in gnome-icon-theme
rm -f administration.png apacheconf.png applets-screenshooter.png file-manager.png gnome-networktool.png logviewer.png network-config.png network.png postscript-viewer.png serviceconf.png system-floppy.png 
cd ../../48x48/apps
rm -f administration.png apacheconf.png applets-screenshooter.png file-manager.png gnome-networktool.png logviewer.png network-config.png network.png postscript-viewer.png serviceconf.png tsclient.png web-browser.png xcdroast.png xsane.png
touch %buildroot%_datadir/icons/Industrial/icon-theme.cache

%clean
rm -fr %buildroot

%post
%update_icon_cache Industrial
%postun
%clean_icon_cache Industrial

%files
%defattr(-, root, root)
%doc COPYING
%{_datadir}/themes/*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/ximian/
%{_datadir}/pixmaps/backgrounds/ximian/
%{_datadir}/gdm/themes/*
%{_datadir}/galeon/themes/*
%{_datadir}/pixmaps/nautilus/*
%{_libdir}/gtk/themes/engines/libindustrial.so
%{_datadir}/xmms/Skins/*
%dir %{_datadir}/icons/Industrial/
%{_datadir}/icons/Industrial/*/
%{_datadir}/icons/Industrial/index.theme
%ghost %_datadir/icons/Industrial/icon-theme.cache
