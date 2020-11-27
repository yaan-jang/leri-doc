# FAQs

## How to build a stand-alone package?

#### Gflags

```text
wget -nc https://github.com/gflags/gflags/archive/v2.2.2.tar.gz -P ${dirt_package}/
cd ${dirt_package}
tar xzf v2.2.2.tar.gz
cd gflags-2.2.2
mkdir build && cd build
# # ccmake # edit the prefix to /home/username/local, and type c
# # or
# cmake CMAKE_INSTALL_PREFIX=/home/<username>/local ..
# vi CMakeCache.txt # edit CMAKE_CXX_FLAGS:STRING=-fPIC
# make 
# make install DESTDIR=/home/<username>/local

# echo ${CMAKE_VARS_DEFINE}
cmake .. ${CMAKE_VARS_DEFINE} \
-G "Unix Makefiles" \
-DCMAKE_INSTALL_PREFIX=${GFLAGS_INSTALL_PATH} \
-DBUILD_SHARED_LIBS=OFF \
-DBUILD_STATIC_LIBS=ON \
-DBUILD_gflags_LIB=ON\
-DINSTALL_STATIC_LIBS=ON \
-DINSTALL_SHARED_LIBS=OFF \
-DREGISTER_INSTALL_PREFIX=OFF
make clean
make -j ${parallel} install
```

#### Glog

```text
wget -nc https://github.com/google/glog/archive/v0.4.0.tar.gz -P ${dirt_package}/
cd ${dirt_package}
tar -xzf v0.4.0.tar.gz
cd glog-0.4.0
if [ ! -d "build" ]; then mkdir build; fi && cd build
gflags_DIR=${GFLAGS_INSTALL_PATH}/lib/cmake/gflags
cmake .. ${CMAKE_VARS_DEFINE} \
-G "Unix Makefiles" \
-DCMAKE_INSTALL_PREFIX=${GLOG_INSTALL_PATH} \
-Dgflags_DIR=${gflags_DIR} \
-DBUILD_SHARED_LIBS=OFF
make clean
make -j ${parallel} install
```

#### Bzip

```text
wget --no-check-certificate https://github.com/LuaDist/bzip2/archive/1.0.5.zip -O ${dirt_package}/bzip2-1.0.5.zip
cd ${dirt_package}/
unzip bzip2-1.0.5.zip
cd ${dirt_package}/bzip2-1.0.5
# Modify
# sed -i -r 's:^\s*#\s*include\s*<sys\\stat.h>\s*$:\n#   include <sys/stat.h>:g' \
# ${dirt_package}/bzip2-1.0.5/bzip2.c
sed -i -r 's/(^\s*ADD_LIBRARY\s*\(\s*bz2\s*)SHARED/# Remove SHARED\n\1/g' \
${dirt_package}/bzip2-1.0.5/CMakeLists.txt

if [ ! -d "build" ]; then mkdir build; fi && cd build
cmake .. $CMAKE_VARS_DEFINE \
-G "Unix Makefiles" \
-DCMAKE_INSTALL_PREFIX=${BZIP2_INSTALL_PATH} \
-DBUILD_SHARED_LIBS=OFF 
make -j ${parallel} install
```

