# Installation

### Compile and install Leri

```bash
# For internal use ONLY
mkdir build && cd build
cmake \
-DCMAKE_BUILD_TYPE=Release \
-DBoost_NO_SYSTEM_PATHS=TRUE \
-DBoost_NO_BOOST_CMAKE=TRUE \
-DBoost_ROOT=/home/<username>/local/include \
-DBoost_LIBRARY_DIRS:FILEPATH=/home/<username>/local/lib \
..
make
make install
```
