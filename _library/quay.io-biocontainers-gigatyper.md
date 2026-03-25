---
layout: container
name:  "quay.io/biocontainers/gigatyper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gigatyper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gigatyper/container.yaml"
updated_at: "2026-03-25 04:49:25.791801"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/gigatyper"
aliases:
 - "RNAconsensus"
 - "TMscore"
 - "bstats"
 - "comppair"
 - "conus_compare"
 - "conus_train"
 - "dialign-tx"
 - "ds"
 - "famsa"
 - "gigatyper"
 - "hmmerbuild"
 - "kalign"
 - "mlst-make_blast_db"
 - "mlst-show_seqs"
 - "mustang"
 - "pModel"
 - "probcons"
 - "probconsRNA"
 - "proda"
 - "sap"
 - "scompare"
 - "sfold"
 - "strain_ml"
 - "treeshrink"
 - "zless"
 - "mlst"
 - "hmmeralign"
 - "opal.jar"
 - "raxml"
 - "run_pasta.py"
 - "run_pasta_gui.py"
 - "run_seqtools.py"
 - "sumlabels"
 - "sumtrees"
 - "DrawGram.jar"
 - "DrawTree.jar"
 - "clique"
 - "consense"
 - "contml"
 - "contrast"
 - "dnacomp"
 - "dnadist"
 - "dnainvar"
 - "dnaml"
 - "dnamlk"
 - "dnamove"
 - "dnapenny"
 - "dollop"
 - "dolmove"
 - "dolpenny"
versions:
 - "1.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for gigatyper"
