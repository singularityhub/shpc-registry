---
layout: container
name:  "quay.io/biocontainers/bamhash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamhash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamhash/container.yaml"
updated_at: "2023-05-02 03:36:20.144645"
latest: "1.1--h32c79c6_6"
container_url: "https://biocontainers.pro/tools/bamhash"
aliases:
 - "bamhash_checksum_bam"
 - "bamhash_checksum_fasta"
 - "bamhash_checksum_fastq"
versions:
 - "1.1--h32c79c6_6"
description: "shpc-registry automated BioContainers addition for bamhash"
config: {"url": "https://biocontainers.pro/tools/bamhash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamhash", "latest": {"1.1--h32c79c6_6": "sha256:d0b26d96a0026731feaa4351ebd5e4791f0aebe5836141d8702307f895627ae9"}, "tags": {"1.1--h32c79c6_6": "sha256:d0b26d96a0026731feaa4351ebd5e4791f0aebe5836141d8702307f895627ae9"}, "docker": "quay.io/biocontainers/bamhash", "aliases": {"bamhash_checksum_bam": "/usr/local/bin/bamhash_checksum_bam", "bamhash_checksum_fasta": "/usr/local/bin/bamhash_checksum_fasta", "bamhash_checksum_fastq": "/usr/local/bin/bamhash_checksum_fastq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamhash.
shpc-registry automated BioContainers addition for bamhash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamhash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamhash:1.1--h32c79c6_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamhash/1.1--h32c79c6_6
$ module help quay.io/biocontainers/bamhash/1.1--h32c79c6_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamhash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamhash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamhash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamhash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamhash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamhash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamhash_checksum_bam

```bash
$ singularity exec <container> /usr/local/bin/bamhash_checksum_bam
$ podman run --it --rm --entrypoint /usr/local/bin/bamhash_checksum_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamhash_checksum_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamhash_checksum_fasta

```bash
$ singularity exec <container> /usr/local/bin/bamhash_checksum_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/bamhash_checksum_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamhash_checksum_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamhash_checksum_fastq

```bash
$ singularity exec <container> /usr/local/bin/bamhash_checksum_fastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamhash_checksum_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamhash_checksum_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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