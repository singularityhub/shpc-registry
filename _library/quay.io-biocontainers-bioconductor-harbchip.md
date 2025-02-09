---
layout: container
name:  "quay.io/biocontainers/bioconductor-harbchip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-harbchip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-harbchip/container.yaml"
updated_at: "2025-02-09 03:09:12.678368"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-harbchip"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-harbchip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-harbchip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-harbchip", "latest": {"1.44.0--r44hdfd78af_0": "sha256:14df8e019063844fd1de18a34f84068e1ce4a97e94fc8dec47821d7ea3e1d750"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:b96e33d5e1626f8d2072f019e2945f0cdc123b3e9bf80c4397325d316f7da66c", "1.36.0--r42hdfd78af_0": "sha256:782ac11e3161e14b08f479d5ea00eb352ae4de3cb898e0df23f3166f90d13023", "1.38.0--r43hdfd78af_0": "sha256:f6a3f51afde079b214fa087f66417fda39a8570c5ab4bacf636be5a37997eec6", "1.40.0--r43hdfd78af_0": "sha256:102469365daad3045cb2a878eb8435ead781d2ad083617216860e3517e91ac89", "1.44.0--r44hdfd78af_0": "sha256:14df8e019063844fd1de18a34f84068e1ce4a97e94fc8dec47821d7ea3e1d750"}, "docker": "quay.io/biocontainers/bioconductor-harbchip"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-harbchip.
shpc-registry automated BioContainers addition for bioconductor-harbchip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-harbchip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-harbchip:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-harbchip/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-harbchip/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-harbchip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harbchip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harbchip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-harbchip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-harbchip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-harbchip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-harbchip

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