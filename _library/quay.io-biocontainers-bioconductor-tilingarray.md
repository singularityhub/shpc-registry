---
layout: container
name:  "quay.io/biocontainers/bioconductor-tilingarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tilingarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tilingarray/container.yaml"
updated_at: "2023-11-07 03:16:43.889661"
latest: "1.78.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tilingarray"

versions:
 - "1.72.0--r41hc0cfd56_2"
 - "1.76.0--r42hc0cfd56_0"
 - "1.76.0--r42ha9d7317_1"
 - "1.78.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tilingarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tilingarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tilingarray", "latest": {"1.78.0--r43ha9d7317_0": "sha256:eab608b17499fb3f7842f61dcd5ee94d6cfd8f0475f29875c237059e19e6d8c8"}, "tags": {"1.72.0--r41hc0cfd56_2": "sha256:58297a96fe687de7636745bd0f6d47081c4eef9d4f2e81e803b2c2278976f005", "1.76.0--r42hc0cfd56_0": "sha256:c0a405188f217da33aeb65dd676e012f0f485e6c612d5df8ef74977cf4eb1c72", "1.76.0--r42ha9d7317_1": "sha256:98714d37d44d0c03accd1185ed29799685bc597a551ee4fd870760e3096907ab", "1.78.0--r43ha9d7317_0": "sha256:eab608b17499fb3f7842f61dcd5ee94d6cfd8f0475f29875c237059e19e6d8c8"}, "docker": "quay.io/biocontainers/bioconductor-tilingarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tilingarray.
shpc-registry automated BioContainers addition for bioconductor-tilingarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tilingarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tilingarray:1.78.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tilingarray/1.78.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-tilingarray/1.78.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tilingarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tilingarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tilingarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tilingarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tilingarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tilingarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tilingarray

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