config: {"url": "https://biocontainers.pro/tools/gigatyper", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gigatyper", "latest": {"1.0.0--hdfd78af_0": "sha256:a78607ad3ef769c53129d91f2efc2d4d463c4fafaad01340b46e64234822b4f1"}, "tags": {"1.0.0--hdfd78af_0": "sha256:a78607ad3ef769c53129d91f2efc2d4d463c4fafaad01340b46e64234822b4f1"}, "docker": "quay.io/biocontainers/gigatyper", "aliases": {"RNAconsensus": "/usr/local/bin/RNAconsensus", "TMscore": "/usr/local/bin/TMscore", "bstats": "/usr/local/bin/bstats", "comppair": "/usr/local/bin/comppair", "conus_compare": "/usr/local/bin/conus_compare", "conus_train": "/usr/local/bin/conus_train", "dialign-tx": "/usr/local/bin/dialign-tx", "ds": "/usr/local/bin/ds", "famsa": "/usr/local/bin/famsa", "gigatyper": "/usr/local/bin/gigatyper", "hmmerbuild": "/usr/local/bin/hmmerbuild", "kalign": "/usr/local/bin/kalign", "mlst-make_blast_db": "/usr/local/bin/mlst-make_blast_db", "mlst-show_seqs": "/usr/local/bin/mlst-show_seqs", "mustang": "/usr/local/bin/mustang", "pModel": "/usr/local/bin/pModel", "probcons": "/usr/local/bin/probcons", "probconsRNA": "/usr/local/bin/probconsRNA", "proda": "/usr/local/bin/proda", "sap": "/usr/local/bin/sap", "scompare": "/usr/local/bin/scompare", "sfold": "/usr/local/bin/sfold", "strain_ml": "/usr/local/bin/strain_ml", "treeshrink": "/usr/local/bin/treeshrink", "zless": "/usr/local/bin/zless", "mlst": "/usr/local/bin/mlst", "hmmeralign": "/usr/local/bin/hmmeralign", "opal.jar": "/usr/local/bin/opal.jar", "raxml": "/usr/local/bin/raxml", "run_pasta.py": "/usr/local/bin/run_pasta.py", "run_pasta_gui.py": "/usr/local/bin/run_pasta_gui.py", "run_seqtools.py": "/usr/local/bin/run_seqtools.py", "sumlabels": "/usr/local/bin/sumlabels", "sumtrees": "/usr/local/bin/sumtrees", "DrawGram.jar": "/usr/local/bin/DrawGram.jar", "DrawTree.jar": "/usr/local/bin/DrawTree.jar", "clique": "/usr/local/bin/clique", "consense": "/usr/local/bin/consense", "contml": "/usr/local/bin/contml", "contrast": "/usr/local/bin/contrast", "dnacomp": "/usr/local/bin/dnacomp", "dnadist": "/usr/local/bin/dnadist", "dnainvar": "/usr/local/bin/dnainvar", "dnaml": "/usr/local/bin/dnaml", "dnamlk": "/usr/local/bin/dnamlk", "dnamove": "/usr/local/bin/dnamove", "dnapenny": "/usr/local/bin/dnapenny", "dollop": "/usr/local/bin/dollop", "dolmove": "/usr/local/bin/dolmove", "dolpenny": "/usr/local/bin/dolpenny"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gigatyper.
singularity registry hpc automated addition for gigatyper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gigatyper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gigatyper:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gigatyper/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/gigatyper/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gigatyper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gigatyper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gigatyper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gigatyper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gigatyper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gigatyper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAconsensus

```bash
$ singularity exec <container> /usr/local/bin/RNAconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMscore

```bash
$ singularity exec <container> /usr/local/bin/TMscore
$ podman run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bstats

```bash
$ singularity exec <container> /usr/local/bin/bstats
$ podman run --it --rm --entrypoint /usr/local/bin/bstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comppair

```bash
$ singularity exec <container> /usr/local/bin/comppair
$ podman run --it --rm --entrypoint /usr/local/bin/comppair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comppair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conus_compare

```bash
$ singularity exec <container> /usr/local/bin/conus_compare
$ podman run --it --rm --entrypoint /usr/local/bin/conus_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conus_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conus_train

```bash
$ singularity exec <container> /usr/local/bin/conus_train
$ podman run --it --rm --entrypoint /usr/local/bin/conus_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conus_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dialign-tx

```bash
$ singularity exec <container> /usr/local/bin/dialign-tx
$ podman run --it --rm --entrypoint /usr/local/bin/dialign-tx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dialign-tx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ds

```bash
$ singularity exec <container> /usr/local/bin/ds
$ podman run --it --rm --entrypoint /usr/local/bin/ds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### famsa

```bash
$ singularity exec <container> /usr/local/bin/famsa
$ podman run --it --rm --entrypoint /usr/local/bin/famsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/famsa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gigatyper

```bash
$ singularity exec <container> /usr/local/bin/gigatyper
$ podman run --it --rm --entrypoint /usr/local/bin/gigatyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gigatyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerbuild

```bash
$ singularity exec <container> /usr/local/bin/hmmerbuild
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kalign

```bash
$ singularity exec <container> /usr/local/bin/kalign
$ podman run --it --rm --entrypoint /usr/local/bin/kalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-make_blast_db

```bash
$ singularity exec <container> /usr/local/bin/mlst-make_blast_db
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-make_blast_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-make_blast_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst-show_seqs

```bash
$ singularity exec <container> /usr/local/bin/mlst-show_seqs
$ podman run --it --rm --entrypoint /usr/local/bin/mlst-show_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst-show_seqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mustang

```bash
$ singularity exec <container> /usr/local/bin/mustang
$ podman run --it --rm --entrypoint /usr/local/bin/mustang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mustang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pModel

```bash
$ singularity exec <container> /usr/local/bin/pModel
$ podman run --it --rm --entrypoint /usr/local/bin/pModel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pModel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### probcons

```bash
$ singularity exec <container> /usr/local/bin/probcons
$ podman run --it --rm --entrypoint /usr/local/bin/probcons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probcons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### probconsRNA

```bash
$ singularity exec <container> /usr/local/bin/probconsRNA
$ podman run --it --rm --entrypoint /usr/local/bin/probconsRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probconsRNA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proda

```bash
$ singularity exec <container> /usr/local/bin/proda
$ podman run --it --rm --entrypoint /usr/local/bin/proda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sap

```bash
$ singularity exec <container> /usr/local/bin/sap
$ podman run --it --rm --entrypoint /usr/local/bin/sap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scompare

```bash
$ singularity exec <container> /usr/local/bin/scompare
$ podman run --it --rm --entrypoint /usr/local/bin/scompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfold

```bash
$ singularity exec <container> /usr/local/bin/sfold
$ podman run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strain_ml

```bash
$ singularity exec <container> /usr/local/bin/strain_ml
$ podman run --it --rm --entrypoint /usr/local/bin/strain_ml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strain_ml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeshrink

```bash
$ singularity exec <container> /usr/local/bin/treeshrink
$ podman run --it --rm --entrypoint /usr/local/bin/treeshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeshrink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst

```bash
$ singularity exec <container> /usr/local/bin/mlst
$ podman run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmeralign

```bash
$ singularity exec <container> /usr/local/bin/hmmeralign
$ podman run --it --rm --entrypoint /usr/local/bin/hmmeralign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmeralign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opal.jar

```bash
$ singularity exec <container> /usr/local/bin/opal.jar
$ podman run --it --rm --entrypoint /usr/local/bin/opal.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml

```bash
$ singularity exec <container> /usr/local/bin/raxml
$ podman run --it --rm --entrypoint /usr/local/bin/raxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_pasta.py

```bash
$ singularity exec <container> /usr/local/bin/run_pasta.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_pasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_pasta.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_pasta_gui.py

```bash
$ singularity exec <container> /usr/local/bin/run_pasta_gui.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_pasta_gui.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_pasta_gui.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_seqtools.py

```bash
$ singularity exec <container> /usr/local/bin/run_seqtools.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_seqtools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels

```bash
$ singularity exec <container> /usr/local/bin/sumlabels
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees

```bash
$ singularity exec <container> /usr/local/bin/sumtrees
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DrawGram.jar

```bash
$ singularity exec <container> /usr/local/bin/DrawGram.jar
$ podman run --it --rm --entrypoint /usr/local/bin/DrawGram.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DrawGram.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DrawTree.jar

```bash
$ singularity exec <container> /usr/local/bin/DrawTree.jar
$ podman run --it --rm --entrypoint /usr/local/bin/DrawTree.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DrawTree.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clique

```bash
$ singularity exec <container> /usr/local/bin/clique
$ podman run --it --rm --entrypoint /usr/local/bin/clique   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clique   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consense

```bash
$ singularity exec <container> /usr/local/bin/consense
$ podman run --it --rm --entrypoint /usr/local/bin/consense   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consense   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contml

```bash
$ singularity exec <container> /usr/local/bin/contml
$ podman run --it --rm --entrypoint /usr/local/bin/contml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contrast

```bash
$ singularity exec <container> /usr/local/bin/contrast
$ podman run --it --rm --entrypoint /usr/local/bin/contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnacomp

```bash
$ singularity exec <container> /usr/local/bin/dnacomp
$ podman run --it --rm --entrypoint /usr/local/bin/dnacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadist

```bash
$ singularity exec <container> /usr/local/bin/dnadist
$ podman run --it --rm --entrypoint /usr/local/bin/dnadist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnainvar

```bash
$ singularity exec <container> /usr/local/bin/dnainvar
$ podman run --it --rm --entrypoint /usr/local/bin/dnainvar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnainvar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnaml

```bash
$ singularity exec <container> /usr/local/bin/dnaml
$ podman run --it --rm --entrypoint /usr/local/bin/dnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnamlk

```bash
$ singularity exec <container> /usr/local/bin/dnamlk
$ podman run --it --rm --entrypoint /usr/local/bin/dnamlk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnamlk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnamove

```bash
$ singularity exec <container> /usr/local/bin/dnamove
$ podman run --it --rm --entrypoint /usr/local/bin/dnamove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnamove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnapenny

```bash
$ singularity exec <container> /usr/local/bin/dnapenny
$ podman run --it --rm --entrypoint /usr/local/bin/dnapenny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnapenny   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dollop

```bash
$ singularity exec <container> /usr/local/bin/dollop
$ podman run --it --rm --entrypoint /usr/local/bin/dollop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dollop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dolmove

```bash
$ singularity exec <container> /usr/local/bin/dolmove
$ podman run --it --rm --entrypoint /usr/local/bin/dolmove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dolmove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dolpenny

```bash
$ singularity exec <container> /usr/local/bin/dolpenny
$ podman run --it --rm --entrypoint /usr/local/bin/dolpenny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dolpenny   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)