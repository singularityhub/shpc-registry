---
layout: container
name:  "quay.io/biocontainers/circleseeker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/circleseeker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/circleseeker/container.yaml"
updated_at: "2026-03-05 00:43:27.499008"
latest: "1.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/circleseeker"
aliases:
 - "CircleSeeker"
 - "TideHunter"
 - "circleseeker"
 - "fasta-nr"
 - "maf-cut"
 - "maf-linked"
 - "fastq-interleave"
 - "last-dotplot"
 - "last-map-probs"
 - "last-pair-probs"
 - "last-postmask"
 - "last-split"
 - "last-train"
 - "lastal"
 - "lastdb"
 - "maf-convert"
 - "maf-join"
 - "maf-sort"
 - "maf-swap"
 - "parallel-fasta"
 - "parallel-fastq"
 - "last-merge-batches"
 - "minimap2.py"
 - "ref-cache"
 - "cd-hit-clstr_2_blm8.pl"
 - "FET.pl"
 - "clstr_list.pl"
 - "clstr_list_sort.pl"
 - "cd-hit"
 - "cd-hit-2d"
 - "cd-hit-2d-para.pl"
versions:
 - "1.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for circleseeker"
config: {"url": "https://biocontainers.pro/tools/circleseeker", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for circleseeker", "latest": {"1.1.1--pyhdfd78af_0": "sha256:d781ef5e2c362c3beaaf35603845851885a2ed8ed2c0b80653b63e5da0b98119"}, "tags": {"1.1.1--pyhdfd78af_0": "sha256:d781ef5e2c362c3beaaf35603845851885a2ed8ed2c0b80653b63e5da0b98119"}, "docker": "quay.io/biocontainers/circleseeker", "aliases": {"CircleSeeker": "/usr/local/bin/CircleSeeker", "TideHunter": "/usr/local/bin/TideHunter", "circleseeker": "/usr/local/bin/circleseeker", "fasta-nr": "/usr/local/bin/fasta-nr", "maf-cut": "/usr/local/bin/maf-cut", "maf-linked": "/usr/local/bin/maf-linked", "fastq-interleave": "/usr/local/bin/fastq-interleave", "last-dotplot": "/usr/local/bin/last-dotplot", "last-map-probs": "/usr/local/bin/last-map-probs", "last-pair-probs": "/usr/local/bin/last-pair-probs", "last-postmask": "/usr/local/bin/last-postmask", "last-split": "/usr/local/bin/last-split", "last-train": "/usr/local/bin/last-train", "lastal": "/usr/local/bin/lastal", "lastdb": "/usr/local/bin/lastdb", "maf-convert": "/usr/local/bin/maf-convert", "maf-join": "/usr/local/bin/maf-join", "maf-sort": "/usr/local/bin/maf-sort", "maf-swap": "/usr/local/bin/maf-swap", "parallel-fasta": "/usr/local/bin/parallel-fasta", "parallel-fastq": "/usr/local/bin/parallel-fastq", "last-merge-batches": "/usr/local/bin/last-merge-batches", "minimap2.py": "/usr/local/bin/minimap2.py", "ref-cache": "/usr/local/bin/ref-cache", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "FET.pl": "/usr/local/bin/FET.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl", "clstr_list_sort.pl": "/usr/local/bin/clstr_list_sort.pl", "cd-hit": "/usr/local/bin/cd-hit", "cd-hit-2d": "/usr/local/bin/cd-hit-2d", "cd-hit-2d-para.pl": "/usr/local/bin/cd-hit-2d-para.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/circleseeker.
singularity registry hpc automated addition for circleseeker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/circleseeker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/circleseeker:1.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/circleseeker/1.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/circleseeker/1.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### circleseeker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### circleseeker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### circleseeker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### circleseeker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### circleseeker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### circleseeker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CircleSeeker

```bash
$ singularity exec <container> /usr/local/bin/CircleSeeker
$ podman run --it --rm --entrypoint /usr/local/bin/CircleSeeker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CircleSeeker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TideHunter

```bash
$ singularity exec <container> /usr/local/bin/TideHunter
$ podman run --it --rm --entrypoint /usr/local/bin/TideHunter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TideHunter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circleseeker

```bash
$ singularity exec <container> /usr/local/bin/circleseeker
$ podman run --it --rm --entrypoint /usr/local/bin/circleseeker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circleseeker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-nr

```bash
$ singularity exec <container> /usr/local/bin/fasta-nr
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-nr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-nr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-cut

```bash
$ singularity exec <container> /usr/local/bin/maf-cut
$ podman run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-linked

```bash
$ singularity exec <container> /usr/local/bin/maf-linked
$ podman run --it --rm --entrypoint /usr/local/bin/maf-linked   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-linked   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### lastdb

```bash
$ singularity exec <container> /usr/local/bin/lastdb
$ podman run --it --rm --entrypoint /usr/local/bin/lastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-convert

```bash
$ singularity exec <container> /usr/local/bin/maf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/maf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### last-merge-batches

```bash
$ singularity exec <container> /usr/local/bin/last-merge-batches
$ podman run --it --rm --entrypoint /usr/local/bin/last-merge-batches   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-merge-batches   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-clstr_2_blm8.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-clstr_2_blm8.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list_sort.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list_sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit

```bash
$ singularity exec <container> /usr/local/bin/cd-hit
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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