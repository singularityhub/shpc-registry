---
layout: container
name:  "quay.io/biocontainers/gmm-demux"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmm-demux/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gmm-demux/container.yaml"
updated_at: "2025-01-26 03:05:04.177843"
latest: "0.2.2.3--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/gmm-demux"
aliases:
 - "GMM-demux"
 - "tabulate"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.2.2.3--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for gmm-demux"
config: {"url": "https://biocontainers.pro/tools/gmm-demux", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gmm-demux", "latest": {"0.2.2.3--pyh7cba7a3_0": "sha256:f69abf68d19ba6a8e653a69b75360c25ab5af36c75fb580df70bdbf900f96f56"}, "tags": {"0.2.2.3--pyh7cba7a3_0": "sha256:f69abf68d19ba6a8e653a69b75360c25ab5af36c75fb580df70bdbf900f96f56"}, "docker": "quay.io/biocontainers/gmm-demux", "aliases": {"GMM-demux": "/usr/local/bin/GMM-demux", "tabulate": "/usr/local/bin/tabulate", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmm-demux.
singularity registry hpc automated addition for gmm-demux
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmm-demux
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmm-demux:0.2.2.3--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmm-demux/0.2.2.3--pyh7cba7a3_0
$ module help quay.io/biocontainers/gmm-demux/0.2.2.3--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmm-demux-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmm-demux-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmm-demux-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmm-demux-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmm-demux-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmm-demux-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GMM-demux

```bash
$ singularity exec <container> /usr/local/bin/GMM-demux
$ podman run --it --rm --entrypoint /usr/local/bin/GMM-demux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMM-demux   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
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