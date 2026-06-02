---
layout: container
name:  "quay.io/biocontainers/prseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prseq/container.yaml"
updated_at: "2026-06-02 07:15:46.659769"
latest: "0.0.33--py310h7e03b2b_0"
container_url: "https://biocontainers.pro/tools/prseq"
aliases:
 - "fasta-filter"
 - "fasta-info"
 - "fasta-stats"
 - "fastq-filter"
 - "fastq-info"
 - "fastq-stats"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.0.33--py310h7e03b2b_0"
 - "0.0.33--py312h07859c3_0"
description: "singularity registry hpc automated addition for prseq"
config: {"url": "https://biocontainers.pro/tools/prseq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for prseq", "latest": {"0.0.33--py310h7e03b2b_0": "sha256:efea91ca6d0a927faec793b89218afe2d7e39d1f4c1a27979a9149e9ed3116c5"}, "tags": {"0.0.33--py310h7e03b2b_0": "sha256:efea91ca6d0a927faec793b89218afe2d7e39d1f4c1a27979a9149e9ed3116c5", "0.0.33--py312h07859c3_0": "sha256:ed9c5a1f4cf92e37c96d8335da71b94dc2f041d48f44bfc134e7768e533c3f7a"}, "docker": "quay.io/biocontainers/prseq", "aliases": {"fasta-filter": "/usr/local/bin/fasta-filter", "fasta-info": "/usr/local/bin/fasta-info", "fasta-stats": "/usr/local/bin/fasta-stats", "fastq-filter": "/usr/local/bin/fastq-filter", "fastq-info": "/usr/local/bin/fastq-info", "fastq-stats": "/usr/local/bin/fastq-stats", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prseq.
singularity registry hpc automated addition for prseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prseq:0.0.33--py310h7e03b2b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prseq/0.0.33--py310h7e03b2b_0
$ module help quay.io/biocontainers/prseq/0.0.33--py310h7e03b2b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasta-filter

```bash
$ singularity exec <container> /usr/local/bin/fasta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-info

```bash
$ singularity exec <container> /usr/local/bin/fasta-info
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-stats

```bash
$ singularity exec <container> /usr/local/bin/fasta-stats
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-filter

```bash
$ singularity exec <container> /usr/local/bin/fastq-filter
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-info

```bash
$ singularity exec <container> /usr/local/bin/fastq-info
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-stats

```bash
$ singularity exec <container> /usr/local/bin/fastq-stats
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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