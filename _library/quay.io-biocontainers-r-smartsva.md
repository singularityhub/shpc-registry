---
layout: container
name:  "quay.io/biocontainers/r-smartsva"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-smartsva/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-smartsva/container.yaml"
updated_at: "2024-02-03 02:52:04.686284"
latest: "0.1.3--r43h21a89ab_8"
container_url: "https://biocontainers.pro/tools/r-smartsva"

versions:
 - "0.1.3--r41hecf12ef_5"
 - "0.1.3--r42hecf12ef_6"
 - "0.1.3--r42h21a89ab_7"
 - "0.1.3--r43h21a89ab_8"
description: "shpc-registry automated BioContainers addition for r-smartsva"
config: {"url": "https://biocontainers.pro/tools/r-smartsva", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-smartsva", "latest": {"0.1.3--r43h21a89ab_8": "sha256:304d33b62238964f0b3a1d5959b740ab0bfb5c7f59859b1e18eecec42d898c07"}, "tags": {"0.1.3--r41hecf12ef_5": "sha256:59cb4b6796563f3cd2b4762d1dc85d1e347f2ab4fc27414388c28b36db9bac7a", "0.1.3--r42hecf12ef_6": "sha256:250d91d1b48d556aa05b5b4ba317df18442958b2f32bb86d54fbb94779ada590", "0.1.3--r42h21a89ab_7": "sha256:b98e4d9ec1aca212bea61a9e11cef4628f384d0e1ca32e1d287e33688409c287", "0.1.3--r43h21a89ab_8": "sha256:304d33b62238964f0b3a1d5959b740ab0bfb5c7f59859b1e18eecec42d898c07"}, "docker": "quay.io/biocontainers/r-smartsva"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-smartsva.
shpc-registry automated BioContainers addition for r-smartsva
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-smartsva
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-smartsva:0.1.3--r43h21a89ab_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-smartsva/0.1.3--r43h21a89ab_8
$ module help quay.io/biocontainers/r-smartsva/0.1.3--r43h21a89ab_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-smartsva-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-smartsva-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-smartsva-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-smartsva-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-smartsva-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-smartsva-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-smartsva

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