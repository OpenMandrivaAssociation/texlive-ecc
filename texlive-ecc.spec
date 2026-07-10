%global tl_name ecc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Sources for the European Concrete fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ecc
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ecc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Metafont sources and TFM files of the European Concrete Fonts. This
is the T1-encoded extension of Knuth's Concrete fonts, including also
the corresponding text companion fonts. Adobe Type 1 versions of the
fonts are available as part of the cm-super font bundle.

