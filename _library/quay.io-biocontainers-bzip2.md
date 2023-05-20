---
layout: container
name:  "quay.io/biocontainers/bzip2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bzip2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bzip2/container.yaml"
updated_at: "2023-05-20 02:47:11.569559"
latest: "1.0.8"
container_url: "https://biocontainers.pro/tools/bzip2"
aliases:
 - "bzip2"
 - "bzip2recover"
versions:
 - "1.0.8"
description: "shpc-registry automated BioContainers addition for bzip2"
config: {"url": "https://biocontainers.pro/tools/bzip2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bzip2", "latest": {"1.0.8": "sha256:4cf525c3120b73c85922fd6b688a30bb5a3aee93a2323ef3539ff204e297aa24"}, "tags": {"1.0.8": "sha256:4cf525c3120b73c85922fd6b688a30bb5a3aee93a2323ef3539ff204e297aa24"}, "docker": "quay.io/biocontainers/bzip2", "aliases": {"bzip2": "/usr/local/bin/bzip2", "bzip2recover": "/usr/local/bin/bzip2recover"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bzip2.
shpc-registry automated BioContainers addition for bzip2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bzip2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bzip2:1.0.8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bzip2/1.0.8
$ module help quay.io/biocontainers/bzip2/1.0.8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bzip2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bzip2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bzip2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bzip2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bzip2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bzip2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bzip2

```bash
$ singularity exec <container> /usr/local/bin/bzip2
$ podman run --it --rm --entrypoint /usr/local/bin/bzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzip2recover

```bash
$ singularity exec <container> /usr/local/bin/bzip2recover
$ podman run --it --rm --entrypoint /usr/local/bin/bzip2recover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzip2recover   -v ${PWD} -w ${PWD} <container> -c " $@"
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