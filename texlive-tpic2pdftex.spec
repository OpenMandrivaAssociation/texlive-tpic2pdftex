Name:		texlive-tpic2pdftex
Version:	52851
Release:	2
Summary:	Use tpic commands in PDFTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/tpic2pdftex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpic2pdftex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpic2pdftex.doc.r%{version}.tar.xz
# Not actually x86_64 binaries -- it's a shell script
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpic2pdftex.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Provides:	texlive-tpic2pdftex.bin = %{EVRD}

%description
The AWK script converts pic language, embedded inline
(delimited by .PS and .PE markers), to \pdfliteral commands.

#-----------------------------------------------------------------------
%files
%{_bindir}/tpic2pdftex
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/tpic2pdftex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
# shell script
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mv bin/*/* %{buildroot}%{_bindir}/
