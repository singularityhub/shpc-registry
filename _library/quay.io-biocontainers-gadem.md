---
layout: container
name:  "quay.io/biocontainers/gadem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gadem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gadem/container.yaml"
updated_at: "2024-09-14 03:31:33.687230"
latest: "1.3.1--h031d066_7"
container_url: "https://biocontainers.pro/tools/gadem"
aliases:
 - "gadem"
versions:
 - "1.3.1--hec16e2b_4"
 - "1.3.1--h031d066_6"
 - "1.3.1--h031d066_7"
description: "shpc-registry automated BioContainers addition for gadem"
config: {"url": "https://biocontainers.pro/tools/gadem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gadem", "latest": {"1.3.1--h031d066_7": "sha256:9034d2da5739a807add3b41366e52fe31a6499894e3786502c0d0eb3b888f646"}, "tags": {"1.3.1--hec16e2b_4": "sha256:de5c2d16302c3e35b4ffb032421a1a6d9ac2cd9e272111a45fb8b7d91ec2786e", "1.3.1--h031d066_6": "sha256:8d8cf76d2d51e0224cecd7fe2e26bade84e49767ec171ceb48cdc23968f556bd", "1.3.1--h031d066_7": "sha256:9034d2da5739a807add3b41366e52fe31a6499894e3786502c0d0eb3b888f646"}, "docker": "quay.io/biocontainers/gadem", "aliases": {"gadem": "/usr/local/bin/gadem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gadem.
shpc-registry automated BioContainers addition for gadem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gadem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gadem:1.3.1--h031d066_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gadem/1.3.1--h031d066_7
$ module help quay.io/biocontainers/gadem/1.3.1--h031d066_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gadem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gadem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gadem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gadem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gadem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gadem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gadem

```bash
$ singularity exec <container> /usr/local/bin/gadem
$ podman run --it --rm --entrypoint /usr/local/bin/gadem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gadem   -v ${PWD} -w ${PWD} <container> -c " $@"
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