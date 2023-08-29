---
layout: container
name:  "quay.io/biocontainers/mapdamage2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mapdamage2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mapdamage2/container.yaml"
updated_at: "2023-08-29 03:20:19.936748"
latest: "2.2.2--pyr43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mapdamage2"
aliases:
 - "mapDamage"
 - "seqtk"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "gio-launch-desktop"
versions:
 - "2.2.1--pyr40_0"
 - "2.2.2--pyr43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for mapdamage2"
config: {"url": "https://biocontainers.pro/tools/mapdamage2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mapdamage2", "latest": {"2.2.2--pyr43hdfd78af_0": "sha256:d2a88384d7082e3f0ef42eef072421b847e839809196f07185f5064c95bcc6ca"}, "tags": {"2.2.1--pyr40_0": "sha256:12d0be7dba8a81b937faf6a78dbf8b6c80efcb4840fb6b2e2bb95db5982daeaf", "2.2.2--pyr43hdfd78af_0": "sha256:d2a88384d7082e3f0ef42eef072421b847e839809196f07185f5064c95bcc6ca"}, "docker": "quay.io/biocontainers/mapdamage2", "aliases": {"mapDamage": "/usr/local/bin/mapDamage", "seqtk": "/usr/local/bin/seqtk", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mapdamage2.
shpc-registry automated BioContainers addition for mapdamage2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mapdamage2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mapdamage2:2.2.2--pyr43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mapdamage2/2.2.2--pyr43hdfd78af_0
$ module help quay.io/biocontainers/mapdamage2/2.2.2--pyr43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mapdamage2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mapdamage2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mapdamage2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mapdamage2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mapdamage2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mapdamage2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mapDamage

```bash
$ singularity exec <container> /usr/local/bin/mapDamage
$ podman run --it --rm --entrypoint /usr/local/bin/mapDamage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapDamage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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