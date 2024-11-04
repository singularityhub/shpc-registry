---
layout: container
name:  "quay.io/biocontainers/sap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sap/container.yaml"
updated_at: "2024-11-04 03:08:18.627340"
latest: "1.1.3--h031d066_4"
container_url: "https://biocontainers.pro/tools/sap"
aliases:
 - "sap"
versions:
 - "1.1.3--hec16e2b_2"
 - "1.1.3--h031d066_4"
description: "shpc-registry automated BioContainers addition for sap"
config: {"url": "https://biocontainers.pro/tools/sap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sap", "latest": {"1.1.3--h031d066_4": "sha256:ef8adfbffd7ec491bcb39eb9147ff467b1cdcdfc6c4bb2a67fbde833f4ed4eb4"}, "tags": {"1.1.3--hec16e2b_2": "sha256:611827a2bec2d4e11f2c6b81a2aae89fc0f6241eb9614f8c00d9fdc5aa9031d2", "1.1.3--h031d066_4": "sha256:ef8adfbffd7ec491bcb39eb9147ff467b1cdcdfc6c4bb2a67fbde833f4ed4eb4"}, "docker": "quay.io/biocontainers/sap", "aliases": {"sap": "/usr/local/bin/sap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sap.
shpc-registry automated BioContainers addition for sap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sap:1.1.3--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sap/1.1.3--h031d066_4
$ module help quay.io/biocontainers/sap/1.1.3--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sap

```bash
$ singularity exec <container> /usr/local/bin/sap
$ podman run --it --rm --entrypoint /usr/local/bin/sap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sap   -v ${PWD} -w ${PWD} <container> -c " $@"
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