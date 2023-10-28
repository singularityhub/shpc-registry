---
layout: container
name:  "quay.io/biocontainers/nanosim-h"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanosim-h/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanosim-h/container.yaml"
updated_at: "2023-10-28 03:02:27.527557"
latest: "1.1.0.4--pyr40h145b6a8_2"
container_url: "https://biocontainers.pro/tools/nanosim-h"
aliases:
 - "fastq-interleave"
 - "last-dotplot"
 - "last-map-probs"
 - "last-merge-batches"
 - "last-pair-probs"
 - "last-postmask"
 - "last-split"
 - "last-split8"
 - "last-train"
 - "lastal"
 - "lastal8"
 - "lastdb"
 - "lastdb8"
 - "maf-convert"
 - "maf-cut"
 - "maf-join"
 - "maf-sort"
 - "maf-swap"
 - "nanosim-h"
 - "nanosim-h-train"
 - "parallel-fasta"
 - "parallel-fastq"
 - "parsort"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
 - "env_parallel.dash"
 - "env_parallel.fish"
 - "env_parallel.ksh"
 - "env_parallel.mksh"
 - "env_parallel.pdksh"
versions:
 - "1.1.0.4--pyr40h145b6a8_2"
description: "shpc-registry automated BioContainers addition for nanosim-h"
config: {"url": "https://biocontainers.pro/tools/nanosim-h", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanosim-h", "latest": {"1.1.0.4--pyr40h145b6a8_2": "sha256:76e3d6ab85a917623886d04b49504f1c0865dcfb6fa27cf9d8bd1a7145a26150"}, "tags": {"1.1.0.4--pyr40h145b6a8_2": "sha256:76e3d6ab85a917623886d04b49504f1c0865dcfb6fa27cf9d8bd1a7145a26150"}, "docker": "quay.io/biocontainers/nanosim-h", "aliases": {"fastq-interleave": "/usr/local/bin/fastq-interleave", "last-dotplot": "/usr/local/bin/last-dotplot", "last-map-probs": "/usr/local/bin/last-map-probs", "last-merge-batches": "/usr/local/bin/last-merge-batches", "last-pair-probs": "/usr/local/bin/last-pair-probs", "last-postmask": "/usr/local/bin/last-postmask", "last-split": "/usr/local/bin/last-split", "last-split8": "/usr/local/bin/last-split8", "last-train": "/usr/local/bin/last-train", "lastal": "/usr/local/bin/lastal", "lastal8": "/usr/local/bin/lastal8", "lastdb": "/usr/local/bin/lastdb", "lastdb8": "/usr/local/bin/lastdb8", "maf-convert": "/usr/local/bin/maf-convert", "maf-cut": "/usr/local/bin/maf-cut", "maf-join": "/usr/local/bin/maf-join", "maf-sort": "/usr/local/bin/maf-sort", "maf-swap": "/usr/local/bin/maf-swap", "nanosim-h": "/usr/local/bin/nanosim-h", "nanosim-h-train": "/usr/local/bin/nanosim-h-train", "parallel-fasta": "/usr/local/bin/parallel-fasta", "parallel-fastq": "/usr/local/bin/parallel-fastq", "parsort": "/usr/local/bin/parsort", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh", "env_parallel.pdksh": "/usr/local/bin/env_parallel.pdksh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanosim-h.
shpc-registry automated BioContainers addition for nanosim-h
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanosim-h
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanosim-h:1.1.0.4--pyr40h145b6a8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanosim-h/1.1.0.4--pyr40h145b6a8_2
$ module help quay.io/biocontainers/nanosim-h/1.1.0.4--pyr40h145b6a8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanosim-h-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanosim-h-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanosim-h-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanosim-h-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanosim-h-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanosim-h-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-interleave

```bash
$ singularity exec <container> /usr/local/bin/fastq-interleave
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-dotplot

```bash
$ singularity exec <container> /usr/local/bin/last-dotplot
$ podman run --it --rm --entrypoint /usr/local/bin/last-dotplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-dotplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-map-probs

```bash
$ singularity exec <container> /usr/local/bin/last-map-probs
$ podman run --it --rm --entrypoint /usr/local/bin/last-map-probs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-map-probs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-merge-batches

```bash
$ singularity exec <container> /usr/local/bin/last-merge-batches
$ podman run --it --rm --entrypoint /usr/local/bin/last-merge-batches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-merge-batches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-pair-probs

```bash
$ singularity exec <container> /usr/local/bin/last-pair-probs
$ podman run --it --rm --entrypoint /usr/local/bin/last-pair-probs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-pair-probs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-postmask

```bash
$ singularity exec <container> /usr/local/bin/last-postmask
$ podman run --it --rm --entrypoint /usr/local/bin/last-postmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-postmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-split

```bash
$ singularity exec <container> /usr/local/bin/last-split
$ podman run --it --rm --entrypoint /usr/local/bin/last-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-split8

```bash
$ singularity exec <container> /usr/local/bin/last-split8
$ podman run --it --rm --entrypoint /usr/local/bin/last-split8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-split8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-train

```bash
$ singularity exec <container> /usr/local/bin/last-train
$ podman run --it --rm --entrypoint /usr/local/bin/last-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastal

```bash
$ singularity exec <container> /usr/local/bin/lastal
$ podman run --it --rm --entrypoint /usr/local/bin/lastal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastal8

```bash
$ singularity exec <container> /usr/local/bin/lastal8
$ podman run --it --rm --entrypoint /usr/local/bin/lastal8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastal8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastdb

```bash
$ singularity exec <container> /usr/local/bin/lastdb
$ podman run --it --rm --entrypoint /usr/local/bin/lastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastdb8

```bash
$ singularity exec <container> /usr/local/bin/lastdb8
$ podman run --it --rm --entrypoint /usr/local/bin/lastdb8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastdb8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-convert

```bash
$ singularity exec <container> /usr/local/bin/maf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/maf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-cut

```bash
$ singularity exec <container> /usr/local/bin/maf-cut
$ podman run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-join

```bash
$ singularity exec <container> /usr/local/bin/maf-join
$ podman run --it --rm --entrypoint /usr/local/bin/maf-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-sort

```bash
$ singularity exec <container> /usr/local/bin/maf-sort
$ podman run --it --rm --entrypoint /usr/local/bin/maf-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-swap

```bash
$ singularity exec <container> /usr/local/bin/maf-swap
$ podman run --it --rm --entrypoint /usr/local/bin/maf-swap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-swap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanosim-h

```bash
$ singularity exec <container> /usr/local/bin/nanosim-h
$ podman run --it --rm --entrypoint /usr/local/bin/nanosim-h   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanosim-h   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanosim-h-train

```bash
$ singularity exec <container> /usr/local/bin/nanosim-h-train
$ podman run --it --rm --entrypoint /usr/local/bin/nanosim-h-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanosim-h-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel-fasta

```bash
$ singularity exec <container> /usr/local/bin/parallel-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/parallel-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parallel-fastq

```bash
$ singularity exec <container> /usr/local/bin/parallel-fastq
$ podman run --it --rm --entrypoint /usr/local/bin/parallel-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parallel-fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.csh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.csh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.dash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.dash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.fish

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.fish
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.mksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.mksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.pdksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.pdksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
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