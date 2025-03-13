---
layout: container
name:  "quay.io/biocontainers/sumaclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sumaclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sumaclust/container.yaml"
updated_at: "2025-03-13 05:23:19.923278"
latest: "1.0.31--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/sumaclust"
aliases:
 - "sumaclust"
versions:
 - "1.0.31--hec16e2b_4"
 - "1.0.31--h031d066_6"
 - "1.0.31--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for sumaclust"
config: {"url": "https://biocontainers.pro/tools/sumaclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sumaclust", "latest": {"1.0.31--h7b50bb2_7": "sha256:11d0dd5ef3f75de8b60dcfeb0cd59744825fe3a5f8e6990f9fdb4bcaa0df1e7c"}, "tags": {"1.0.31--hec16e2b_4": "sha256:0642b5f80857abb50e39bb07ff25e278d177b1f6a4247997e5c646759b4a9095", "1.0.31--h031d066_6": "sha256:bbf70dfed517e2fa3460e0ce3b0ec7b07ab4993abe23a856dedefcf6a1682c8e", "1.0.31--h7b50bb2_7": "sha256:11d0dd5ef3f75de8b60dcfeb0cd59744825fe3a5f8e6990f9fdb4bcaa0df1e7c"}, "docker": "quay.io/biocontainers/sumaclust", "aliases": {"sumaclust": "/usr/local/bin/sumaclust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sumaclust.
shpc-registry automated BioContainers addition for sumaclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sumaclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sumaclust:1.0.31--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sumaclust/1.0.31--h7b50bb2_7
$ module help quay.io/biocontainers/sumaclust/1.0.31--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sumaclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sumaclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sumaclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sumaclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sumaclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sumaclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sumaclust

```bash
$ singularity exec <container> /usr/local/bin/sumaclust
$ podman run --it --rm --entrypoint /usr/local/bin/sumaclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumaclust   -v ${PWD} -w ${PWD} <container> -c " $@"
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