---
layout: container
name:  "quay.io/biocontainers/parafly"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parafly/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/parafly/container.yaml"
updated_at: "2023-05-03 03:00:16.900900"
latest: "r2013_01_21--1"
container_url: "https://biocontainers.pro/tools/parafly"
aliases:
 - "ParaFly"
versions:
 - "r2013_01_21--1"
description: "shpc-registry automated BioContainers addition for parafly"
config: {"url": "https://biocontainers.pro/tools/parafly", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parafly", "latest": {"r2013_01_21--1": "sha256:847dfde25fc5aaca81d2fa5a69276dc1df6d206166469d7f5ae10ff98278fb29"}, "tags": {"r2013_01_21--1": "sha256:847dfde25fc5aaca81d2fa5a69276dc1df6d206166469d7f5ae10ff98278fb29"}, "docker": "quay.io/biocontainers/parafly", "aliases": {"ParaFly": "/usr/local/bin/ParaFly"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parafly.
shpc-registry automated BioContainers addition for parafly
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parafly
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parafly:r2013_01_21--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parafly/r2013_01_21--1
$ module help quay.io/biocontainers/parafly/r2013_01_21--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parafly-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parafly-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parafly-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parafly-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parafly-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parafly-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ParaFly

```bash
$ singularity exec <container> /usr/local/bin/ParaFly
$ podman run --it --rm --entrypoint /usr/local/bin/ParaFly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ParaFly   -v ${PWD} -w ${PWD} <container> -c " $@"
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