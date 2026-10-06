%global commit      3e1c26e79782e257fac8b61fa23598aa7a6411c7
%global shortcommit %{sub %{commit} 1 7}

Name:           qwinblowsdecorations
Version:        0.1.7
Release:        12.%{shortcommit}%{?dist}
Summary:        Qt decoration plugin implementing Windows-like client-side decorations

License:        LGPL-2.1-or-later
URL:            https://github.com/adil192/QWinblowsDecorations
Source0:        https://github.com/adil192/QWinblowsDecorations/archive/%{commit}/QWinblowsDecorations-%{commit}.tar.gz


BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  wayland-devel

%description
%{summary}.

%package qt6
Summary:        Qt decoration plugin implementing Windows-like client-side decorations
BuildRequires:  qt6-qtbase-devel >= 6.5.0
BuildRequires:  qt6-qtbase-static >= 6.5.0
BuildRequires:  qt6-qtwayland-devel >= 6.5.0
BuildRequires:  qt6-qtbase-private-devel >= 6.5.0
BuildRequires:  qt6-qtsvg-devel >= 6.5.0
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

# When GNOME Shell and Qt 6 are installed, we want this by default
Supplements:   (qt6-qtbase and gnome-shell)

Provides:       qadwaitadecorations-qt6 = %{version}-%{release}
Obsoletes:      qadwaitadecorations-qt6 < 0.1.8
Obsoletes:      qadwaitadecorations-qt6 < 1:0.1.8

%description qt6
%{summary}.

%prep
%autosetup -p1 -n  QWinblowsDecorations-%{commit}

%build
%global _vpath_builddir %{_target_platform}-qt6
%cmake -DUSE_QT6=true
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%files qt6
%doc README.md
%license LICENSE
%{_qt6_plugindir}/wayland-decoration-client/libqwinblowsdecorations.so

%changelog
* Tue Oct 06 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-12
- Rebrand from QAdwaitaDecorations to QWinblowsDecorations

* Wed Sep 09 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-11
- Rebuild (qt6)

* Mon Sep 07 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-10
- Build from pinned commit

* Sun Sep 06 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-9
- Improved window button colors.

* Wed Aug 26 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-8
- Rebuild (qt6)

* Sat Aug 22 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-7
- Fixed the min/max/close buttons having a resize cursor on hover.

* Tue Aug 11 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-6
- Worked around qt6ct not updating instantly when changing light/dark mode. If the color scheme isn't available yet, it will try again in a few seconds.

* Mon Aug 10 2026 Adil Hanney <adilhanney@disroot.org> - 0.1.7-5
- Switched to my Windows-inspired fork of QWinblowsDecorations

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Nov 04 2025 Jan Grulich <jgrulich@redhat.com> - 0.1.7-2
- Rebuild (qt5)

* Tue Oct 07 2025 Jan Grulich <jgrulich@redhat.com> - 0.1.7-1
- 0.1.7

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 26 2025 Jan Grulich <jgrulich@redhat.com> - 0.1.6-8
- Rebuild (qt5)

* Mon Feb 03 2025 Jan Grulich <jgrulich@redhat.com> - 0.1.6-7
- Rebuild (qt6)

* Wed Jan 22 2025 Jan Grulich <jgrulich@redhat.com> - 0.1.6-6
- Rebuild (qt5)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Jan Grulich <jgrulich@redhat.com> - 0.1.6-4
- Rebuild (qt5)

* Tue Dec 10 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.6-3
- Fix condition where we wrongly enabled -qt6 on F41+

* Wed Dec 04 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.6-2
- Rebuild (qt6)

* Fri Nov 29 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.6-1
- 0.1.6

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.5-8
- Rebuild (qt6)

* Thu Sep 05 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.5-7
- Rebuild (qt5)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.5-5
- Rebuild (qt6)

* Thu May 30 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.5-4
- Rebuild (qt5)

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.5-3
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.5-2
- Rebuild (qt6)

* Wed Mar 20 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.5-1
- 0.1.5

* Fri Mar 15 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.4-3
- Rebuild (qt5)

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.4-2
- Rebuild (qt6)

* Fri Jan 26 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.4-1
- 0.1.4

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.3-5
- Rebuild (qt5)

* Mon Dec 11 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-4
- Skip empty icon themes

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-3
- Rebuild (qt6)

* Wed Nov 22 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-2
- Backport upstream fixes and improvements
  - fix crash on forcing repaint on non-existing decorations
  - fix indentation of buttons when placed on the left side
  - apply correct button order
  - use Adwaita icons as fallback

* Mon Oct 16 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-1
- 0.1.3

* Sun Oct 15 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-5
- Upstream backport: do not use lambda function for DBus response

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-4
- Rebuild (qt6)

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-3
- Rebuild (qt5)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 0.1.2-2
- Rebuild for Qt Private API

* Wed Sep 27 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-1
- 0.1.2

* Mon Sep 11 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.1-1
- 0.1.1

* Tue Aug 15 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.0
- Initial package
