---
layout: container
name:  "quay.io/biocontainers/soapdenovo2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapdenovo2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapdenovo2/container.yaml"
updated_at: "2024-03-18 02:58:18.304591"
latest: "2.40--1"
container_url: "https://biocontainers.pro/tools/soapdenovo2"

versions:
 - "2.40--1"
description: "shpc-registry automated BioContainers addition for soapdenovo2"
config: {"url": "https://biocontainers.pro/tools/soapdenovo2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapdenovo2", "latest": {"2.40--1": "sha256:07f6f28132589eaa707aaad2f087aa0389d709ab7af758ca0fbac23e1be939a0"}, "tags": {"2.40--1": "sha256:07f6f28132589eaa707aaad2f087aa0389d709ab7af758ca0fbac23e1be939a0"}, "docker": "quay.io/biocontainers/soapdenovo2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapdenovo2.
shpc-registry automated BioContainers addition for soapdenovo2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapdenovo2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapdenovo2:2.40--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapdenovo2/2.40--1
$ module help quay.io/biocontainers/soapdenovo2/2.40--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapdenovo2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapdenovo2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapdenovo2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapdenovo2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapdenovo2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### soapdenovo2

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