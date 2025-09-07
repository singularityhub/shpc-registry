---
layout: container
name:  "quay.io/biocontainers/bioconductor-grmetrics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-grmetrics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-grmetrics/container.yaml"
updated_at: "2025-09-07 03:42:15.935775"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-grmetrics"
aliases:
 - "idn2"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-grmetrics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-grmetrics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-grmetrics", "latest": {"1.32.0--r44hdfd78af_0": "sha256:d9b1b840f90cb4392ba54f43d03972e714a867e7ef1580cea6d9beb5b87337c7"}, "tags": {"1.8.1--r351_0": "sha256:4f030502a32fd33fceed01a968efb6672904a3527064bb89afdb5ec53463dde4", "1.24.0--r42hdfd78af_0": "sha256:025a479d92f071072bfdc820b6d441c44e6df8cd5641e1be83acdba91e5cbe1a", "1.20.0--r41hdfd78af_0": "sha256:6956732564daeb695474e57f56fac549f426be26b04806e56815b139742ea0e7", "1.18.0--r41hdfd78af_0": "sha256:c3e944db3850810df1c0ccb07c9c5cc0a2744f9c5f035990a4fad70ed5a7c85e", "1.16.0--r40hdfd78af_1": "sha256:22c26f286a334c0f4228677b4f00d870c034e470462c6d94e3613062c34cd0a2", "1.14.0--r40_0": "sha256:efa1ea4ce169912d054b021e05a4af4a8d88e03728ddcb538ccc5c9e88d20dc9", "1.26.0--r43hdfd78af_0": "sha256:257480d4e1a68ca9a73b36b00909638d5649e48826fe6d2e3720a6013ba70265", "1.28.0--r43hdfd78af_0": "sha256:e2dc0b17e54b40b31011fbaf4687ceb21973bf9fbf9ece8a9cb87f9cd3d05a4c", "1.32.0--r44hdfd78af_0": "sha256:d9b1b840f90cb4392ba54f43d03972e714a867e7ef1580cea6d9beb5b87337c7"}, "docker": "quay.io/biocontainers/bioconductor-grmetrics", "aliases": {"idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-grmetrics.
shpc-registry automated BioContainers addition for bioconductor-grmetrics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-grmetrics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-grmetrics:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-grmetrics/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-grmetrics/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-grmetrics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grmetrics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grmetrics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-grmetrics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-grmetrics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-grmetrics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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