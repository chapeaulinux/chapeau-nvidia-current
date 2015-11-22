%define _use_internal_dependency_generator 0

Summary:	Chapeau meta-package for nvidia proprietary drivers
Name:		chapeau-nvidia-current
Version:	1
Release:	2%{?dist}
License:	distributable
Group:		Chapeau
URL:		http://chapeaulinux.org
BuildArch:	x86_64

Requires:	akmod-nvidia
Requires:	libvdpau
Requires:	libvdpau(x86-32)
Requires:	libva-vdpau-driver
Requires:	libva-utils
Requires:	xorg-x11-drv-nvidia-libs(x86-32)

%description
A meta package for the nvidia drivers packages from RPMFusion

%prep

%build

%clean 

%install

%post

%preun
[ $1 =0 ] && rpm -e akmod-nvidia xorg-x11-drv-nvidia-libs.i686
return 0

%files 


%changelog
* Sat Nov 21 2014 Vince Pooley <vince@chapeaulinux.org>
- Fix 32bit requirements

* Fri Nov 20 2014 Vince Pooley <vince@chapeaulinux.org>
- initial release

