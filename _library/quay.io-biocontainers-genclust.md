---
layout: container
name:  "quay.io/biocontainers/genclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genclust/container.yaml"
updated_at: "2025-10-31 03:44:36.078337"
latest: "1.0--hec16e2b_3"
container_url: "https://biocontainers.pro/tools/genclust"
aliases:
 - "genclust"
versions:
 - "1.0--hec16e2b_3"
description: "shpc-registry automated BioContainers addition for genclust"
config: {"url": "https://biocontainers.pro/tools/genclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genclust", "latest": {"1.0--hec16e2b_3": "sha256:3f7ada966b6d03c4430cf0ae1a89ad93228b878e9c8e4dbc648e3f800f883ad0"}, "tags": {"1.0--hec16e2b_3": "sha256:3f7ada966b6d03c4430cf0ae1a89ad93228b878e9c8e4dbc648e3f800f883ad0"}, "docker": "quay.io/biocontainers/genclust", "aliases": {"genclust": "/usr/local/bin/genclust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genclust.
shpc-registry automated BioContainers addition for genclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genclust:1.0--hec16e2b_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genclust/1.0--hec16e2b_3
$ module help quay.io/biocontainers/genclust/1.0--hec16e2b_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genclust

```bash
$ singularity exec <container> /usr/local/bin/genclust
$ podman run --it --rm --entrypoint /usr/local/bin/genclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genclust   -v ${PWD} -w ${PWD} <container> -c " $@"
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