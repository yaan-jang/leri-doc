# Requirements

If you are not in sudoers, then you can still install leri without root access. Firstly, you are required to install the dependencies step by step

## Dependencies

### GCC

### Make

```bash
wget make*.tar.gz
./configure --prefix=/home/<username>/local
make -j8
make install
```

### Cmake

```bash
wget https://cmake.org/files/v3.11/cmake-3.11.1.tar.gz
tar -xvf cmake-3.10.0-rc1.tar.gz
cd cmake-3.11.1*
./configure --prefix=/home/<username>/local/
make && make install 
cmake --version 
```

### Boost 

```bash
cd boost_1_57_0/                                                 
./bootstrap.sh --libdir=/home/<username>/local/lib --includedir=/home/<username>/local/include                                                                
vi project-config.jam # edit python path if you have a compiled one
./b2                                                             
./b2 install  
```

### Gflags

```bash
cd gflags
mkdir build
cd build
ccmake .. # edit the prefix to /home/username/local, and type c
vi CMakeCache.txt # edit CMAKE_CXX_FLAGS:STRING=-fPIC
make 
make install
```

### Glog

```bash
./configure --prefix=/home/username/local
make 
make install
```

