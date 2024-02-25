---
layout: container
name:  "quay.io/biocontainers/rasusa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rasusa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rasusa/container.yaml"
updated_at: "2024-02-25 02:40:33.220228"
latest: "0.8.0--h031d066_0"
container_url: "https://biocontainers.pro/tools/rasusa"
aliases:
 - "rasusa"
versions:
 - "0.7.0--hec16e2b_1"
 - "0.7.1--hec16e2b_0"
 - "0.7.1--h031d066_2"
 - "0.8.0--h031d066_0"
description: "shpc-registry automated BioContainers addition for rasusa"
config: {"url": "https://biocontainers.pro/tools/rasusa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rasusa", "latest": {"0.8.0--h031d066_0": "sha256:0f7577bc44e65a924e0397e34409e22124b91a28b848f61b8a6c869c0d4b1928"}, "tags": {"0.7.0--hec16e2b_1": "sha256:0ece28f6a09a00cc777718efee938fe5721cf4f3295ffaad1138d3711633c970", "0.7.1--hec16e2b_0": "sha256:3b9615b296caef2e0a4c995a13e5532d72dbfa6484172afbe85202c7448142aa", "0.7.1--h031d066_2": "sha256:94d5e0a00070a336bb5da9a28811e8d138d1eec3a4cb1e9f16815f3893e80a64", "0.8.0--h031d066_0": "sha256:0f7577bc44e65a924e0397e34409e22124b91a28b848f61b8a6c869c0d4b1928"}, "docker": "quay.io/biocontainers/rasusa", "aliases": {"rasusa": "/usr/local/bin/rasusa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rasusa.
shpc-registry automated BioContainers addition for rasusa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rasusa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rasusa:0.8.0--h031d066_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rasusa/0.8.0--h031d066_0
$ module help quay.io/biocontainers/rasusa/0.8.0--h031d066_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rasusa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rasusa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rasusa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rasusa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rasusa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rasusa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rasusa

```bash
$ singularity exec <container> /usr/local/bin/rasusa
$ podman run --it --rm --entrypoint /usr/local/bin/rasusa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rasusa   -v ${PWD} -w ${PWD} <container> -c " $@"
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