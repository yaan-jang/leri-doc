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
