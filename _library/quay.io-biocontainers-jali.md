---
layout: container
name:  "quay.io/biocontainers/jali"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jali/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jali/container.yaml"
updated_at: "2023-10-04 03:09:31.732894"
latest: "1.3--0"
container_url: "https://biocontainers.pro/tools/jali"
aliases:
 - "jali"
 - "jscan"
 - "jsearch"
versions:
 - "1.3--0"
description: "shpc-registry automated BioContainers addition for jali"
config: {"url": "https://biocontainers.pro/tools/jali", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jali", "latest": {"1.3--0": "sha256:cf04cf7e161c3a83e8366770c54049ae529a6097e23bd112f0f53bb294ad0430"}, "tags": {"1.3--0": "sha256:cf04cf7e161c3a83e8366770c54049ae529a6097e23bd112f0f53bb294ad0430"}, "docker": "quay.io/biocontainers/jali", "aliases": {"jali": "/usr/local/bin/jali", "jscan": "/usr/local/bin/jscan", "jsearch": "/usr/local/bin/jsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jali.
shpc-registry automated BioContainers addition for jali
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jali
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jali:1.3--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jali/1.3--0
$ module help quay.io/biocontainers/jali/1.3--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jali-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jali-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jali-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jali-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jali-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jali-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jali

```bash
$ singularity exec <container> /usr/local/bin/jali
$ podman run --it --rm --entrypoint /usr/local/bin/jali   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jali   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jscan

```bash
$ singularity exec <container> /usr/local/bin/jscan
$ podman run --it --rm --entrypoint /usr/local/bin/jscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsearch

```bash
$ singularity exec <container> /usr/local/bin/jsearch
$ podman run --it --rm --entrypoint /usr/local/bin/jsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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