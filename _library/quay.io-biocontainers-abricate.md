---
layout: container
name:  "quay.io/biocontainers/abricate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abricate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abricate/container.yaml"
updated_at: "2025-09-11 05:07:54.689995"
latest: "1.0.1--h05cac1d_3"
container_url: "https://biocontainers.pro/tools/abricate"
aliases:
 - "abricate"
 - "abricate-get_db"
 - "any2fasta"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "unzip"
 - "bam2bedgraph"
 - "bp_pairwise_kaks"
 - "bp_find-blast-matches.pl"
 - "t_coffee"
versions:
 - "1.0.1--ha8f3691_1"
 - "1.0.1--ha8f3691_2"
 - "1.0.1--h05cac1d_3"
description: "shpc-registry automated BioContainers addition for abricate"
config: {"url": "https://biocontainers.pro/tools/abricate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abricate", "latest": {"1.0.1--h05cac1d_3": "sha256:e63b96f92ca214fce80cdf5e7247f3dbeb1b5a4f4057b8717916d5b3566db8c1"}, "tags": {"1.0.1--ha8f3691_1": "sha256:9de8b0d3edb97f9946ac8d57e2a1207d48801ae7a3b1f263f0a0e5773904451e", "1.0.1--ha8f3691_2": "sha256:3e40ec72d3fcb4352cda27fb71adbe73f0e6cb215cb337dc3ba44c809754ec93", "1.0.1--h05cac1d_3": "sha256:e63b96f92ca214fce80cdf5e7247f3dbeb1b5a4f4057b8717916d5b3566db8c1"}, "docker": "quay.io/biocontainers/abricate", "aliases": {"abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "any2fasta": "/usr/local/bin/any2fasta", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "unzip": "/usr/local/bin/unzip", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_pairwise_kaks": "/usr/local/bin/bp_pairwise_kaks", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "t_coffee": "/usr/local/bin/t_coffee"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abricate.
shpc-registry automated BioContainers addition for abricate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abricate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abricate:1.0.1--h05cac1d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abricate/1.0.1--h05cac1d_3
$ module help quay.io/biocontainers/abricate/1.0.1--h05cac1d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abricate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abricate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abricate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abricate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abricate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abricate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t_coffee

```bash
$ singularity exec <container> /usr/local/bin/t_coffee
$ podman run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
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