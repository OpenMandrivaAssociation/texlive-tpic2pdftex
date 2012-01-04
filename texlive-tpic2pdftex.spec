# revision 23089
# category TLCore
# catalog-ctan /graphics/tpic2pdftex
# catalog-date 2010-01-16 19:56:06 +0100
# catalog-license gpl
# catalog-version 1.97
Name:		texlive-tpic2pdftex
Version:	1.97
Release:	2
Summary:	Use tpic commands in PDFTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/tpic2pdftex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpic2pdftex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tpic2pdftex.doc.tar.xz
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
%doc %{_mandir}/man1/tpic2pdftex.1*
%doc %{_texmfdir}/doc/man/man1/tpic2pdftex.man1.pdf
%doc %{_texmfdir}/doc/tpic2pdftex/Makefile
%doc %{_texmfdir}/doc/tpic2pdftex/beamerexample.pdf
%doc %{_texmfdir}/doc/tpic2pdftex/beamerexample.pic
%doc %{_texmfdir}/doc/tpic2pdftex/example.pdf
%doc %{_texmfdir}/doc/tpic2pdftex/example.pic

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
# shell script
mkdir -p %{buildroot}%{_bindir}
cp -fpa bin/x86_64-linux/tpic2pdftex %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
