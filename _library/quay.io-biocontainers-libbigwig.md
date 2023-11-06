---
layout: container
name:  "quay.io/biocontainers/libbigwig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libbigwig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libbigwig/container.yaml"
updated_at: "2023-11-06 02:57:44.690920"
latest: "0.4.7--h09f99ed_4"
container_url: "https://biocontainers.pro/tools/libbigwig"

versions:
 - "0.4.7--h1d40642_0"
 - "0.4.7--h1d40642_1"
 - "0.4.7--h09f99ed_4"
description: "shpc-registry automated BioContainers addition for libbigwig"
config: {"url": "https://biocontainers.pro/tools/libbigwig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libbigwig", "latest": {"0.4.7--h09f99ed_4": "sha256:0c654cd9f5c0745cfa9ccc06992aa900a013d012816262748e1d3b19191e6129"}, "tags": {"0.4.7--h1d40642_0": "sha256:956927f13965b99fa747854709f47b8c8589d2372c345960063b6b787c202729", "0.4.7--h1d40642_1": "sha256:1a5b4aeef47708bb32e7f9c5e7dc3b6f6d6889ec86d7da702f35655f87350407", "0.4.7--h09f99ed_4": "sha256:0c654cd9f5c0745cfa9ccc06992aa900a013d012816262748e1d3b19191e6129"}, "docker": "quay.io/biocontainers/libbigwig"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libbigwig.
shpc-registry automated BioContainers addition for libbigwig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libbigwig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libbigwig:0.4.7--h09f99ed_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libbigwig/0.4.7--h09f99ed_4
$ module help quay.io/biocontainers/libbigwig/0.4.7--h09f99ed_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libbigwig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libbigwig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libbigwig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libbigwig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libbigwig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libbigwig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libbigwig

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