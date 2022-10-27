---
layout: container
name:  "quay.io/biocontainers/bioconductor-mapscape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mapscape/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mapscape/container.yaml"
updated_at: "2022-10-27 00:38:21.787360"
latest: "1.8.0--r361_1"
container_url: "https://biocontainers.pro/tools/bioconductor-mapscape"

versions:
 - "1.8.0--r361_1"
description: "shpc-registry automated BioContainers addition for bioconductor-mapscape"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mapscape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mapscape", "latest": {"1.8.0--r361_1": "sha256:cc2dc6b0bf25e581425e85300b673a4609fd98315858274fedad19413dc5c01b"}, "tags": {"1.8.0--r361_1": "sha256:cc2dc6b0bf25e581425e85300b673a4609fd98315858274fedad19413dc5c01b"}, "docker": "quay.io/biocontainers/bioconductor-mapscape"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mapscape.
shpc-registry automated BioContainers addition for bioconductor-mapscape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mapscape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mapscape:1.8.0--r361_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mapscape/1.8.0--r361_1
$ module help quay.io/biocontainers/bioconductor-mapscape/1.8.0--r361_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mapscape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapscape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mapscape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mapscape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mapscape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mapscape-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mapscape

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