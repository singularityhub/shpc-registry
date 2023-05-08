---
layout: container
name:  "quay.io/biocontainers/dnarrange"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnarrange/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnarrange/container.yaml"
updated_at: "2023-05-08 04:13:32.903339"
latest: "1.5.3--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/dnarrange"
aliases:
 - "dnarrange"
 - "dnarrange-genes"
 - "dnarrange-link"
 - "dnarrange-merge"
 - "fasta-nr"
 - "fastq-interleave"
 - "lamassemble"
 - "last-dotplot"
 - "last-map-probs"
 - "last-merge-batches"
 - "last-multiplot"
 - "last-pair-probs"
 - "last-postmask"
 - "last-split"
 - "last-split5"
 - "last-train"
 - "lastal"
 - "lastal5"
 - "lastdb"
 - "lastdb5"
 - "maf-convert"
 - "maf-cut"
 - "maf-join"
 - "maf-sort"
 - "maf-swap"
 - "parallel-fasta"
 - "parallel-fastq"
 - "parsort"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
 - "fftnsi"
 - "ginsi"
 - "linsi"
 - "mafft-distance"
 - "mafft-einsi"
 - "mafft-fftns"
versions:
 - "1.5.3--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for dnarrange"
config: {"url": "https://biocontainers.pro/tools/dnarrange", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnarrange", "latest": {"1.5.3--pyh5e36f6f_0": "sha256:1a0c04c0d9d8199965b44c2f22953e7521639ee28e1058fb4d0f60f876c93873"}, "tags": {"1.5.3--pyh5e36f6f_0": "sha256:1a0c04c0d9d8199965b44c2f22953e7521639ee28e1058fb4d0f60f876c93873"}, "docker": "quay.io/biocontainers/dnarrange", "aliases": {"dnarrange": "/usr/local/bin/dnarrange", "dnarrange-genes": "/usr/local/bin/dnarrange-genes", "dnarrange-link": "/usr/local/bin/dnarrange-link", "dnarrange-merge": "/usr/local/bin/dnarrange-merge", "fasta-nr": "/usr/local/bin/fasta-nr", "fastq-interleave": "/usr/local/bin/fastq-interleave", "lamassemble": "/usr/local/bin/lamassemble", "last-dotplot": "/usr/local/bin/last-dotplot", "last-map-probs": "/usr/local/bin/last-map-probs", "last-merge-batches": "/usr/local/bin/last-merge-batches", "last-multiplot": "/usr/local/bin/last-multiplot", "last-pair-probs": "/usr/local/bin/last-pair-probs", "last-postmask": "/usr/local/bin/last-postmask", "last-split": "/usr/local/bin/last-split", "last-split5": "/usr/local/bin/last-split5", "last-train": "/usr/local/bin/last-train", "lastal": "/usr/local/bin/lastal", "lastal5": "/usr/local/bin/lastal5", "lastdb": "/usr/local/bin/lastdb", "lastdb5": "/usr/local/bin/lastdb5", "maf-convert": "/usr/local/bin/maf-convert", "maf-cut": "/usr/local/bin/maf-cut", "maf-join": "/usr/local/bin/maf-join", "maf-sort": "/usr/local/bin/maf-sort", "maf-swap": "/usr/local/bin/maf-swap", "parallel-fasta": "/usr/local/bin/parallel-fasta", "parallel-fastq": "/usr/local/bin/parallel-fastq", "parsort": "/usr/local/bin/parsort", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns", "fftnsi": "/usr/local/bin/fftnsi", "ginsi": "/usr/local/bin/ginsi", "linsi": "/usr/local/bin/linsi", "mafft-distance": "/usr/local/bin/mafft-distance", "mafft-einsi": "/usr/local/bin/mafft-einsi", "mafft-fftns": "/usr/local/bin/mafft-fftns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnarrange.
shpc-registry automated BioContainers addition for dnarrange
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnarrange
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnarrange:1.5.3--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnarrange/1.5.3--pyh5e36f6f_0
$ module help quay.io/biocontainers/dnarrange/1.5.3--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnarrange-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnarrange-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnarrange-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnarrange-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnarrange-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnarrange-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnarrange

```bash
$ singularity exec <container> /usr/local/bin/dnarrange
$ podman run --it --rm --entrypoint /usr/local/bin/dnarrange   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnarrange   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnarrange-genes

```bash
$ singularity exec <container> /usr/local/bin/dnarrange-genes
$ podman run --it --rm --entrypoint /usr/local/bin/dnarrange-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnarrange-genes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnarrange-link

```bash
$ singularity exec <container> /usr/local/bin/dnarrange-link
$ podman run --it --rm --entrypoint /usr/local/bin/dnarrange-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnarrange-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnarrange-merge

```bash
$ singularity exec <container> /usr/local/bin/dnarrange-merge
$ podman run --it --rm --entrypoint /usr/local/bin/dnarrange-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnarrange-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-nr

```bash
$ singularity exec <container> /usr/local/bin/fasta-nr
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-nr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-nr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-interleave

```bash
$ singularity exec <container> /usr/local/bin/fastq-interleave
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lamassemble

```bash
$ singularity exec <container> /usr/local/bin/lamassemble
$ podman run --it --rm --entrypoint /usr/local/bin/lamassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lamassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### last-multiplot

```bash
$ singularity exec <container> /usr/local/bin/last-multiplot
$ podman run --it --rm --entrypoint /usr/local/bin/last-multiplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-multiplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### last-split5

```bash
$ singularity exec <container> /usr/local/bin/last-split5
$ podman run --it --rm --entrypoint /usr/local/bin/last-split5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-split5   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### lastal5

```bash
$ singularity exec <container> /usr/local/bin/lastal5
$ podman run --it --rm --entrypoint /usr/local/bin/lastal5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastal5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastdb

```bash
$ singularity exec <container> /usr/local/bin/lastdb
$ podman run --it --rm --entrypoint /usr/local/bin/lastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastdb5

```bash
$ singularity exec <container> /usr/local/bin/lastdb5
$ podman run --it --rm --entrypoint /usr/local/bin/lastdb5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastdb5   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftnsi

```bash
$ singularity exec <container> /usr/local/bin/fftnsi
$ podman run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ginsi

```bash
$ singularity exec <container> /usr/local/bin/ginsi
$ podman run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linsi

```bash
$ singularity exec <container> /usr/local/bin/linsi
$ podman run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-distance

```bash
$ singularity exec <container> /usr/local/bin/mafft-distance
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-einsi

```bash
$ singularity exec <container> /usr/local/bin/mafft-einsi
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftns

```bash
$ singularity exec <container> /usr/local/bin/mafft-fftns
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
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