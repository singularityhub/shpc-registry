---
layout: container
name:  "quay.io/biocontainers/ataqv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ataqv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ataqv/container.yaml"
updated_at: "2022-10-27 00:43:39.411746"
latest: "1.3.0--py27h5e5d24b_4"
container_url: "https://biocontainers.pro/tools/ataqv"
aliases:
 - "ataqv"
 - "mkarv"
 - "srvarv"
versions:
 - "1.3.0--py27h5e5d24b_4"
description: "shpc-registry automated BioContainers addition for ataqv"
config: {"url": "https://biocontainers.pro/tools/ataqv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ataqv", "latest": {"1.3.0--py27h5e5d24b_4": "sha256:e2a89c9badc8f52305001c6435da54fbf8576a55a5281a5a44e12ddc715c843f"}, "tags": {"1.3.0--py27h5e5d24b_4": "sha256:e2a89c9badc8f52305001c6435da54fbf8576a55a5281a5a44e12ddc715c843f"}, "docker": "quay.io/biocontainers/ataqv", "aliases": {"ataqv": "/usr/local/bin/ataqv", "mkarv": "/usr/local/bin/mkarv", "srvarv": "/usr/local/bin/srvarv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ataqv.
shpc-registry automated BioContainers addition for ataqv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ataqv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ataqv:1.3.0--py27h5e5d24b_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ataqv/1.3.0--py27h5e5d24b_4
$ module help quay.io/biocontainers/ataqv/1.3.0--py27h5e5d24b_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ataqv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ataqv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ataqv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ataqv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ataqv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ataqv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ataqv

```bash
$ singularity exec <container> /usr/local/bin/ataqv
$ podman run --it --rm --entrypoint /usr/local/bin/ataqv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ataqv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkarv

```bash
$ singularity exec <container> /usr/local/bin/mkarv
$ podman run --it --rm --entrypoint /usr/local/bin/mkarv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkarv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srvarv

```bash
$ singularity exec <container> /usr/local/bin/srvarv
$ podman run --it --rm --entrypoint /usr/local/bin/srvarv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srvarv   -v ${PWD} -w ${PWD} <container> -c " $@"
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