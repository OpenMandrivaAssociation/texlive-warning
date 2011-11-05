# revision 22028
# category Package
# catalog-ctan /macros/latex/contrib/warning
# catalog-date 2011-04-08 17:41:44 +0200
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-warning
Version:	0.01
Release:	1
Summary:	Global warnings at the end of the logfile
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/warning
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warning.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warning.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides a command that generates a list of
warnings that are printed out at the very end of the logfile.
This is useful for warnings such as 'Rerun for this or that
reason' or 'This is a draft, change it before the final run'.

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
%{_texmfdistdir}/tex/latex/warning/warning.sty
%doc %{_texmfdistdir}/doc/latex/warning/warning-doc.pdf
%doc %{_texmfdistdir}/doc/latex/warning/warning-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
