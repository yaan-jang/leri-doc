# Lipidomics

Based on `Leri`, one can easily employ the [t-SNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding) to analyze her/his high-dimensional data and get the interactive plotting. 

```text
leri stats_tsne \
-mat <the_data_in_CSV_format> \
-output <user_defined> \
-jobname <user_defined>
```

The recognized format of CSV is shown below,

```markup
#sample, column 1, column2, ..., column i, ..., column N
name 1, 1.0, 1.0, ..., 1.0, ..., 1.0
name 2, 1.0, 1.0, ..., 1.0, ..., 1.0
.
.
.
name M, 1.0, 1.0, ..., 1.0, ..., 1.0
```

As shown above, the first line MUST starts with "\#".

