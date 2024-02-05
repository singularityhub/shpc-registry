---
layout: container
name:  "quay.io/biocontainers/iqtree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/iqtree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/iqtree/container.yaml"
updated_at: "2024-02-05 02:36:22.908361"
latest: "2.2.6--h21ec9f0_0"
container_url: "https://biocontainers.pro/tools/iqtree"
aliases:
 - "iqtree"
 - "iqtree2"
versions:
 - "2.2.0_beta--hb97b32f_1"
 - "2.2.0.3--hb97b32f_1"
 - "2.2.2.3--hb97b32f_0"
 - "2.2.2.3--h2202e69_2"
 - "2.2.2.7--h21ec9f0_2"
 - "2.2.3--h21ec9f0_0"
 - "2.2.5--h21ec9f0_0"
 - "2.2.6--h21ec9f0_0"
description: "shpc-registry automated BioContainers addition for iqtree"
config: {"url": "https://biocontainers.pro/tools/iqtree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for iqtree", "latest": {"2.2.6--h21ec9f0_0": "sha256:40230f1ed601f73bfe8bc4ae8bc0f1cdbeadc91fe77d3e10fb0f18c7e5ec8964"}, "tags": {"2.2.0_beta--hb97b32f_1": "sha256:96ca289717c1d1d07536802939f2da66c22ccf7e527b22297c78de585358e1c3", "2.2.0.3--hb97b32f_1": "sha256:a4d3f266bfac25f8018eaf03b14db48c66aa6eb02391ad28cf19520d61c3e5fb", "2.2.2.3--hb97b32f_0": "sha256:4442ecc36f74f42136a862eb4418c07cc3b220fcdc89c933127a14f61af66f97", "2.2.2.3--h2202e69_2": "sha256:a5f542fabdb0049270011df51d5561fa3884f0e0dc546d23722f46e58c7967fe", "2.2.2.7--h21ec9f0_2": "sha256:795c665251b2a6a92be9f5556b5c082d5907d00135231f663bbf0420000f6397", "2.2.3--h21ec9f0_0": "sha256:e64c69633a2eeb8755904583bf9601997a799dea1511987604fba26c51074501", "2.2.5--h21ec9f0_0": "sha256:4497a9270b83c860c8665e9618b326c1d1b879511bd0ba7fcb77e7ede061c834", "2.2.6--h21ec9f0_0": "sha256:40230f1ed601f73bfe8bc4ae8bc0f1cdbeadc91fe77d3e10fb0f18c7e5ec8964"}, "docker": "quay.io/biocontainers/iqtree", "aliases": {"iqtree": "/usr/local/bin/iqtree", "iqtree2": "/usr/local/bin/iqtree2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/iqtree.
shpc-registry automated BioContainers addition for iqtree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/iqtree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/iqtree:2.2.6--h21ec9f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/iqtree/2.2.6--h21ec9f0_0
$ module help quay.io/biocontainers/iqtree/2.2.6--h21ec9f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### iqtree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### iqtree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### iqtree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### iqtree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### iqtree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### iqtree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
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