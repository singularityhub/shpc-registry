---
layout: container
name:  "quay.io/biocontainers/bioconductor-bufferedmatrixmethods"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bufferedmatrixmethods/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bufferedmatrixmethods/container.yaml"
updated_at: "2024-12-29 03:24:24.106120"
latest: "1.66.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bufferedmatrixmethods"

versions:
 - "1.58.0--r41hc0cfd56_2"
 - "1.61.0--r42hc0cfd56_0"
 - "1.61.0--r42ha9d7317_1"
 - "1.64.0--r43ha9d7317_0"
 - "1.66.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bufferedmatrixmethods"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bufferedmatrixmethods", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bufferedmatrixmethods", "latest": {"1.66.0--r43ha9d7317_0": "sha256:4dfb59ba1e723500e40a31bae734d295a4ee6fda9196ef3d19a7ad1e2ad1c7f7"}, "tags": {"1.58.0--r41hc0cfd56_2": "sha256:6e5218393657051ad69aedc51e0d4288fed1e5c3e27c832aeef4070c8c6d2c6b", "1.61.0--r42hc0cfd56_0": "sha256:f6224b1e59722f1ef8c259af27708b93c0473974e429cbb3a3c15324b872ab58", "1.61.0--r42ha9d7317_1": "sha256:4fed13ae4db0b3d354df6bccc67c0fdb1410bc90e871dc31af27ccb7ebdbc316", "1.64.0--r43ha9d7317_0": "sha256:e5001d90ed72f101f7923e7a5ba46e0c3e9a7801c6984274815f4350b1303e2e", "1.66.0--r43ha9d7317_0": "sha256:4dfb59ba1e723500e40a31bae734d295a4ee6fda9196ef3d19a7ad1e2ad1c7f7"}, "docker": "quay.io/biocontainers/bioconductor-bufferedmatrixmethods"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bufferedmatrixmethods.
shpc-registry automated BioContainers addition for bioconductor-bufferedmatrixmethods
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bufferedmatrixmethods
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bufferedmatrixmethods:1.66.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bufferedmatrixmethods/1.66.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-bufferedmatrixmethods/1.66.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bufferedmatrixmethods-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bufferedmatrixmethods-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bufferedmatrixmethods-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bufferedmatrixmethods-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bufferedmatrixmethods-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bufferedmatrixmethods-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bufferedmatrixmethods

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