---
layout: container
name:  "quay.io/biocontainers/mageck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mageck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mageck/container.yaml"
updated_at: "2025-10-07 03:25:44.829836"
latest: "0.5.9.5--py310h184ae93_8"
container_url: "https://biocontainers.pro/tools/mageck"

versions:
 - "0.5.9--py27h6bb024c_0"
 - "0.5.9.5--py39h1f90b4d_3"
 - "0.5.9.5--py38h2494328_4"
 - "0.5.9.5--py311h2a4ad6c_5"
 - "0.5.9.5--py312hf731ba3_6"
 - "0.5.9.5--py310h184ae93_8"
description: "shpc-registry automated BioContainers addition for mageck"
config: {"url": "https://biocontainers.pro/tools/mageck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mageck", "latest": {"0.5.9.5--py310h184ae93_8": "sha256:d75024a642ed1799ad86abb85784e4f891dee76f62d07658c5d596f3d80c2d5b"}, "tags": {"0.5.9--py27h6bb024c_0": "sha256:a48b9632470df5d854c43fb986f95df8e1b3749265a6f4de81dcd06db9bb3537", "0.5.9.5--py39h1f90b4d_3": "sha256:46311eda123fa8c2f4cac44921407a11962f7c65d73028f0babd89b709b4dcb9", "0.5.9.5--py38h2494328_4": "sha256:c0a0dc2f99da12af4c9dee2b3dd56918efab6240549b7f5b10c08ec5635f86b3", "0.5.9.5--py311h2a4ad6c_5": "sha256:d04109a6ea7ef95157d36fc311c7a455d4254514295c133b173f1fe46abc1a6b", "0.5.9.5--py312hf731ba3_6": "sha256:31fd8669ff75f60a4a04a3908054aa638aac90d27d0b05c4ae5fb1eef45b26a2", "0.5.9.5--py310h184ae93_8": "sha256:d75024a642ed1799ad86abb85784e4f891dee76f62d07658c5d596f3d80c2d5b"}, "docker": "quay.io/biocontainers/mageck"}
---

This module is a singularity container wrapper for quay.io/biocontainers/mageck.
shpc-registry automated BioContainers addition for mageck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mageck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mageck:0.5.9.5--py310h184ae93_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mageck/0.5.9.5--py310h184ae93_8
$ module help quay.io/biocontainers/mageck/0.5.9.5--py310h184ae93_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mageck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mageck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mageck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mageck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mageck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mageck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mageck

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