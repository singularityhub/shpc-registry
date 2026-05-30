---
layout: container
name:  "quay.io/biocontainers/kleboscope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kleboscope/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kleboscope/container.yaml"
updated_at: "2026-05-30 06:30:44.967524"
latest: "1.0.1--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/kleboscope"
aliases:
 - "bstats"
 - "comppair"
 - "dialign-tx"
 - "ds"
 - "famsa"
 - "kaptive"
 - "kleboscope"
 - "mustang"
 - "pModel"
 - "probcons"
 - "probconsRNA"
 - "proda"
 - "scompare"
 - "strain_ml"
 - "treeshrink"
 - "TMscore"
 - "conus_compare"
 - "conus_train"
 - "sap"
 - "sfold"
 - "abricate"
 - "abricate-get_db"
 - "hmmerbuild"
 - "kalign"
 - "zless"
 - "RNAconsensus"
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
versions:
 - "1.0.1--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_1"
description: "singularity registry hpc automated addition for kleboscope"
config: {"url": "https://biocontainers.pro/tools/kleboscope", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kleboscope", "latest": {"1.0.1--pyhdfd78af_1": "sha256:9617855d820a3bd60d9f7092c2c7a5e89ab854515c85b84a0f5018a715a48526"}, "tags": {"1.0.1--pyhdfd78af_0": "sha256:1970125855baa2110ac9616349eca6f0bc7d85efd596261f9b5be9104c5729ff", "1.0.1--pyhdfd78af_1": "sha256:9617855d820a3bd60d9f7092c2c7a5e89ab854515c85b84a0f5018a715a48526"}, "docker": "quay.io/biocontainers/kleboscope", "aliases": {"bstats": "/usr/local/bin/bstats", "comppair": "/usr/local/bin/comppair", "dialign-tx": "/usr/local/bin/dialign-tx", "ds": "/usr/local/bin/ds", "famsa": "/usr/local/bin/famsa", "kaptive": "/usr/local/bin/kaptive", "kleboscope": "/usr/local/bin/kleboscope", "mustang": "/usr/local/bin/mustang", "pModel": "/usr/local/bin/pModel", "probcons": "/usr/local/bin/probcons", "probconsRNA": "/usr/local/bin/probconsRNA", "proda": "/usr/local/bin/proda", "scompare": "/usr/local/bin/scompare", "strain_ml": "/usr/local/bin/strain_ml", "treeshrink": "/usr/local/bin/treeshrink", "TMscore": "/usr/local/bin/TMscore", "conus_compare": "/usr/local/bin/conus_compare", "conus_train": "/usr/local/bin/conus_train", "sap": "/usr/local/bin/sap", "sfold": "/usr/local/bin/sfold", "abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "hmmerbuild": "/usr/local/bin/hmmerbuild", "kalign": "/usr/local/bin/kalign", "zless": "/usr/local/bin/zless", "RNAconsensus": "/usr/local/bin/RNAconsensus", "DrawGram.jar": "/usr/local/bin/DrawGram.jar", "DrawTree.jar": "/usr/local/bin/DrawTree.jar", "clique": "/usr/local/bin/clique", "consense": "/usr/local/bin/consense", "contml": "/usr/local/bin/contml", "contrast": "/usr/local/bin/contrast", "dnacomp": "/usr/local/bin/dnacomp", "dnadist": "/usr/local/bin/dnadist", "dnainvar": "/usr/local/bin/dnainvar", "dnaml": "/usr/local/bin/dnaml", "dnamlk": "/usr/local/bin/dnamlk", "dnamove": "/usr/local/bin/dnamove", "dnapenny": "/usr/local/bin/dnapenny", "dollop": "/usr/local/bin/dollop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kleboscope.
singularity registry hpc automated addition for kleboscope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kleboscope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kleboscope:1.0.1--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kleboscope/1.0.1--pyhdfd78af_1
$ module help quay.io/biocontainers/kleboscope/1.0.1--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kleboscope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kleboscope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kleboscope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kleboscope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kleboscope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kleboscope-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### kaptive

```bash
$ singularity exec <container> /usr/local/bin/kaptive
$ podman run --it --rm --entrypoint /usr/local/bin/kaptive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaptive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kleboscope

```bash
$ singularity exec <container> /usr/local/bin/kleboscope
$ podman run --it --rm --entrypoint /usr/local/bin/kleboscope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kleboscope   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### scompare

```bash
$ singularity exec <container> /usr/local/bin/scompare
$ podman run --it --rm --entrypoint /usr/local/bin/scompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scompare   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### TMscore

```bash
$ singularity exec <container> /usr/local/bin/TMscore
$ podman run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sap

```bash
$ singularity exec <container> /usr/local/bin/sap
$ podman run --it --rm --entrypoint /usr/local/bin/sap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfold

```bash
$ singularity exec <container> /usr/local/bin/sfold
$ podman run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAconsensus

```bash
$ singularity exec <container> /usr/local/bin/RNAconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
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