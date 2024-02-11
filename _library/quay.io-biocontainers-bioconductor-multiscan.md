---
layout: container
name:  "quay.io/biocontainers/bioconductor-multiscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multiscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multiscan/container.yaml"
updated_at: "2024-02-11 02:42:02.246519"
latest: "1.62.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multiscan"

versions:
 - "1.54.0--r41hc0cfd56_2"
 - "1.58.0--r42hc0cfd56_0"
 - "1.58.0--r42ha9d7317_1"
 - "1.60.0--r43ha9d7317_0"
 - "1.62.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multiscan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multiscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multiscan", "latest": {"1.62.0--r43ha9d7317_0": "sha256:6a2a038e9f5c7fcda0ae07e58f2ceb291e39f150e8f336e0934886588983b40e"}, "tags": {"1.54.0--r41hc0cfd56_2": "sha256:c0f78e8a360775039917d59e1ea66c22dbb6ee3fb69d7c334501259df6b6b374", "1.58.0--r42hc0cfd56_0": "sha256:054aeb1cecf9c0a566c20f2dfad8110803af75da0c1379fb1dbabaf8f2916b62", "1.58.0--r42ha9d7317_1": "sha256:77d57be5a6f3d7498704fa98c4b6a0a5098d405c40eff076ed37d4aa4646dec0", "1.60.0--r43ha9d7317_0": "sha256:a9323d2ac07aca895cb134c7034a66ebdc44976d7b902c154088aa7c9257bf53", "1.62.0--r43ha9d7317_0": "sha256:6a2a038e9f5c7fcda0ae07e58f2ceb291e39f150e8f336e0934886588983b40e"}, "docker": "quay.io/biocontainers/bioconductor-multiscan"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multiscan.
shpc-registry automated BioContainers addition for bioconductor-multiscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multiscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multiscan:1.62.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multiscan/1.62.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-multiscan/1.62.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multiscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multiscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multiscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multiscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-multiscan

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