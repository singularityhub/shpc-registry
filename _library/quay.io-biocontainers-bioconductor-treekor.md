---
layout: container
name:  "quay.io/biocontainers/bioconductor-treekor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-treekor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-treekor/container.yaml"
updated_at: "2023-01-12 03:24:10.355621"
latest: "1.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-treekor"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-treekor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-treekor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-treekor", "latest": {"1.6.0--r42hdfd78af_0": "sha256:9a7f07f441d69092ff76d2b3c6dbe9f7ec6998996da0934f8cc330306e7f5b59"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:b048679c87e5f506d259d988c0e89a36c07fb490d1ab08a8985897e82d65beb7", "1.6.0--r42hdfd78af_0": "sha256:9a7f07f441d69092ff76d2b3c6dbe9f7ec6998996da0934f8cc330306e7f5b59"}, "docker": "quay.io/biocontainers/bioconductor-treekor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-treekor.
shpc-registry automated BioContainers addition for bioconductor-treekor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-treekor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-treekor:1.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-treekor/1.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-treekor/1.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-treekor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treekor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treekor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-treekor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-treekor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-treekor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-treekor

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