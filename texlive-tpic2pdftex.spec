%global tl_name tpic2pdftex
%global tl_revision 75712

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Use tpic commands in pdfTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/tpic2pdftex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tpic2pdftex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tpic2pdftex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(tpic2pdftex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This AWK script converts pic language, embedded inline (delimited by .PS
and .PE markers), to \pdfliteral commands. It is now maintained as part
of TeX Live.

