---
layout: container
name:  "quay.io/biocontainers/classpro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/classpro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/classpro/container.yaml"
updated_at: "2025-08-12 03:28:35.414007"
latest: "1.0.2--hda11466_1"
container_url: "https://biocontainers.pro/tools/classpro"
aliases:
 - "ClassGS"
 - "ClassPro"
 - "class2acc"
 - "class2cns"
 - "prof2class"
versions:
 - "1.0.2--hfeaf35a_0"
 - "1.0.2--hda11466_1"
description: "singularity registry hpc automated addition for classpro"
config: {"url": "https://biocontainers.pro/tools/classpro", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for classpro", "latest": {"1.0.2--hda11466_1": "sha256:8a6b198d2826163771f00e22f3af0df206e119fa7a1347b8490858f83a0d8c9f"}, "tags": {"1.0.2--hfeaf35a_0": "sha256:5c0e2aae262cf009a70cbe698ccbd01d9d4744437aedac4cf27c53a646503916", "1.0.2--hda11466_1": "sha256:8a6b198d2826163771f00e22f3af0df206e119fa7a1347b8490858f83a0d8c9f"}, "docker": "quay.io/biocontainers/classpro", "aliases": {"ClassGS": "/usr/local/bin/ClassGS", "ClassPro": "/usr/local/bin/ClassPro", "class2acc": "/usr/local/bin/class2acc", "class2cns": "/usr/local/bin/class2cns", "prof2class": "/usr/local/bin/prof2class"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/classpro.
singularity registry hpc automated addition for classpro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/classpro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/classpro:1.0.2--hda11466_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/classpro/1.0.2--hda11466_1
$ module help quay.io/biocontainers/classpro/1.0.2--hda11466_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### classpro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### classpro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### classpro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### classpro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### classpro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### classpro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ClassGS

```bash
$ singularity exec <container> /usr/local/bin/ClassGS
$ podman run --it --rm --entrypoint /usr/local/bin/ClassGS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ClassGS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ClassPro

```bash
$ singularity exec <container> /usr/local/bin/ClassPro
$ podman run --it --rm --entrypoint /usr/local/bin/ClassPro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ClassPro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### class2acc

```bash
$ singularity exec <container> /usr/local/bin/class2acc
$ podman run --it --rm --entrypoint /usr/local/bin/class2acc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/class2acc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### class2cns

```bash
$ singularity exec <container> /usr/local/bin/class2cns
$ podman run --it --rm --entrypoint /usr/local/bin/class2cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/class2cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prof2class

```bash
$ singularity exec <container> /usr/local/bin/prof2class
$ podman run --it --rm --entrypoint /usr/local/bin/prof2class   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prof2class   -v ${PWD} -w ${PWD} <container> -c " $@"
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