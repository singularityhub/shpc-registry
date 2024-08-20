---
layout: container
name:  "quay.io/biocontainers/bioconductor-ribor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ribor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ribor/container.yaml"
updated_at: "2024-08-20 02:51:50.278060"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ribor"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ribor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ribor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ribor", "latest": {"1.14.0--r43hdfd78af_0": "sha256:516fc77c3aa21a96e0dc054fd1bf0470388d1655d487a75d6fcd3ac2b9fcfa0e"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:bd53a9240a993daef65255e8ab8ee16d3a2ef7bacf259a2759e949f6e092df1f", "1.10.0--r42hdfd78af_0": "sha256:2ec5aced0d6703f7109b5e7793c6ae1cf8bd53e18ab2b2d7d91b09334140b7cd", "1.12.0--r43hdfd78af_0": "sha256:8d1e1caff559154623e4f1efd3d803a136ecc1eb90c146b6f06675eac6dca187", "1.14.0--r43hdfd78af_0": "sha256:516fc77c3aa21a96e0dc054fd1bf0470388d1655d487a75d6fcd3ac2b9fcfa0e"}, "docker": "quay.io/biocontainers/bioconductor-ribor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ribor.
shpc-registry automated BioContainers addition for bioconductor-ribor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ribor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ribor:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ribor/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ribor/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ribor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ribor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ribor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ribor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ribor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ribor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ribor

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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