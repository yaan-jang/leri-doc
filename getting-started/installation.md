# Installation

### Pre-built distribution

Please go [here](https://kornmann.bioch.ox.ac.uk/leri/resources/download.html) to download pre-built distributions.

### Build Leri from source code

```bash
# For internal use ONLY
mkdir build && cd build
cmake \
-DCMAKE_BUILD_TYPE=Release \
-DUSE_CCACHE=ON \
-DUSE_PLOT=ON \
-DUSE_PYMOL=ON \
-DUSE_TORCH=ON \
-DUSE_OPENMP=ON \
..
make
make install
```
