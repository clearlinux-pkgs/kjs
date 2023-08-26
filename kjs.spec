#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kjs
Version  : 5.109.0
Release  : 64
URL      : https://download.kde.org/stable/frameworks/5.109/portingAids/kjs-5.109.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.109/portingAids/kjs-5.109.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.109/portingAids/kjs-5.109.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kjs-bin = %{version}-%{release}
Requires: kjs-data = %{version}-%{release}
Requires: kjs-lib = %{version}-%{release}
Requires: kjs-license = %{version}-%{release}
Requires: kjs-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(libpcre)
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This library provides an ECMAScript compatible interpreter. The ECMA standard
is based on well known scripting languages such as Netscape's JavaScript and
Microsoft's JScript.

%package bin
Summary: bin components for the kjs package.
Group: Binaries
Requires: kjs-data = %{version}-%{release}
Requires: kjs-license = %{version}-%{release}

%description bin
bin components for the kjs package.


%package data
Summary: data components for the kjs package.
Group: Data

%description data
data components for the kjs package.


%package dev
Summary: dev components for the kjs package.
Group: Development
Requires: kjs-lib = %{version}-%{release}
Requires: kjs-bin = %{version}-%{release}
Requires: kjs-data = %{version}-%{release}
Provides: kjs-devel = %{version}-%{release}
Requires: kjs = %{version}-%{release}

%description dev
dev components for the kjs package.


%package lib
Summary: lib components for the kjs package.
Group: Libraries
Requires: kjs-data = %{version}-%{release}
Requires: kjs-license = %{version}-%{release}

%description lib
lib components for the kjs package.


%package license
Summary: license components for the kjs package.
Group: Default

%description license
license components for the kjs package.


%package man
Summary: man components for the kjs package.
Group: Default

%description man
man components for the kjs package.


%prep
%setup -q -n kjs-5.109.0
cd %{_builddir}/kjs-5.109.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693018973
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1693018973
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kjs
cp %{_builddir}/kjs-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kjs/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kjs5
/usr/bin/kjs5

