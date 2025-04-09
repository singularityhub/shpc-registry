---
layout: container
name:  "quay.io/biocontainers/fargene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fargene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fargene/container.yaml"
updated_at: "2025-04-09 03:17:17.382115"
latest: "0.1--py27h21c881e_4"
container_url: "https://biocontainers.pro/tools/fargene"
aliases:
 - "ORFfinder"
 - "fargene"
 - "fargene_model_creation"
 - "pick_long_reads"
 - "trim_galore"
 - "clustalo"
 - "_aaindexextract"
 - "_abiview"
 - "_acdc"
 - "_acdpretty"
 - "_acdtable"
 - "_acdtrace"
 - "_acdvalid"
 - "_antigenic"
 - "_backtranambig"
versions:
 - "0.1--py27h21c881e_4"
description: "shpc-registry automated BioContainers addition for fargene"
config: {"url": "https://biocontainers.pro/tools/fargene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fargene", "latest": {"0.1--py27h21c881e_4": "sha256:77f944a47472696df2dc5b316fdd2a7a36135fbf64fea6d3360eb873abff478a"}, "tags": {"0.1--py27h21c881e_4": "sha256:77f944a47472696df2dc5b316fdd2a7a36135fbf64fea6d3360eb873abff478a"}, "docker": "quay.io/biocontainers/fargene", "aliases": {"ORFfinder": "/usr/local/bin/ORFfinder", "fargene": "/usr/local/bin/fargene", "fargene_model_creation": "/usr/local/bin/fargene_model_creation", "pick_long_reads": "/usr/local/bin/pick_long_reads", "trim_galore": "/usr/local/bin/trim_galore", "clustalo": "/usr/local/bin/clustalo", "_aaindexextract": "/usr/local/bin/_aaindexextract", "_abiview": "/usr/local/bin/_abiview", "_acdc": "/usr/local/bin/_acdc", "_acdpretty": "/usr/local/bin/_acdpretty", "_acdtable": "/usr/local/bin/_acdtable", "_acdtrace": "/usr/local/bin/_acdtrace", "_acdvalid": "/usr/local/bin/_acdvalid", "_antigenic": "/usr/local/bin/_antigenic", "_backtranambig": "/usr/local/bin/_backtranambig"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fargene.
shpc-registry automated BioContainers addition for fargene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fargene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fargene:0.1--py27h21c881e_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fargene/0.1--py27h21c881e_4
$ module help quay.io/biocontainers/fargene/0.1--py27h21c881e_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fargene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fargene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fargene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fargene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fargene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fargene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ORFfinder

```bash
$ singularity exec <container> /usr/local/bin/ORFfinder
$ podman run --it --rm --entrypoint /usr/local/bin/ORFfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ORFfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fargene

```bash
$ singularity exec <container> /usr/local/bin/fargene
$ podman run --it --rm --entrypoint /usr/local/bin/fargene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fargene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fargene_model_creation

```bash
$ singularity exec <container> /usr/local/bin/fargene_model_creation
$ podman run --it --rm --entrypoint /usr/local/bin/fargene_model_creation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fargene_model_creation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pick_long_reads

```bash
$ singularity exec <container> /usr/local/bin/pick_long_reads
$ podman run --it --rm --entrypoint /usr/local/bin/pick_long_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pick_long_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_galore

```bash
$ singularity exec <container> /usr/local/bin/trim_galore
$ podman run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/_aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _abiview

```bash
$ singularity exec <container> /usr/local/bin/_abiview
$ podman run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdc

```bash
$ singularity exec <container> /usr/local/bin/_acdc
$ podman run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdpretty

```bash
$ singularity exec <container> /usr/local/bin/_acdpretty
$ podman run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtable

```bash
$ singularity exec <container> /usr/local/bin/_acdtable
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtrace

```bash
$ singularity exec <container> /usr/local/bin/_acdtrace
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdvalid

```bash
$ singularity exec <container> /usr/local/bin/_acdvalid
$ podman run --it --rm --entrypoint /usr/local/bin/_acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _antigenic

```bash
$ singularity exec <container> /usr/local/bin/_antigenic
$ podman run --it --rm --entrypoint /usr/local/bin/_antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _backtranambig

```bash
$ singularity exec <container> /usr/local/bin/_backtranambig
$ podman run --it --rm --entrypoint /usr/local/bin/_backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
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