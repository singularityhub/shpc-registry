---
layout: container
name:  "quay.io/biocontainers/pydna_repeatfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pydna_repeatfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pydna_repeatfinder/container.yaml"
updated_at: "2024-08-25 02:46:23.279788"
latest: "0.2.9--py310h84f13bb_1"
container_url: "https://biocontainers.pro/tools/pydna_repeatfinder"
aliases:
 - "pydna_repeatfinder"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2.9--py310h84f13bb_1"
 - "0.2.9--py38h2123bcc_1"
description: "singularity registry hpc automated addition for pydna_repeatfinder"
config: {"url": "https://biocontainers.pro/tools/pydna_repeatfinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pydna_repeatfinder", "latest": {"0.2.9--py310h84f13bb_1": "sha256:98429700526e08da2409406cee03c58f1ad95b7f3c85446da2c0b454a1fc0962"}, "tags": {"0.2.9--py310h84f13bb_1": "sha256:98429700526e08da2409406cee03c58f1ad95b7f3c85446da2c0b454a1fc0962", "0.2.9--py38h2123bcc_1": "sha256:3c3364ad2808a79e391a97a8fc7e1f300210da9b8978bab8d47a8d60cb974e28"}, "docker": "quay.io/biocontainers/pydna_repeatfinder", "aliases": {"pydna_repeatfinder": "/usr/local/bin/pydna_repeatfinder", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pydna_repeatfinder.
singularity registry hpc automated addition for pydna_repeatfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pydna_repeatfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pydna_repeatfinder:0.2.9--py310h84f13bb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pydna_repeatfinder/0.2.9--py310h84f13bb_1
$ module help quay.io/biocontainers/pydna_repeatfinder/0.2.9--py310h84f13bb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pydna_repeatfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pydna_repeatfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pydna_repeatfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pydna_repeatfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pydna_repeatfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pydna_repeatfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pydna_repeatfinder

```bash
$ singularity exec <container> /usr/local/bin/pydna_repeatfinder
$ podman run --it --rm --entrypoint /usr/local/bin/pydna_repeatfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydna_repeatfinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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