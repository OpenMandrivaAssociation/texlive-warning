Name:		texlive-warning
Version:	22028
Release:	2
Summary:	Global warnings at the end of the logfile
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/warning
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warning.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/warning.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a command that generates a list of
warnings that are printed out at the very end of the logfile.
This is useful for warnings such as 'Rerun for this or that
reason' or 'This is a draft, change it before the final run'.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/warning/warning.sty
%doc %{_texmfdistdir}/doc/latex/warning/warning-doc.pdf
%doc %{_texmfdistdir}/doc/latex/warning/warning-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
