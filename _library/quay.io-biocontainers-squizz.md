---
layout: container
name:  "quay.io/biocontainers/squizz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/squizz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/squizz/container.yaml"
updated_at: "2023-02-23 03:45:55.913995"
latest: "0.99d--hec16e2b_4"
container_url: "https://biocontainers.pro/tools/squizz"
aliases:
 - "squizz"
versions:
 - "0.99d--hec16e2b_4"
description: "shpc-registry automated BioContainers addition for squizz"
config: {"url": "https://biocontainers.pro/tools/squizz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for squizz", "latest": {"0.99d--hec16e2b_4": "sha256:6f7404af0d76b299fc46734e2a06099a5191433af30fd349e85b8acbcc4b38ab"}, "tags": {"0.99d--hec16e2b_4": "sha256:6f7404af0d76b299fc46734e2a06099a5191433af30fd349e85b8acbcc4b38ab"}, "docker": "quay.io/biocontainers/squizz", "aliases": {"squizz": "/usr/local/bin/squizz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/squizz.
shpc-registry automated BioContainers addition for squizz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/squizz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/squizz:0.99d--hec16e2b_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/squizz/0.99d--hec16e2b_4
$ module help quay.io/biocontainers/squizz/0.99d--hec16e2b_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### squizz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### squizz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### squizz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### squizz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### squizz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### squizz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### squizz

```bash
$ singularity exec <container> /usr/local/bin/squizz
$ podman run --it --rm --entrypoint /usr/local/bin/squizz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/squizz   -v ${PWD} -w ${PWD} <container> -c " $@"
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