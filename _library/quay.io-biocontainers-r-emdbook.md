---
layout: container
name:  "quay.io/biocontainers/r-emdbook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-emdbook/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-emdbook/container.yaml"
updated_at: "2022-10-27 00:45:32.057273"
latest: "1.3.9--r3.3.1_0"
container_url: "https://biocontainers.pro/tools/r-emdbook"

versions:
 - "1.3.9--r3.3.1_0"
description: "shpc-registry automated BioContainers addition for r-emdbook"
config: {"url": "https://biocontainers.pro/tools/r-emdbook", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-emdbook", "latest": {"1.3.9--r3.3.1_0": "sha256:d5c86fc734093393a9f9654c23c10397c80f88bd7403f8226f36e5b178e00f1f"}, "tags": {"1.3.9--r3.3.1_0": "sha256:d5c86fc734093393a9f9654c23c10397c80f88bd7403f8226f36e5b178e00f1f"}, "docker": "quay.io/biocontainers/r-emdbook"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-emdbook.
shpc-registry automated BioContainers addition for r-emdbook
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-emdbook
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-emdbook:1.3.9--r3.3.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-emdbook/1.3.9--r3.3.1_0
$ module help quay.io/biocontainers/r-emdbook/1.3.9--r3.3.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-emdbook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-emdbook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-emdbook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-emdbook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-emdbook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-emdbook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-emdbook

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