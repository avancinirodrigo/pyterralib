#!/bin/bash

if [ "$_PYTERRALIB_ROOT_DIR" == "" ]; then
  _PYTERRALIB_ROOT_DIR="/home/dev/pyterralib"
fi
export _PYTERRALIB_ROOT_DIR="$_PYTERRALIB_ROOT_DIR"
echo "pyTerraLib root dir $_PYTERRALIB_ROOT_DIR"

if [ "$_PYTERRALIB_GIT_DIR" == "" ]; then
  _PYTERRALIB_GIT_DIR="$_PYTERRALIB_ROOT_DIR/git/pyterralib"
fi
export _PYTERRALIB_GIT_DIR="$_PYTERRALIB_GIT_DIR"
echo "pyTerraLib git dir $_PYTERRALIB_GIT_DIR"

if [ "$_PYTERRALIB_BUILD_DIR" == "" ]; then
  _PYTERRALIB_BUILD_DIR=$_PYTERRALIB_ROOT_DIR/solution
fi
export _PYTERRALIB_BUILD_DIR="$_PYTERRALIB_BUILD_DIR"
echo "pyTerraLib building dir $_PYTERRALIB_BUILD_DIR"


if [ "$_TERRALIB_ROOT_DIR" == "" ]; then
  _TERRALIB_ROOT_DIR="$_PYTERRALIB_ROOT_DIR/terralib"
fi
export _TERRALIB_ROOT_DIR="$_TERRALIB_ROOT_DIR"

if [ "$_TERRALIB_3RDPARTY_DIR" == "" ]; then
  _TERRALIB_3RDPARTY_DIR="$_TERRALIB_ROOT_DIR/3rdparty"
fi
export _TERRALIB_3RDPARTY_DIR="$_TERRALIB_3RDPARTY_DIR"
echo "TerraLib 3rd party dir $_TERRALIB_3RDPARTY_DIR"

if [ "$_TERRALIB_3RDPARTY_LIBS_DIR" == "" ]; then
  _TERRALIB_3RDPARTY_LIBS_DIR="$_TERRALIB_3RDPARTY_DIR/libs"
fi
export _TERRALIB_3RDPARTY_LIBS_DIR="$_TERRALIB_3RDPARTY_LIBS_DIR"
echo "TerraLib 3rd party install dir $_TERRALIB_3RDPARTY_LIBS_DIR"

if [ "$_TERRALIB_SOLUTION_DIR" == "" ]; then
  _TERRALIB_SOLUTION_DIR=$_TERRALIB_ROOT_DIR/solution
fi
export _TERRALIB_SOLUTION_DIR="$_TERRALIB_SOLUTION_DIR"
echo "TerraLib solution dir $_TERRALIB_SOLUTION_DIR"

if [ "$_TERRALIB_INSTALL_DIR" == "" ]; then
  _TERRALIB_INSTALL_DIR=$_TERRALIB_SOLUTION_DIR/install
fi
export _TERRALIB_INSTALL_DIR="$_TERRALIB_INSTALL_DIR"
echo "TerraLib install dir $_TERRALIB_INSTALL_DIR"

if [ "$_TERRALIB_BUILD_DIR" == "" ]; then
  _TERRALIB_BUILD_DIR=$_TERRALIB_SOLUTION_DIR/build
fi
export _TERRALIB_BUILD_DIR="$_TERRALIB_BUILD_DIR"
echo "TerraLib building dir $_TERRALIB_BUILD_DIR"

if [ "$_TERRALIB_GIT_DIR" == "" ]; then
  _TERRALIB_GIT_DIR="$_TERRALIB_ROOT_DIR/git/terralib"
fi
export _TERRALIB_GIT_DIR="$_TERRALIB_GIT_DIR"
echo "TerraLib git dir $_TERRALIB_GIT_DIR"

git clone -b python3-release-5.5 https://gitlab.dpi.inpe.br/rodrigo.avancini/terralib.git $_TERRALIB_GIT_DIR
mkdir -p $_TERRALIB_3RDPARTY_DIR
cd $_TERRALIB_3RDPARTY_DIR
wget -nc http://www.dpi.inpe.br/terralib5-devel/3rdparty/src/5.5/terralib-3rdparty-linux-ubuntu-18.04.tar.gz  
cp $_TERRALIB_GIT_DIR/install/install-3rdparty-linux-ubuntu-18.04.sh .
TERRALIB_DEPENDENCIES_DIR="$_TERRALIB_3RDPARTY_LIBS_DIR" ./install-3rdparty-linux-ubuntu-18.04.sh 

mkdir -p $_TERRALIB_SOLUTION_DIR
cd $_TERRALIB_SOLUTION_DIR
mkdir -p $_TERRALIB_BUILD_DIR
cd $_TERRALIB_BUILD_DIR

cmake -G "Unix Makefiles" -C $_PYTERRALIB_GIT_DIR/build/cmake/terralib-build-conf.cmake $_TERRALIB_GIT_DIR/build/cmake
cmake --build . --target install --config Release 

cd $_PYTERRALIB_BUILD_DIR
mkdir -p terralib

cp $_TERRALIB_INSTALL_DIR/bindings/python/terralib/* terralib
rm -rf terralib/__init__.py
cp $_PYTERRALIB_GIT_DIR/__init__.py terralib

cp $_TERRALIB_INSTALL_DIR/lib/*.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_locale.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_regex.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_filesystem.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_system.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_log.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_log_setup.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_thread.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_thread.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libboost_date_time.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libgeos-*.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libxerces-*.so* terralib
cp $_TERRALIB_3RDPARTY_LIBS_DIR/lib/libproj*.so* terralib

ln -sf $_PYTERRALIB_GIT_DIR/setup.py .
