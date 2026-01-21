---
layout: container
name:  "quay.io/biocontainers/tadbit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tadbit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tadbit/container.yaml"
updated_at: "2026-01-21 04:09:56.127055"
latest: "1.0.1--py36h4aaaa08_1"
container_url: "https://biocontainers.pro/tools/tadbit"
aliases:
 - "gem-indexer"
 - "gem-mapper"
 - "gem-retriever"
 - "normalize_oneD.R"
 - "tadbit"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
 - "mcxassemble"
versions:
 - "1.0.1--py36h4aaaa08_1"
 - "1.0--py27h877ad6c_1"
 - "1.0.1--py310h2a84d7f_1"
description: "shpc-registry automated BioContainers addition for tadbit"
config: {"url": "https://biocontainers.pro/tools/tadbit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tadbit", "latest": {"1.0.1--py36h4aaaa08_1": "sha256:c3c69e45f09ff844de670fb2204610268bab04c181f495c45cc810268d468897"}, "tags": {"1.0.1--py36h4aaaa08_1": "sha256:c3c69e45f09ff844de670fb2204610268bab04c181f495c45cc810268d468897", "1.0--py27h877ad6c_1": "sha256:c82fad7b55d437ae373e3926a75c793503e3c7e08b7319b1b926ccdb88ea5b30", "1.0.1--py310h2a84d7f_1": "sha256:04a00d23463ff263ba768054ee3304508abb790e7873b3264db2673dde3b05fb"}, "docker": "quay.io/biocontainers/tadbit", "aliases": {"gem-indexer": "/usr/local/bin/gem-indexer", "gem-mapper": "/usr/local/bin/gem-mapper", "gem-retriever": "/usr/local/bin/gem-retriever", "normalize_oneD.R": "/usr/local/bin/normalize_oneD.R", "tadbit": "/usr/local/bin/tadbit", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tadbit.
shpc-registry automated BioContainers addition for tadbit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tadbit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tadbit:1.0.1--py36h4aaaa08_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tadbit/1.0.1--py36h4aaaa08_1
$ module help quay.io/biocontainers/tadbit/1.0.1--py36h4aaaa08_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tadbit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tadbit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tadbit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tadbit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tadbit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tadbit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gem-indexer

```bash
$ singularity exec <container> /usr/local/bin/gem-indexer
$ podman run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-mapper

```bash
$ singularity exec <container> /usr/local/bin/gem-mapper
$ podman run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-retriever

```bash
$ singularity exec <container> /usr/local/bin/gem-retriever
$ podman run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize_oneD.R

```bash
$ singularity exec <container> /usr/local/bin/normalize_oneD.R
$ podman run --it --rm --entrypoint /usr/local/bin/normalize_oneD.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize_oneD.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tadbit

```bash
$ singularity exec <container> /usr/local/bin/tadbit
$ podman run --it --rm --entrypoint /usr/local/bin/tadbit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tadbit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxassemble

```bash
$ singularity exec <container> /usr/local/bin/mcxassemble
$ podman run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
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