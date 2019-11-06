---
description: >-
  Here, we provide a bash script to install leri and its major dependencies. If
  any other dependencies are required, one can customize the installation
  functions from the existing functions as used.
---

# All-in-one installation

    # Copyright 2019 by yaan.jang@gmail.com

    #-------------------------------------------------------------------------------------------
    # This script will download packages for, configure, 
    # build and install a Leri software without root 
    # permission. Customize the variables (SCRATCH_DIRT, 
    # LOCAL_INSTALL_DIRT, etc.) to your liking before running.
    # Tested on: Debina 9
    #
    # See: https://leri.gitbook.io/doc/
    #-------------------------------------------------------------------------------------------

    # Dependencies:
    # - cmake
    # - gflags
    # - glog
    # - boost

    LOCAL_INSTALL_DIRT=${HOME}/local
    LERI_INSTALL_DIRT=${LOCAL_INSTALL_DIRT}/leri
    SCRATCH_DIRT=${HOME}/scratch_for_packages

    LERI_GPU=OFF
    CMAKE_VERSION_MAJOR=3.12
    CMAKE_VERSION_MINOR=2
    GFLAGS_VERSION="2.2.2"
    GLOG_VERSION="0.4.0"
    BOOST_VERSION="1.65.0"

    CMAKE_LINK="https://cmake.org/files/v${CMAKE_VERSION_MAJOR}/cmake-${CMAKE_VERSION_MAJOR}.${CMAKE_VERSION_MINOR}.tar.gz"
    GFLAGS_LINK="https://github.com/gflags/gflags/archive/v${GFLAGS_VERSION}.tar.gz"
    GLOG_LINK="https://github.com/google/glog/archive/v${GLOG_VERSION}.tar.gz"
    BOOST_LINK="https://dl.bintray.com/boostorg/release/${BOOST_VERSION}/source/boost_`echo ${BOOST_VERSION} | sed "s/\./_/g"`.tar.gz"


    # Make a local installation directory
    if [ ! -f ${LOCAL_INSTALL_DIRT} ]; then
      mkdir -p ${LOCAL_INSTALL_DIRT}
    fi
    set -e

    untar_to_dirt() {
      tar xzvf ${1} --strip-components=1
    }

    scratch_init() {
      if [ ! -f ${SCRATCH_DIRT} ]; then
        mkdir -p ${SCRATCH_DIRT}
      fi 
      cd "${SCRATCH_DIRT}"
      mkdir -p "$1"
      cd "$1"
    }

    install_cmake() {
      scratch_init cmake
      wget -nc -q ${CMAKE_LINK}
      untar_to_dirt "cmake-*.tar.gz"
      ./configure --prefix=${LOCAL_INSTALL_DIRT}
      make -s
      make install 
      echo "[-- Add the line into your ~/.bashrc"
      echo "[-- export PATH=\$PATH:${LOCAL_INSTALL_DIRT}/${CMAKE_VERSION_MAJOR}/bin"
    }

    install_gflags() {
      scratch_init gflags
      wget -nc -q ${GFLAGS_LINK}
      untar_to_dirt "v${GFLAGS_VERSION}.tar.gz"
      echo ${SCRATCH_DIRT}/gflags/build
      if [[ ! -d build ]]; then
        mkdir build 
      fi
      cd build
      cmake -D CMAKE_INSTALL_PREFIX="${LOCAL_INSTALL_DIRT}" -D CMAKE_POSITION_INDEPENDENT_CODE=ON ..
      make
      make install
    }

    install_glog() {
      scratch_init glog
      wget -nc -q ${GLOG_LINK}
      untar_to_dirt "v${GLOG_VERSION}.tar.gz"
      ./autogen.sh
      ./configure --prefix="${LOCAL_INSTALL_DIRT}/glog-${GLOG_VERSION}"
      make
      make install
    }

    install_boost() {
      scratch_init boost
      wget -nc -q ${BOOST_LINK}
      untar_to_dirt "boost_*.tar.gz"
      ./bootstrap.sh --prefix="${LOCAL_INSTALL_DIRT}/boost-${BOOST_VERSION}"
      # or 
      # ./bootstrap.sh \
      # --libdir=${LOCAL_INSTALL_DIRT}/lib \
      # --includedir=${LOCAL_INSTALL_DIRT}/include \
      #
      ./b2 install
    }

    install_leri() {
      scratch_init leri
      git clone https://yaan-jang@bitbucket.org/lerianalytics/leri.git
      if [[ ! -d build ]]; then
        mkdir build 
      fi
      cd build
      cmake -DUSE_GPU=${LERI_GPU} -DCMAKE_INSTALL_PREFIX:PATH=${LERI_INSTALL_DIRT} ..
      make
      make install
    }

    echo "[-- Installing cmake ..."
    install_cmake
    echo "[-- Installing gflags ..."
    install_gflags
    echo "[-- Installing glog ..."
    install_glog
    echo "[-- Installing boost ..."
    install_boost
    echo "[-- Installing leri ..."
    install_leri

    echo "[-- Add the line into your ~/.bashrc"
    echo "[-- export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:${LERI_INSTALL_DIRT}/lib"
    echo "[-- export PATH=\$PATH:${LERI_INSTALL_DIRT}/bin"

    # Last thing you may do is to delete the packages
    #rm -rf ${SCRATCH_DIRT}