%files data
%defattr(-,root,root,-)
/usr/share/kf5/kjs/create_hash_table

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/kjs/CommonIdentifiers.h
/usr/include/KF5/kjs/CompileState.h
/usr/include/KF5/kjs/ExecState.h
/usr/include/KF5/kjs/JSImmediate.h
/usr/include/KF5/kjs/JSLock.h
/usr/include/KF5/kjs/JSType.h
/usr/include/KF5/kjs/JSVariableObject.h
/usr/include/KF5/kjs/JSWrapperObject.h
/usr/include/KF5/kjs/LocalStorage.h
/usr/include/KF5/kjs/Parser.h
/usr/include/KF5/kjs/PropertyNameArray.h
/usr/include/KF5/kjs/SavedBuiltins.h
/usr/include/KF5/kjs/SymbolTable.h
/usr/include/KF5/kjs/array_instance.h
/usr/include/KF5/kjs/array_object.h
/usr/include/KF5/kjs/bool_object.h
/usr/include/KF5/kjs/collector.h
/usr/include/KF5/kjs/commonunicode.h
/usr/include/KF5/kjs/completion.h
/usr/include/KF5/kjs/context.h
/usr/include/KF5/kjs/date_object.h
/usr/include/KF5/kjs/debugger.h
/usr/include/KF5/kjs/dtoa.h
/usr/include/KF5/kjs/error_object.h
/usr/include/KF5/kjs/function.h
/usr/include/KF5/kjs/function_object.h
/usr/include/KF5/kjs/global.h
/usr/include/KF5/kjs/grammar.h
/usr/include/KF5/kjs/identifier.h
/usr/include/KF5/kjs/internal.h
/usr/include/KF5/kjs/interpreter.h
/usr/include/KF5/kjs/json_object.h
/usr/include/KF5/kjs/jsonlexer.h
/usr/include/KF5/kjs/jsonstringify.h
/usr/include/KF5/kjs/kjsapi_export.h
/usr/include/KF5/kjs/kjsarguments.h
/usr/include/KF5/kjs/kjscontext.h
/usr/include/KF5/kjs/kjsinterpreter.h
/usr/include/KF5/kjs/kjsobject.h
/usr/include/KF5/kjs/kjsprototype.h
/usr/include/KF5/kjs/lexer.h
/usr/include/KF5/kjs/list.h
/usr/include/KF5/kjs/lookup.h
/usr/include/KF5/kjs/makenodes.h
/usr/include/KF5/kjs/math_object.h
/usr/include/KF5/kjs/nodes.h
/usr/include/KF5/kjs/nodes2bytecode.h
/usr/include/KF5/kjs/number_object.h
/usr/include/KF5/kjs/object.h
/usr/include/KF5/kjs/object_object.h
/usr/include/KF5/kjs/operations.h
/usr/include/KF5/kjs/package.h
/usr/include/KF5/kjs/property_map.h
/usr/include/KF5/kjs/property_slot.h
/usr/include/KF5/kjs/propertydescriptor.h
/usr/include/KF5/kjs/protect.h
/usr/include/KF5/kjs/regexp.h
/usr/include/KF5/kjs/regexp_object.h
/usr/include/KF5/kjs/scope_chain.h
/usr/include/KF5/kjs/scriptfunction.h
/usr/include/KF5/kjs/string_object.h
/usr/include/KF5/kjs/types.h
/usr/include/KF5/kjs/ustring.h
/usr/include/KF5/kjs/value.h
/usr/include/KF5/kjs_version.h
/usr/include/KF5/wtf/ASCIICType.h
/usr/include/KF5/wtf/AlwaysInline.h
/usr/include/KF5/wtf/Assertions.h
/usr/include/KF5/wtf/DisallowCType.h
/usr/include/KF5/wtf/FastMalloc.h
/usr/include/KF5/wtf/Forward.h
/usr/include/KF5/wtf/GetPtr.h
/usr/include/KF5/wtf/HashCountedSet.h
/usr/include/KF5/wtf/HashFunctions.h
/usr/include/KF5/wtf/HashIterators.h
/usr/include/KF5/wtf/HashMap.h
/usr/include/KF5/wtf/HashSet.h
/usr/include/KF5/wtf/HashTable.h
/usr/include/KF5/wtf/HashTraits.h
/usr/include/KF5/wtf/ListRefPtr.h
/usr/include/KF5/wtf/MathExtras.h
/usr/include/KF5/wtf/Noncopyable.h
/usr/include/KF5/wtf/OwnArrayPtr.h
/usr/include/KF5/wtf/OwnPtr.h
/usr/include/KF5/wtf/PassRefPtr.h
/usr/include/KF5/wtf/Platform.h
/usr/include/KF5/wtf/RefCounted.h
/usr/include/KF5/wtf/RefPtr.h
/usr/include/KF5/wtf/RefPtrHashMap.h
/usr/include/KF5/wtf/SharedPtr.h
/usr/include/KF5/wtf/UnusedParam.h
/usr/include/KF5/wtf/Vector.h
/usr/include/KF5/wtf/VectorTraits.h
/usr/lib64/cmake/KF5JS/KF5JSConfig.cmake
/usr/lib64/cmake/KF5JS/KF5JSConfigVersion.cmake
/usr/lib64/cmake/KF5JS/KF5JSTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5JS/KF5JSTargets.cmake
/usr/lib64/libKF5JS.so
/usr/lib64/libKF5JSApi.so
/usr/lib64/qt5/mkspecs/modules/qt_KJS.pri
/usr/lib64/qt5/mkspecs/modules/qt_KJSApi.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5JS.so.5.109.0
/V3/usr/lib64/libKF5JSApi.so.5.109.0
/usr/lib64/libKF5JS.so.5
/usr/lib64/libKF5JS.so.5.109.0
/usr/lib64/libKF5JSApi.so.5
/usr/lib64/libKF5JSApi.so.5.109.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kjs/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kjs5.1
/usr/share/man/ca@valencia/man1/kjs5.1
/usr/share/man/de/man1/kjs5.1
/usr/share/man/es/man1/kjs5.1
/usr/share/man/fr/man1/kjs5.1
/usr/share/man/it/man1/kjs5.1
/usr/share/man/man1/kjs5.1
/usr/share/man/nl/man1/kjs5.1
/usr/share/man/pt/man1/kjs5.1
/usr/share/man/pt_BR/man1/kjs5.1
/usr/share/man/sv/man1/kjs5.1
/usr/share/man/uk/man1/kjs5.1
