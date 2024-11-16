---
layout: container
name:  "quay.io/biocontainers/magpurify"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/magpurify/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/magpurify/container.yaml"
updated_at: "2024-11-16 02:59:49.607520"
latest: "2.1.2--py_1"
container_url: "https://biocontainers.pro/tools/magpurify"
aliases:
 - "coverm"
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
 - "magpurify"
 - "parallel-fasta"
 - "parallel-fastq"
 - "remove_minimap2_duplicated_headers"
 - "starcode"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "mash"
 - "parsort"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
versions:
 - "2.1.2--py_1"
description: "shpc-registry automated BioContainers addition for magpurify"
config: {"url": "https://biocontainers.pro/tools/magpurify", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for magpurify", "latest": {"2.1.2--py_1": "sha256:04aa9ea844627dcad499aa86a37c41e85936527c4f195ff1a4c8726c940546ae"}, "tags": {"2.1.2--py_1": "sha256:04aa9ea844627dcad499aa86a37c41e85936527c4f195ff1a4c8726c940546ae"}, "docker": "quay.io/biocontainers/magpurify", "aliases": {"coverm": "/usr/local/bin/coverm", "fastq-interleave": "/usr/local/bin/fastq-interleave", "last-dotplot": "/usr/local/bin/last-dotplot", "last-map-probs": "/usr/local/bin/last-map-probs", "last-merge-batches": "/usr/local/bin/last-merge-batches", "last-pair-probs": "/usr/local/bin/last-pair-probs", "last-postmask": "/usr/local/bin/last-postmask", "last-split": "/usr/local/bin/last-split", "last-split8": "/usr/local/bin/last-split8", "last-train": "/usr/local/bin/last-train", "lastal": "/usr/local/bin/lastal", "lastal8": "/usr/local/bin/lastal8", "lastdb": "/usr/local/bin/lastdb", "lastdb8": "/usr/local/bin/lastdb8", "maf-convert": "/usr/local/bin/maf-convert", "maf-cut": "/usr/local/bin/maf-cut", "maf-join": "/usr/local/bin/maf-join", "maf-sort": "/usr/local/bin/maf-sort", "maf-swap": "/usr/local/bin/maf-swap", "magpurify": "/usr/local/bin/magpurify", "parallel-fasta": "/usr/local/bin/parallel-fasta", "parallel-fastq": "/usr/local/bin/parallel-fastq", "remove_minimap2_duplicated_headers": "/usr/local/bin/remove_minimap2_duplicated_headers", "starcode": "/usr/local/bin/starcode", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash", "parsort": "/usr/local/bin/parsort", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/magpurify.
shpc-registry automated BioContainers addition for magpurify
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/magpurify
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/magpurify:2.1.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/magpurify/2.1.2--py_1
$ module help quay.io/biocontainers/magpurify/2.1.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### magpurify-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### magpurify-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### magpurify-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### magpurify-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### magpurify-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### magpurify-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coverm

```bash
$ singularity exec <container> /usr/local/bin/coverm
$ podman run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### magpurify

```bash
$ singularity exec <container> /usr/local/bin/magpurify
$ podman run --it --rm --entrypoint /usr/local/bin/magpurify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magpurify   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### remove_minimap2_duplicated_headers

```bash
$ singularity exec <container> /usr/local/bin/remove_minimap2_duplicated_headers
$ podman run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-c++

```bash
$ singularity exec <container> /usr/local/bin/capnpc-c++
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-capnp

```bash
$ singularity exec <container> /usr/local/bin/capnpc-capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mash

```bash
$ singularity exec <container> /usr/local/bin/mash
$ podman run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
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