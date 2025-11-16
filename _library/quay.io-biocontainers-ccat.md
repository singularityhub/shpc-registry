---
layout: container
name:  "quay.io/biocontainers/ccat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ccat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ccat/container.yaml"
updated_at: "2025-11-16 04:07:28.880682"
latest: "3.0--hec16e2b_5"
container_url: "https://biocontainers.pro/tools/ccat"
aliases:
 - "CCAT"
versions:
 - "3.0--hec16e2b_5"
description: "shpc-registry automated BioContainers addition for ccat"
config: {"url": "https://biocontainers.pro/tools/ccat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ccat", "latest": {"3.0--hec16e2b_5": "sha256:edcb462eda3cb3b51ffffc12a2133fd8971c6e0871b39e1e0641fd16527b6f9c"}, "tags": {"3.0--hec16e2b_5": "sha256:edcb462eda3cb3b51ffffc12a2133fd8971c6e0871b39e1e0641fd16527b6f9c"}, "docker": "quay.io/biocontainers/ccat", "aliases": {"CCAT": "/usr/local/bin/CCAT"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ccat.
shpc-registry automated BioContainers addition for ccat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ccat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ccat:3.0--hec16e2b_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ccat/3.0--hec16e2b_5
$ module help quay.io/biocontainers/ccat/3.0--hec16e2b_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ccat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ccat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ccat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ccat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ccat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ccat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CCAT

```bash
$ singularity exec <container> /usr/local/bin/CCAT
$ podman run --it --rm --entrypoint /usr/local/bin/CCAT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CCAT   -v ${PWD} -w ${PWD} <container> -c " $@"
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