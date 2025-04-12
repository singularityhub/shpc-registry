---
layout: container
name:  "quay.io/biocontainers/get_fasta_info"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/get_fasta_info/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/get_fasta_info/container.yaml"
updated_at: "2025-04-12 03:12:52.993816"
latest: "2.5.0--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/get_fasta_info"
aliases:
 - "get_fasta_info"
 - "get_fastq_info"
versions:
 - "2.4--h7132678_0"
 - "2.4--he4a0461_2"
 - "2.4--h577a1d6_3"
 - "2.5.0--h577a1d6_0"
description: "singularity registry hpc automated addition for get_fasta_info"
config: {"url": "https://biocontainers.pro/tools/get_fasta_info", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for get_fasta_info", "latest": {"2.5.0--h577a1d6_0": "sha256:9a25dd627a230e24aca0c774e04e4a809e60dc2a4bf65e4ba423987890aaa704"}, "tags": {"2.4--h7132678_0": "sha256:1d2e5a089c229cc1215b63ed870f234f3fd5032e1afce41c5c178df2318f09ae", "2.4--he4a0461_2": "sha256:6cd9c895b3b5fb70461dba6fc556c70245fd3f0d293029417f17b85fe57c90d4", "2.4--h577a1d6_3": "sha256:195afb18e99f17dd70711c7175e2074d9da3830a14cd6df2e9b94bdb9b4ed9e8", "2.5.0--h577a1d6_0": "sha256:9a25dd627a230e24aca0c774e04e4a809e60dc2a4bf65e4ba423987890aaa704"}, "docker": "quay.io/biocontainers/get_fasta_info", "aliases": {"get_fasta_info": "/usr/local/bin/get_fasta_info", "get_fastq_info": "/usr/local/bin/get_fastq_info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/get_fasta_info.
singularity registry hpc automated addition for get_fasta_info
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/get_fasta_info
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/get_fasta_info:2.5.0--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/get_fasta_info/2.5.0--h577a1d6_0
$ module help quay.io/biocontainers/get_fasta_info/2.5.0--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### get_fasta_info-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### get_fasta_info-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### get_fasta_info-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### get_fasta_info-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### get_fasta_info-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### get_fasta_info-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### get_fasta_info

```bash
$ singularity exec <container> /usr/local/bin/get_fasta_info
$ podman run --it --rm --entrypoint /usr/local/bin/get_fasta_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_fasta_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_fastq_info

```bash
$ singularity exec <container> /usr/local/bin/get_fastq_info
$ podman run --it --rm --entrypoint /usr/local/bin/get_fastq_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_fastq_info   -v ${PWD} -w ${PWD} <container> -c " $@"
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