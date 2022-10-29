---
layout: container
name:  "quay.io/biocontainers/komb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/komb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/komb/container.yaml"
updated_at: "2022-10-29 05:50:03.187459"
latest: "1.0--py37h595c7a6_5"
container_url: "https://biocontainers.pro/tools/komb"
aliases:
 - "Bifrost"
 - "abyss-db-csv"
 - "komb"
 - "2to3-3.7"
 - "ABYSS"
 - "ABYSS-P"
 - "AdjList"
 - "Consensus"
 - "DAssembler"
 - "DistanceEst"
 - "DistanceEst-ssq"
 - "KAligner"
 - "MergeContigs"
versions:
 - "1.0--py37h595c7a6_5"
description: "shpc-registry automated BioContainers addition for komb"
config: {"url": "https://biocontainers.pro/tools/komb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for komb", "latest": {"1.0--py37h595c7a6_5": "sha256:9362a60c7a27bd00c04a7d599660e43cd4a3acb45d9f56306ee3248fe1a8707b"}, "tags": {"1.0--py37h595c7a6_5": "sha256:9362a60c7a27bd00c04a7d599660e43cd4a3acb45d9f56306ee3248fe1a8707b"}, "docker": "quay.io/biocontainers/komb", "aliases": {"Bifrost": "/usr/local/bin/Bifrost", "abyss-db-csv": "/usr/local/bin/abyss-db-csv", "komb": "/usr/local/bin/komb", "2to3-3.7": "/usr/local/bin/2to3-3.7", "ABYSS": "/usr/local/bin/ABYSS", "ABYSS-P": "/usr/local/bin/ABYSS-P", "AdjList": "/usr/local/bin/AdjList", "Consensus": "/usr/local/bin/Consensus", "DAssembler": "/usr/local/bin/DAssembler", "DistanceEst": "/usr/local/bin/DistanceEst", "DistanceEst-ssq": "/usr/local/bin/DistanceEst-ssq", "KAligner": "/usr/local/bin/KAligner", "MergeContigs": "/usr/local/bin/MergeContigs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/komb.
shpc-registry automated BioContainers addition for komb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/komb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/komb:1.0--py37h595c7a6_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/komb/1.0--py37h595c7a6_5
$ module help quay.io/biocontainers/komb/1.0--py37h595c7a6_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### komb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### komb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### komb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### komb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### komb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### komb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bifrost

```bash
$ singularity exec <container> /usr/local/bin/Bifrost
$ podman run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-db-csv

```bash
$ singularity exec <container> /usr/local/bin/abyss-db-csv
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### komb

```bash
$ singularity exec <container> /usr/local/bin/komb
$ podman run --it --rm --entrypoint /usr/local/bin/komb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/komb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ABYSS

```bash
$ singularity exec <container> /usr/local/bin/ABYSS
$ podman run --it --rm --entrypoint /usr/local/bin/ABYSS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ABYSS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ABYSS-P

```bash
$ singularity exec <container> /usr/local/bin/ABYSS-P
$ podman run --it --rm --entrypoint /usr/local/bin/ABYSS-P   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ABYSS-P   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AdjList

```bash
$ singularity exec <container> /usr/local/bin/AdjList
$ podman run --it --rm --entrypoint /usr/local/bin/AdjList   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AdjList   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Consensus

```bash
$ singularity exec <container> /usr/local/bin/Consensus
$ podman run --it --rm --entrypoint /usr/local/bin/Consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DAssembler

```bash
$ singularity exec <container> /usr/local/bin/DAssembler
$ podman run --it --rm --entrypoint /usr/local/bin/DAssembler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DAssembler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DistanceEst

```bash
$ singularity exec <container> /usr/local/bin/DistanceEst
$ podman run --it --rm --entrypoint /usr/local/bin/DistanceEst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DistanceEst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DistanceEst-ssq

```bash
$ singularity exec <container> /usr/local/bin/DistanceEst-ssq
$ podman run --it --rm --entrypoint /usr/local/bin/DistanceEst-ssq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DistanceEst-ssq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KAligner

```bash
$ singularity exec <container> /usr/local/bin/KAligner
$ podman run --it --rm --entrypoint /usr/local/bin/KAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MergeContigs

```bash
$ singularity exec <container> /usr/local/bin/MergeContigs
$ podman run --it --rm --entrypoint /usr/local/bin/MergeContigs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MergeContigs   -v ${PWD} -w ${PWD} <container> -c " $@"
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