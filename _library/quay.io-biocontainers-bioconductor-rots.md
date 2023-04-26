---
layout: container
name:  "quay.io/biocontainers/bioconductor-rots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rots/container.yaml"
updated_at: "2023-04-26 03:15:59.747877"
latest: "1.26.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rots"

versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.16.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rots"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rots", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rots", "latest": {"1.26.0--r42hc247a5b_0": "sha256:fc17f9b05961757f7d69d12743d224ad5e2fc3d5e8bbe57a48b5d26ea846b249"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:3cd6044911158101c494f3266c33b6d81448f971301699307a043d47147a1ea4", "1.26.0--r42hc247a5b_0": "sha256:fc17f9b05961757f7d69d12743d224ad5e2fc3d5e8bbe57a48b5d26ea846b249", "1.22.0--r41hc247a5b_2": "sha256:4f0d10750b94d9c6c40639d4ef91ae66bc67971e67ea2e6d64bcc82472cf300e", "1.20.0--r41h399db7b_0": "sha256:4e60df4a4d4f83d02c8a0f9206977aa8fc301260eeb337c7937254a9c92d864b", "1.18.0--r40h399db7b_1": "sha256:60bcd40c84244efcebf112f08372709510f7dd51d7024fe6b1514932ee0b387a", "1.16.0--r40h5f743cb_0": "sha256:e8709fd46d10b09460664af8c69648ab6ceb8f0c9737f7fae9f3c66a218c51c8"}, "docker": "quay.io/biocontainers/bioconductor-rots"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rots.
shpc-registry automated BioContainers addition for bioconductor-rots
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rots
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rots:1.26.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rots/1.26.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-rots/1.26.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rots-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rots

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