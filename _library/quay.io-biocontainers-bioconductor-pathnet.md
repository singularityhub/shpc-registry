---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathnet/container.yaml"
updated_at: "2023-02-13 02:59:16.290749"
latest: "1.38.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathnet"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathnet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathnet", "latest": {"1.38.0--r42hdfd78af_0": "sha256:f3797b88e232cec17dd0e4c0b6d658e3d35a499a4df47c2dea73d3ebc02fc41c"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:c853379d2f678e6c1f89d51e8f887f84c8ecc61ed9403f0b899b6f79308521a3", "1.38.0--r42hdfd78af_0": "sha256:f3797b88e232cec17dd0e4c0b6d658e3d35a499a4df47c2dea73d3ebc02fc41c"}, "docker": "quay.io/biocontainers/bioconductor-pathnet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathnet.
shpc-registry automated BioContainers addition for bioconductor-pathnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathnet:1.38.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathnet/1.38.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pathnet/1.38.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pathnet

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