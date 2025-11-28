---
layout: container
name:  "quay.io/biocontainers/crossfilt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crossfilt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crossfilt/container.yaml"
updated_at: "2025-11-28 03:45:02.564982"
latest: "0.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/crossfilt"
aliases:
 - "crossfilt-filter"
 - "crossfilt-lift"
 - "crossfilt-split"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.1.3--pyhdfd78af_0"
 - "0.1.5--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for crossfilt"
config: {"url": "https://biocontainers.pro/tools/crossfilt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for crossfilt", "latest": {"0.2.1--pyhdfd78af_0": "sha256:2b78e4ec5f4931f899be82271a371778dd6cf16c082227b91eb678ef63749818"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:420e1ea89aabd483ce2bf232a708a908f5a6360b9358fa56858eb0c3790a3753", "0.1.5--pyhdfd78af_0": "sha256:3e72aea13b5378e36d21acaf10e014a41654ffc2dbc99c30a978dfd5ea035660", "0.2.1--pyhdfd78af_0": "sha256:2b78e4ec5f4931f899be82271a371778dd6cf16c082227b91eb678ef63749818"}, "docker": "quay.io/biocontainers/crossfilt", "aliases": {"crossfilt-filter": "/usr/local/bin/crossfilt-filter", "crossfilt-lift": "/usr/local/bin/crossfilt-lift", "crossfilt-split": "/usr/local/bin/crossfilt-split", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crossfilt.
singularity registry hpc automated addition for crossfilt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crossfilt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crossfilt:0.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crossfilt/0.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/crossfilt/0.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crossfilt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crossfilt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crossfilt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crossfilt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crossfilt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crossfilt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crossfilt-filter

```bash
$ singularity exec <container> /usr/local/bin/crossfilt-filter
$ podman run --it --rm --entrypoint /usr/local/bin/crossfilt-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossfilt-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossfilt-lift

```bash
$ singularity exec <container> /usr/local/bin/crossfilt-lift
$ podman run --it --rm --entrypoint /usr/local/bin/crossfilt-lift   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossfilt-lift   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossfilt-split

```bash
$ singularity exec <container> /usr/local/bin/crossfilt-split
$ podman run --it --rm --entrypoint /usr/local/bin/crossfilt-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossfilt-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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