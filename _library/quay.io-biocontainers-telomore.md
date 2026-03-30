---
layout: container
name:  "quay.io/biocontainers/telomore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/telomore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/telomore/container.yaml"
updated_at: "2026-03-30 05:04:45.142828"
latest: "0.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/telomore"
aliases:
 - "fasta-nr"
 - "lamassemble"
 - "maf-cut"
 - "maf-linked"
 - "telomore"
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
 - "xmlget"
 - "xmltext"
 - "aaindexextract"
 - "abiview"
 - "acdgalaxy"
 - "acdlog"
 - "acdpretty"
 - "acdtable"
 - "acdtrace"
versions:
 - "0.4.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for telomore"
config: {"url": "https://biocontainers.pro/tools/telomore", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for telomore", "latest": {"0.4.1--pyhdfd78af_0": "sha256:ccff223601ddd7afbe735fac03b7c5056e2a0cdb8695a14711b1406cb73c7270"}, "tags": {"0.4.1--pyhdfd78af_0": "sha256:ccff223601ddd7afbe735fac03b7c5056e2a0cdb8695a14711b1406cb73c7270"}, "docker": "quay.io/biocontainers/telomore", "aliases": {"fasta-nr": "/usr/local/bin/fasta-nr", "lamassemble": "/usr/local/bin/lamassemble", "maf-cut": "/usr/local/bin/maf-cut", "maf-linked": "/usr/local/bin/maf-linked", "telomore": "/usr/local/bin/telomore", "fastq-interleave": "/usr/local/bin/fastq-interleave", "last-dotplot": "/usr/local/bin/last-dotplot", "last-map-probs": "/usr/local/bin/last-map-probs", "last-pair-probs": "/usr/local/bin/last-pair-probs", "last-postmask": "/usr/local/bin/last-postmask", "last-split": "/usr/local/bin/last-split", "last-train": "/usr/local/bin/last-train", "lastal": "/usr/local/bin/lastal", "lastdb": "/usr/local/bin/lastdb", "maf-convert": "/usr/local/bin/maf-convert", "maf-join": "/usr/local/bin/maf-join", "maf-sort": "/usr/local/bin/maf-sort", "maf-swap": "/usr/local/bin/maf-swap", "parallel-fasta": "/usr/local/bin/parallel-fasta", "parallel-fastq": "/usr/local/bin/parallel-fastq", "last-merge-batches": "/usr/local/bin/last-merge-batches", "xmlget": "/usr/local/bin/xmlget", "xmltext": "/usr/local/bin/xmltext", "aaindexextract": "/usr/local/bin/aaindexextract", "abiview": "/usr/local/bin/abiview", "acdgalaxy": "/usr/local/bin/acdgalaxy", "acdlog": "/usr/local/bin/acdlog", "acdpretty": "/usr/local/bin/acdpretty", "acdtable": "/usr/local/bin/acdtable", "acdtrace": "/usr/local/bin/acdtrace"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/telomore.
singularity registry hpc automated addition for telomore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/telomore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/telomore:0.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/telomore/0.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/telomore/0.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### telomore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### telomore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### telomore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### telomore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### telomore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### telomore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasta-nr

```bash
$ singularity exec <container> /usr/local/bin/fasta-nr
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-nr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-nr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lamassemble

```bash
$ singularity exec <container> /usr/local/bin/lamassemble
$ podman run --it --rm --entrypoint /usr/local/bin/lamassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lamassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### telomore

```bash
$ singularity exec <container> /usr/local/bin/telomore
$ podman run --it --rm --entrypoint /usr/local/bin/telomore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/telomore   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xmlget

```bash
$ singularity exec <container> /usr/local/bin/xmlget
$ podman run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmltext

```bash
$ singularity exec <container> /usr/local/bin/xmltext
$ podman run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmltext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abiview

```bash
$ singularity exec <container> /usr/local/bin/abiview
$ podman run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdgalaxy

```bash
$ singularity exec <container> /usr/local/bin/acdgalaxy
$ podman run --it --rm --entrypoint /usr/local/bin/acdgalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdgalaxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdlog

```bash
$ singularity exec <container> /usr/local/bin/acdlog
$ podman run --it --rm --entrypoint /usr/local/bin/acdlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdpretty

```bash
$ singularity exec <container> /usr/local/bin/acdpretty
$ podman run --it --rm --entrypoint /usr/local/bin/acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdtable

```bash
$ singularity exec <container> /usr/local/bin/acdtable
$ podman run --it --rm --entrypoint /usr/local/bin/acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acdtrace

```bash
$ singularity exec <container> /usr/local/bin/acdtrace
$ podman run --it --rm --entrypoint /usr/local/bin/acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
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