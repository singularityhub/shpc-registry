---
layout: container
name:  "quay.io/biocontainers/macrel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/macrel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/macrel/container.yaml"
updated_at: "2024-11-12 03:31:46.698004"
latest: "1.5.0--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/macrel"
aliases:
 - "macrel"
 - "ngless"
 - "paladin"
 - "pyrodigal"
 - "megahit_core"
 - "megahit_core_no_hw_accel"
 - "megahit_core_popcnt"
 - "megahit"
 - "megahit_toolkit"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
versions:
 - "1.2.0--pyh5e36f6f_0"
 - "1.2.0--pyhdfd78af_1"
 - "1.3.0--pyh7cba7a3_0"
 - "1.4.0--pyh7e72e81_0"
 - "1.5.0--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for macrel"
config: {"url": "https://biocontainers.pro/tools/macrel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for macrel", "latest": {"1.5.0--pyh7e72e81_0": "sha256:d80a8e86c5ab00d08414d2c64e3f872429b73754fb1dc8b1c8da2fbda62764d1"}, "tags": {"1.2.0--pyh5e36f6f_0": "sha256:13ccbe1e380e2536687663f55046fdd14f9bc663f9b19dfea70155f9ea59cf99", "1.2.0--pyhdfd78af_1": "sha256:5fc52ca4e7509e82e984346d4f1331c0caa95ca8549ebd13d37aee462b638079", "1.3.0--pyh7cba7a3_0": "sha256:92fd920873e4019499d24d79171eb8aed9c87ab8818511690b877e8225dedd3c", "1.4.0--pyh7e72e81_0": "sha256:7c3b14a71d0c1d1a137a6b54590bf280f34238cdb8bd6c9a794f122fcf418767", "1.5.0--pyh7e72e81_0": "sha256:d80a8e86c5ab00d08414d2c64e3f872429b73754fb1dc8b1c8da2fbda62764d1"}, "docker": "quay.io/biocontainers/macrel", "aliases": {"macrel": "/usr/local/bin/macrel", "ngless": "/usr/local/bin/ngless", "paladin": "/usr/local/bin/paladin", "pyrodigal": "/usr/local/bin/pyrodigal", "megahit_core": "/usr/local/bin/megahit_core", "megahit_core_no_hw_accel": "/usr/local/bin/megahit_core_no_hw_accel", "megahit_core_popcnt": "/usr/local/bin/megahit_core_popcnt", "megahit": "/usr/local/bin/megahit", "megahit_toolkit": "/usr/local/bin/megahit_toolkit", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/macrel.
shpc-registry automated BioContainers addition for macrel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/macrel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/macrel:1.5.0--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/macrel/1.5.0--pyh7e72e81_0
$ module help quay.io/biocontainers/macrel/1.5.0--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### macrel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### macrel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### macrel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### macrel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### macrel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### macrel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### macrel

```bash
$ singularity exec <container> /usr/local/bin/macrel
$ podman run --it --rm --entrypoint /usr/local/bin/macrel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macrel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngless

```bash
$ singularity exec <container> /usr/local/bin/ngless
$ podman run --it --rm --entrypoint /usr/local/bin/ngless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paladin

```bash
$ singularity exec <container> /usr/local/bin/paladin
$ podman run --it --rm --entrypoint /usr/local/bin/paladin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paladin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_no_hw_accel

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_no_hw_accel
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_popcnt

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_popcnt
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit

```bash
$ singularity exec <container> /usr/local/bin/megahit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_toolkit

```bash
$ singularity exec <container> /usr/local/bin/megahit_toolkit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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