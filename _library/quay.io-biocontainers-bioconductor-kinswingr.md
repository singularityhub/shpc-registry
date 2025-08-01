---
layout: container
name:  "quay.io/biocontainers/bioconductor-kinswingr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-kinswingr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-kinswingr/container.yaml"
updated_at: "2025-08-01 04:37:00.196463"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-kinswingr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-kinswingr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-kinswingr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-kinswingr", "latest": {"1.24.0--r44hdfd78af_0": "sha256:53199f4af2a5aca8167d05a7f5af614efe57ffde67113523b19ae74e6c0a7c40"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:a9c6bee4b77629e445501acf878bc25766134dade67953ddd2a09656399fd834", "1.16.0--r42hdfd78af_0": "sha256:fbeb61dc37465eadb7b936574c5cb1819bf998a6ea4f3813701609e806163209", "1.12.0--r41hdfd78af_0": "sha256:a109bc01050f0814f86094336d1b9ff1b5c994627fe834256185b7f5e76c430b", "1.10.0--r41hdfd78af_0": "sha256:03b0ac92c612c35f77b67e4e01b42a139247e1e6e7b8ae3b2e9da7b44307c8b8", "1.18.0--r43hdfd78af_0": "sha256:7da3ec1dfe9f535b5b9d8fb80858ea97954117795cda80d8129c5bd57e942233", "1.20.0--r43hdfd78af_0": "sha256:fbc656402c3816045366b38d6c17936d25f2772810d9df161d5131cfe3d90a25", "1.24.0--r44hdfd78af_0": "sha256:53199f4af2a5aca8167d05a7f5af614efe57ffde67113523b19ae74e6c0a7c40"}, "docker": "quay.io/biocontainers/bioconductor-kinswingr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-kinswingr.
shpc-registry automated BioContainers addition for bioconductor-kinswingr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-kinswingr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-kinswingr:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-kinswingr/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-kinswingr/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-kinswingr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kinswingr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kinswingr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-kinswingr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-kinswingr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-kinswingr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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