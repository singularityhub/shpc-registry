---
layout: container
name:  "quay.io/biocontainers/halla"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/halla/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/halla/container.yaml"
updated_at: "2022-10-27 00:44:38.521311"
latest: "0.8.17--py36_0"
container_url: "https://biocontainers.pro/tools/halla"
aliases:
 - "halla"
 - "halladata"
 - "hallagram"
 - "hallascatter"
versions:
 - "0.8.17--py36_0"
description: "shpc-registry automated BioContainers addition for halla"
config: {"url": "https://biocontainers.pro/tools/halla", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for halla", "latest": {"0.8.17--py36_0": "sha256:4c4ae4051f8db1e777892a856a89447478a610d6f9a58858e754ab40637f0848"}, "tags": {"0.8.17--py36_0": "sha256:4c4ae4051f8db1e777892a856a89447478a610d6f9a58858e754ab40637f0848"}, "docker": "quay.io/biocontainers/halla", "aliases": {"halla": "/usr/local/bin/halla", "halladata": "/usr/local/bin/halladata", "hallagram": "/usr/local/bin/hallagram", "hallascatter": "/usr/local/bin/hallascatter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/halla.
shpc-registry automated BioContainers addition for halla
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/halla
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/halla:0.8.17--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/halla/0.8.17--py36_0
$ module help quay.io/biocontainers/halla/0.8.17--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### halla-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### halla-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### halla-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### halla-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### halla-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### halla-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### halla

```bash
$ singularity exec <container> /usr/local/bin/halla
$ podman run --it --rm --entrypoint /usr/local/bin/halla   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halla   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### halladata

```bash
$ singularity exec <container> /usr/local/bin/halladata
$ podman run --it --rm --entrypoint /usr/local/bin/halladata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halladata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hallagram

```bash
$ singularity exec <container> /usr/local/bin/hallagram
$ podman run --it --rm --entrypoint /usr/local/bin/hallagram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hallagram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hallascatter

```bash
$ singularity exec <container> /usr/local/bin/hallascatter
$ podman run --it --rm --entrypoint /usr/local/bin/hallascatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hallascatter   -v ${PWD} -w ${PWD} <container> -c " $@"
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