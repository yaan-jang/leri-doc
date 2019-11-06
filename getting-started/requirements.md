# Requirements

If you are not in sudoers, then you can still install leri without root access. Firstly, you are required to install the dependencies step by step.

{% hint style="info" %}
NOT support Boost Library 1.70+
{% endhint %}

## Unix-like system

```
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
      build-essential \
      libgflags-dev \
      libgoogle-glog-dev \
      libomp-dev \
      libhdf5-dev \
      libeigen3-dev \
      libbz2-dev

```

## Mac OSX

We highly recommend using the [Homebrew](http://brew.sh/) package manager to install the dependencies.

```
brew install -vd cmake gflags glog boost
brew install zlib bzip2
```

## Step-by-step

### GCC

Sometimes, on an old UNIX-like distribution,  a new version of `gcc` is required \(i.e. utilize the features from `C++11` standard\) before installing other dependencies. Don't worry, here is how you can compile your own `gcc` on the distribution with/without root access.

```
#! /bin/bash
set -e
#-----------------------------------------------------------------------------
# This script, as part of Leri Analytics, will download packages, configure, 
# build and install GCC, Make, Cmake on Unix-like systems. Customize the 
# variables (GCC_VERSION, MAKE_VERSION, etc.) before running.
# Copyright@2017, Leri Analytics
# Email: yaan.jang@gmail.com
#-----------------------------------------------------------------------------

# Path where to install without root
LOCAL_PATH=/home/<username>/local

# Customize the versions
PARALLEL_MAKE=-j128
GCC_VERSION=gcc-6.3.0
MPFR_VERSION=mpfr-3.1.5
GMP_VERSION=gmp-6.1.2
MPC_VERSION=mpc-1.0.3
MAKE_VERSION=make-4.2
CMAKE_VERSION=cmake-3.12.2

# Creat a directory
if [ ! -f leri-gnu ]; then
  mkdir -p leri-gnu
else
  rm -rf leri-gnu
fi
cd leri-gnu/


# Download packages, maybe you already have the packages, please put them in the directory <leri-gnu>
export http_proxy=$HTTP_PROXY https_proxy=$HTTP_PROXY ftp_proxy=$HTTP_PROXY
wget -nc https://ftp.gnu.org/gnu/gmp/$GMP_VERSION.tar.xz
wget -nc https://ftp.gnu.org/gnu/mpfr/$MPFR_VERSION.tar.xz
wget -nc https://ftp.gnu.org/gnu/mpc/$MPC_VERSION.tar.gz
wget -nc https://ftp.gnu.org/gnu/gcc/$GCC_VERSION/$GCC_VERSION.tar.gz
wget -nc http://ftp.gnu.org/gnu/make/$MAKE_VERSION.tar.gz
wget -nc https://cmake.org/files/v3.12/cmake-3.12.2.tar.gz

# Extract Packages
echo "Extracting tar files ..."
for f in *.tar*; do tar xfk $f; done

# Step 1. Install GMP
echo "Step 1. Installing GMP ..."
cd $GMP_VERSION
mkdir build && cd build
../configure --prefix=$LOCAL_PATH/$GMP_VERSION --enable-cxx
nice -n 19 time make $PARALLEL_MAKE
make install && make check
cd ../..

# Step 2. Install MPFR
echo "Step 2. Installing MPFR ..."
cd $MPFR_VERSION
mkdir build && cd build
../configure --prefix=$LOCAL_PATH/$MPFR_VERSION --with-gmp=$LOCAL_PATH/$GMP_VERSION 
nice -n 19 time make $PARALLEL_MAKE
make install && make check
cd ../..

# Step 3. Install MPC
echo "Step 3. Installing MPC ..."
cd $MPC_VERSION
mkdir build && cd build
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib \
../configure --prefix=$LOCAL_PATH/$MPC_VERSION \
--with-gmp=$LOCAL_PATH/$GMP_VERSION \
--with-mpfr=$LOCAL_PATH/$MPFR_VERSION
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib \
nice -n 19 time make $PARALLEL_MAKE
make install && make check
cd ../..

# Step 4. Install GCC
echo "Step 4. Installing GCC ..."
cd $GCC_VERSION
mkdir -p build && cd build
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib \
../configure --prefix=$LOCAL_PATH/$GCC_VERSION \
--with-gmp=$LOCAL_PATH/$GMP_VERSION \
--with-mpfr=$LOCAL_PATH/$MPFR_VERSION \
--with-mpc=$LOCAL_PATH/$MPC_VERSION \
--disable-multilib \
--enable-languages=c,c++ \
--enable-libgomp
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib \
nice -n 19 time make $PARALLEL_MAKE
make install && make check
cd ../..

## Step 5. Install Make
#echo "Step 5. Installing Make ..."
#cd $MAKE_VERSION
#mkdir -p build && cd build
#LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib \
#../configure --prefix=$LOCAL_PATH/$MAKE_VERSION
#LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib \
#nice -n 19 time make $PARALLEL_MAKE
#make install && make check
#cd ../..

## Step 6. Install Make
#echo "Step 6. Installing Cmake ..."
#cd $CMAKE_VERSION
#mkdir -p build && cd build
#LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib64:$LOCAL_PATH/$MAKE_VERSION/lib \
#../configure --prefix=$LOCAL_PATH/$CMAKE_VERSION
#LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib64:$LOCAL_PATH/$MAKE_VERSION/lib \
#nice -n 19 time make $PARALLEL_MAKE
#make install && make check
#cd ../..

## echo $MACHTYPE
##$LOCAL_PATH/$GCC_VERSION/lib64 is correct on x86_64; it may need to be replaced with $LOCAL_PATH/$GCC_VERSION/lib on other platforms.
## Or paste the following lines to ~/.bashrc in Unix-like systems
export LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib64:$LOCAL_PATH/$MAKE_VERSION/lib:$LOCAL_PATH/$CMAKE_VERSION/lib
export PATH=$LOCAL_PATH/$GCC_VERSION/bin:$PATH
#export PATH=$LOCAL_PATH/$MAKE_VERSION/bin:$PATH
#export PATH=$LOCAL_PATH/$CMAKE_VERSION/bin:$PATH
```

### Make

If the version of `gcc` is not too old on your distribution, you can just simply install the `make` as follows,

```
wget -nc https://ftp.gnu.org/gnu/make/make-4.2.tar.gz
tar -xzvf make-4.2.tar.gz
./configure --prefix=/home/<username>/local
make
make install
```

If you compile your `gcc` own , then you are recommanded \(as shown above in step 5, just uncomment the lines\) to run as follows, 

```
## Step 5. Install Make
# echo "Step 5. Installing Make ..."
cd $MAKE_VERSION
mkdir -p build && cd build
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib \
../configure --prefix=$LOCAL_PATH/$MAKE_VERSION
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib \
nice -n 19 time make $PARALLEL_MAKE
make install && make check
cd ../..
# !important, add the line into ~/.bashrc
export PATH=$LOCAL_PATH/$MAKE_VERSION/bin:$PATH
```

### Cmake

```
wget -nc https://cmake.org/files/v3.12/cmake-3.12.2.tar.gz
tar -xvf cmake-3.12.2.tar.gz
cd cmake-3.12.2
./configure --prefix=/home/<username>/local/
make && make install 
cmake --version 
```

Or install `cmake` by following lines if you compile your own `gcc` 

```
## Step 6. Install Make
#echo "Step 6. Installing Cmake ..."
cd $CMAKE_VERSION
mkdir -p build && cd build
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib64:$LOCAL_PATH/$MAKE_VERSION/lib \
../configure --prefix=$LOCAL_PATH/$CMAKE_VERSION
LD_LIBRARY_PATH=$LOCAL_PATH/$GMP_VERSION/lib:$LOCAL_PATH/$MPFR_VERSION/lib:$LOCAL_PATH/$MPC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib:$LOCAL_PATH/$GCC_VERSION/lib64:$LOCAL_PATH/$MAKE_VERSION/lib \
nice -n 19 time make $PARALLEL_MAKE
make install && make check
cd ../..

# !important, add the line into ~/.bashrc
export PATH=$LOCAL_PATH/$CMAKE_VERSION/bin:$PATH
```

### Boost library

On Unix-like system, it is easy to install Boost library with sudo, type the following command in the terminal to install Boost library. 

```
apt-get install libboost-all-dev
```

If you would like to install the Boost library without root, you can follow this instruction to install it. 

```
wget -nc https://dl.bintray.com/boostorg/release/1.65.0/source/boost_1_65_0.tar.gz
tar -xvzf boost_1_65_0.tar.gz
cd boost_1_65_0                                             
./bootstrap.sh \
--libdir=/home/<username>/local/lib \
--includedir=/home/<username>/local/include
./b2                                                             
./b2 install  
```

### Gflags 

The `gflags` package contains a C++ library that implements command line flags processing.

{% hint style="warning" %}
The latest version of `gflags` is not validated for the Leri software.
{% endhint %}

```
wget -nc https://github.com/gflags/gflags/archive/v2.2.2.tar.gz
cd gflags
mkdir build
cd build
# ccmake # edit the prefix to /home/username/local, and type c
# or
cmake CMAKE_INSTALL_PREFIX=/home/username/local ..
vi CMakeCache.txt # edit CMAKE_CXX_FLAGS:STRING=-fPIC
make 
make install DESTDIR=/home/bioc1657/local
```

### Glog

The `glog` library contains a C++ implementation of the Google logging module.

{% hint style="warning" %}
The latest version of `glog` is not validated for the Leri software.
{% endhint %}

```
wget -nc https://github.com/google/glog/archive/v0.4.0.tar.gz
tar -xvzf *.tar.gz
./configure --prefix=/home/username/local
make 
make install
```

### Plotting

If one would like to run leri with figures, plotting packages are required to install. Gnuplot and R are two packages to generate figures. 

```
$ sudo apt install r-base gnuplot
```

Then, install library `circlize` as follows,

```
install.packages("circlize")
```

Install Gnuplot in the terminal as follows,

```
$ sudo apt install gnuplot
```

