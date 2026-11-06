---
layout: container
name:  "quay.io/biocontainers/recore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/recore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/recore/container.yaml"
updated_at: "2026-11-06 18:21:31.737788"
latest: "1.0.0--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/recore"
aliases:
 - "recore"
 - "sdust"
 - "paftools.js"
 - "k8"
 - "minimap2"
 - "x86_64-conda-linux-gnu.cfg"
versions:
 - "1.0.0--hab7d0fd_0"
description: "singularity registry hpc automated addition for recore"
config: {"url": "https://biocontainers.pro/tools/recore", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for recore", "latest": {"1.0.0--hab7d0fd_0": "sha256:feffa4d7f7c4a636dae0ed508ce9ef33e81a496048bdfb2326e18a660a0256ec"}, "tags": {"1.0.0--hab7d0fd_0": "sha256:feffa4d7f7c4a636dae0ed508ce9ef33e81a496048bdfb2326e18a660a0256ec"}, "docker": "quay.io/biocontainers/recore", "aliases": {"recore": "/usr/local/bin/recore", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "k8": "/usr/local/bin/k8", "minimap2": "/usr/local/bin/minimap2", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/recore.
singularity registry hpc automated addition for recore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/recore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/recore:1.0.0--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/recore/1.0.0--hab7d0fd_0
$ module help quay.io/biocontainers/recore/1.0.0--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### recore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### recore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### recore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### recore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### recore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### recore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### recore

```bash
$ singularity exec <container> /usr/local/bin/recore
$ podman run --it --rm --entrypoint /usr/local/bin/recore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
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