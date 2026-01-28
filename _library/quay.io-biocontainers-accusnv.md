---
layout: container
name:  "quay.io/biocontainers/accusnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/accusnv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/accusnv/container.yaml"
updated_at: "2026-01-28 04:22:57.824882"
latest: "1.0.0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/accusnv"
aliases:
 - "accusnv"
 - "accusnv_downstream"
 - "accusnv_snakemake"
 - "gff2gff"
 - "phc"
 - "ref-cache"
 - "roh-viz"
 - "sickle"
 - "vrfs-variances"
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
 - "drawgram"
 - "drawgram_gui"
 - "drawtree"
 - "drawtree_gui"
 - "fitch"
 - "gendist"
 - "kitsch"
 - "mix"
 - "move"
versions:
 - "1.0.0.3--pyhdfd78af_0"
 - "1.0.0.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for accusnv"
config: {"url": "https://biocontainers.pro/tools/accusnv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for accusnv", "latest": {"1.0.0.5--pyhdfd78af_0": "sha256:c1637f6c3788efcc708eba6f95fd8129b62110627bc028d3da896efee1cbee72"}, "tags": {"1.0.0.3--pyhdfd78af_0": "sha256:1a3e82f198e4ad82616542dee1cbeea4767431ad6e3bd3b558cc9666f06ef793", "1.0.0.5--pyhdfd78af_0": "sha256:c1637f6c3788efcc708eba6f95fd8129b62110627bc028d3da896efee1cbee72"}, "docker": "quay.io/biocontainers/accusnv", "aliases": {"accusnv": "/usr/local/bin/accusnv", "accusnv_downstream": "/usr/local/bin/accusnv_downstream", "accusnv_snakemake": "/usr/local/bin/accusnv_snakemake", "gff2gff": "/usr/local/bin/gff2gff", "phc": "/usr/local/bin/phc", "ref-cache": "/usr/local/bin/ref-cache", "roh-viz": "/usr/local/bin/roh-viz", "sickle": "/usr/local/bin/sickle", "vrfs-variances": "/usr/local/bin/vrfs-variances", "DrawGram.jar": "/usr/local/bin/DrawGram.jar", "DrawTree.jar": "/usr/local/bin/DrawTree.jar", "clique": "/usr/local/bin/clique", "consense": "/usr/local/bin/consense", "contml": "/usr/local/bin/contml", "contrast": "/usr/local/bin/contrast", "dnacomp": "/usr/local/bin/dnacomp", "dnadist": "/usr/local/bin/dnadist", "dnainvar": "/usr/local/bin/dnainvar", "dnaml": "/usr/local/bin/dnaml", "dnamlk": "/usr/local/bin/dnamlk", "dnamove": "/usr/local/bin/dnamove", "dnapenny": "/usr/local/bin/dnapenny", "dollop": "/usr/local/bin/dollop", "dolmove": "/usr/local/bin/dolmove", "dolpenny": "/usr/local/bin/dolpenny", "drawgram": "/usr/local/bin/drawgram", "drawgram_gui": "/usr/local/bin/drawgram_gui", "drawtree": "/usr/local/bin/drawtree", "drawtree_gui": "/usr/local/bin/drawtree_gui", "fitch": "/usr/local/bin/fitch", "gendist": "/usr/local/bin/gendist", "kitsch": "/usr/local/bin/kitsch", "mix": "/usr/local/bin/mix", "move": "/usr/local/bin/move"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/accusnv.
singularity registry hpc automated addition for accusnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/accusnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/accusnv:1.0.0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/accusnv/1.0.0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/accusnv/1.0.0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### accusnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### accusnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### accusnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### accusnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### accusnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### accusnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### accusnv

```bash
$ singularity exec <container> /usr/local/bin/accusnv
$ podman run --it --rm --entrypoint /usr/local/bin/accusnv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accusnv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accusnv_downstream

```bash
$ singularity exec <container> /usr/local/bin/accusnv_downstream
$ podman run --it --rm --entrypoint /usr/local/bin/accusnv_downstream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accusnv_downstream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accusnv_snakemake

```bash
$ singularity exec <container> /usr/local/bin/accusnv_snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/accusnv_snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accusnv_snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff

```bash
$ singularity exec <container> /usr/local/bin/gff2gff
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phc

```bash
$ singularity exec <container> /usr/local/bin/phc
$ podman run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roh-viz

```bash
$ singularity exec <container> /usr/local/bin/roh-viz
$ podman run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sickle

```bash
$ singularity exec <container> /usr/local/bin/sickle
$ podman run --it --rm --entrypoint /usr/local/bin/sickle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sickle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vrfs-variances

```bash
$ singularity exec <container> /usr/local/bin/vrfs-variances
$ podman run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### drawgram

```bash
$ singularity exec <container> /usr/local/bin/drawgram
$ podman run --it --rm --entrypoint /usr/local/bin/drawgram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawgram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawgram_gui

```bash
$ singularity exec <container> /usr/local/bin/drawgram_gui
$ podman run --it --rm --entrypoint /usr/local/bin/drawgram_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawgram_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawtree

```bash
$ singularity exec <container> /usr/local/bin/drawtree
$ podman run --it --rm --entrypoint /usr/local/bin/drawtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawtree_gui

```bash
$ singularity exec <container> /usr/local/bin/drawtree_gui
$ podman run --it --rm --entrypoint /usr/local/bin/drawtree_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawtree_gui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fitch

```bash
$ singularity exec <container> /usr/local/bin/fitch
$ podman run --it --rm --entrypoint /usr/local/bin/fitch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fitch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gendist

```bash
$ singularity exec <container> /usr/local/bin/gendist
$ podman run --it --rm --entrypoint /usr/local/bin/gendist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gendist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kitsch

```bash
$ singularity exec <container> /usr/local/bin/kitsch
$ podman run --it --rm --entrypoint /usr/local/bin/kitsch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kitsch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mix

```bash
$ singularity exec <container> /usr/local/bin/mix
$ podman run --it --rm --entrypoint /usr/local/bin/mix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### move

```bash
$ singularity exec <container> /usr/local/bin/move
$ podman run --it --rm --entrypoint /usr/local/bin/move   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/move   -v ${PWD} -w ${PWD} <container> -c " $@"
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