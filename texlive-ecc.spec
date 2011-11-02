Name:		texlive-ecc
Version:	20061207
Release:	1
Summary:	Sources for the European Concrete fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ecc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ecc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The MetaFont sources and TFM files of the European Concrete
Fonts. This is the T1-encoded extension of Knuth's Concrete
fonts, including also the corresponding text companion fonts.
Adobe Type 1 versions of the fonts are available as part of the
cm-super font bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/ecc/conc10pt.mf
%{_texmfdistdir}/fonts/source/public/ecc/conc5pt.mf
%{_texmfdistdir}/fonts/source/public/ecc/conc6pt.mf
%{_texmfdistdir}/fonts/source/public/ecc/conc7pt.mf
%{_texmfdistdir}/fonts/source/public/ecc/conc8pt.mf
%{_texmfdistdir}/fonts/source/public/ecc/conc9pt.mf
%{_texmfdistdir}/fonts/source/public/ecc/coni10pt.mf
%{_texmfdistdir}/fonts/source/public/ecc/eocc10.mf
%{_texmfdistdir}/fonts/source/public/ecc/eorm10.mf
%{_texmfdistdir}/fonts/source/public/ecc/eorm5.mf
%{_texmfdistdir}/fonts/source/public/ecc/eorm6.mf
%{_texmfdistdir}/fonts/source/public/ecc/eorm7.mf
%{_texmfdistdir}/fonts/source/public/ecc/eorm8.mf
%{_texmfdistdir}/fonts/source/public/ecc/eorm9.mf
%{_texmfdistdir}/fonts/source/public/ecc/eosl10.mf
%{_texmfdistdir}/fonts/source/public/ecc/eosl5.mf
%{_texmfdistdir}/fonts/source/public/ecc/eosl6.mf
%{_texmfdistdir}/fonts/source/public/ecc/eosl7.mf
%{_texmfdistdir}/fonts/source/public/ecc/eosl8.mf
%{_texmfdistdir}/fonts/source/public/ecc/eosl9.mf
%{_texmfdistdir}/fonts/source/public/ecc/eoti10.mf
%{_texmfdistdir}/fonts/source/public/ecc/tcssdc10.mf
%{_texmfdistdir}/fonts/source/public/ecc/torm10.mf
%{_texmfdistdir}/fonts/source/public/ecc/torm5.mf
%{_texmfdistdir}/fonts/source/public/ecc/torm6.mf
%{_texmfdistdir}/fonts/source/public/ecc/torm7.mf
%{_texmfdistdir}/fonts/source/public/ecc/torm8.mf
%{_texmfdistdir}/fonts/source/public/ecc/torm9.mf
%{_texmfdistdir}/fonts/source/public/ecc/tosl10.mf
%{_texmfdistdir}/fonts/source/public/ecc/tosl5.mf
%{_texmfdistdir}/fonts/source/public/ecc/tosl6.mf
%{_texmfdistdir}/fonts/source/public/ecc/tosl7.mf
%{_texmfdistdir}/fonts/source/public/ecc/tosl8.mf
%{_texmfdistdir}/fonts/source/public/ecc/tosl9.mf
%{_texmfdistdir}/fonts/source/public/ecc/toti10.mf
%{_texmfdistdir}/fonts/tfm/public/ecc/eocc10.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eorm10.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eorm5.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eorm6.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eorm7.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eorm8.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eorm9.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eosl10.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eosl5.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eosl6.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eosl7.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eosl8.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eosl9.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/eoti10.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/tcssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/torm10.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/torm5.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/torm6.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/torm7.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/torm8.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/torm9.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/tosl10.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/tosl5.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/tosl6.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/tosl7.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/tosl8.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/tosl9.tfm
%{_texmfdistdir}/fonts/tfm/public/ecc/toti10.tfm
%doc %{_texmfdistdir}/doc/fonts/ecc/copyrite
%doc %{_texmfdistdir}/doc/fonts/ecc/liesmich
%doc %{_texmfdistdir}/doc/fonts/ecc/readme

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
