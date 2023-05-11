---
layout: container
name:  "quay.io/biocontainers/bioconductor-rqubic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rqubic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rqubic/container.yaml"
updated_at: "2023-05-11 03:05:52.733636"
latest: "1.44.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rqubic"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rqubic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rqubic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rqubic", "latest": {"1.44.0--r42hc0cfd56_0": "sha256:a1f41d550391670ef348e3b573f7ada0c69e39d8d03940e560258f9fdcc5fa7d"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:72476766f7e29083d3dfee75909a7f5cd422ad658d1611f84942d066f4faf58e", "1.44.0--r42hc0cfd56_0": "sha256:a1f41d550391670ef348e3b573f7ada0c69e39d8d03940e560258f9fdcc5fa7d"}, "docker": "quay.io/biocontainers/bioconductor-rqubic"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rqubic.
shpc-registry automated BioContainers addition for bioconductor-rqubic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rqubic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rqubic:1.44.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rqubic/1.44.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-rqubic/1.44.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rqubic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rqubic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rqubic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rqubic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rqubic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rqubic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rqubic

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