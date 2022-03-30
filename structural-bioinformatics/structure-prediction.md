# Structure prediction

### Training

```
amo semer3d \
-train \
-dirt training_data/ \
-index training_data/index_list \
-mbs 128 \
-echo 20000 \
-threads 8
# Checkpoint
# -param /path_to_pre_trained_model/XXXXX.pt
```

### Prediction

```
amo semer3d \
-param /path_to_pre_trained_model/XXXXX.pt \
-n MAXIMUM_LENGTH \
-fastx XXXXX.fasta
```

### Case study

![The Vps13 contains 3144 amino acids. (Vps13, YLL040C, Yeast)](../.gitbook/assets/vps13\_3144aa\_predicted.png)

More examples can be found at [this link](https://kornmann.bioch.ox.ac.uk/leri/resources/predict\_struct.html).

