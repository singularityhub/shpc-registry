---
layout: container
name:  "quay.io/biocontainers/harvesttools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/harvesttools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/harvesttools/container.yaml"
updated_at: "2023-09-11 03:34:38.263788"
latest: "1.2--h139f625_1"
container_url: "https://biocontainers.pro/tools/harvesttools"
aliases:
 - "harvesttools"
versions:
 - "1.2--h139f625_1"
description: "shpc-registry automated BioContainers addition for harvesttools"
config: {"url": "https://biocontainers.pro/tools/harvesttools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for harvesttools", "latest": {"1.2--h139f625_1": "sha256:aca6182668c03777cbe14d9298edd9806ab53207296daadefca072af5fb69f0f"}, "tags": {"1.2--h139f625_1": "sha256:aca6182668c03777cbe14d9298edd9806ab53207296daadefca072af5fb69f0f"}, "docker": "quay.io/biocontainers/harvesttools", "aliases": {"harvesttools": "/usr/local/bin/harvesttools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/harvesttools.
shpc-registry automated BioContainers addition for harvesttools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/harvesttools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/harvesttools:1.2--h139f625_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/harvesttools/1.2--h139f625_1
$ module help quay.io/biocontainers/harvesttools/1.2--h139f625_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### harvesttools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### harvesttools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### harvesttools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### harvesttools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### harvesttools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### harvesttools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### harvesttools

```bash
$ singularity exec <container> /usr/local/bin/harvesttools
$ podman run --it --rm --entrypoint /usr/local/bin/harvesttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/harvesttools   -v ${PWD} -w ${PWD} <container> -c " $@"
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