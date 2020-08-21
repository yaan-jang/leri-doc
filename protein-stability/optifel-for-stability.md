# OptiFel for stability

#### How to use OptiFel

Train the OptiFel as follows,

```text
leri optifel \
-phase 0 \          # for training
-dirt <DIRECTORY> \ # that contains the training data
-nrule 3 \          # number of fuzzy rules
-max_iter 5000 \    # number of maximum iterations
-echo 50 \          # number of echoes
-threads 4 \        # number of threads
-output <DIRECTORY> # optional, where to output the results
```

Prediction

```text
leri optifel \
-phase 1 \              # for prediction
-dirt <DIRECTORY> \     # that contains the data for prediction
-nrule 3 \              # number of rules
-param <PARAMETER FILE> # the parameter file for the trained optifel model
-output <DIRECTORY>     # optional, where to output the results 
```

#### 



