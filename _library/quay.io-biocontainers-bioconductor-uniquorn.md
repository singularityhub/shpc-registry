---
layout: container
name:  "quay.io/biocontainers/bioconductor-uniquorn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-uniquorn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-uniquorn/container.yaml"
updated_at: "2025-10-25 03:21:04.773793"
latest: "2.26.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-uniquorn"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r40_0"
 - "2.18.0--r42hdfd78af_0"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.0--r41hdfd78af_0"
 - "2.10.0--r40hdfd78af_1"
 - "2.20.0--r43hdfd78af_0"
 - "2.22.0--r43hdfd78af_0"
 - "2.26.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-uniquorn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-uniquorn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-uniquorn", "latest": {"2.26.0--r44hdfd78af_0": "sha256:bca560a70243a3ffe3bec02ac10659e3c442f175b781219555b67906d9865301"}, "tags": {"2.8.0--r40_0": "sha256:8fc224c01bd3adb5ac9587a49092eb5917eff74bb7b7eacc237d6bc1c3f49cb8", "2.18.0--r42hdfd78af_0": "sha256:f79c44d69e58b3e6e49da118391fe72ee374df7cde71d364ec2b1be72c17d634", "2.14.0--r41hdfd78af_0": "sha256:c5e9647ef71857869d661da858d0a0fd0c70fbabb6c821e49a9c6c87e44c0316", "2.12.0--r41hdfd78af_0": "sha256:5521f1c09dd9804df1e21bcb853360ea5339c4696987ea749f8063e82990bf3f", "2.10.0--r40hdfd78af_1": "sha256:f5c8facdfd949c4bd414952a35e740126b9d19651b36c9297600a12bcf9c83c3", "2.20.0--r43hdfd78af_0": "sha256:0e3aadf7d450270d4eaf87ff3f00039e92c92016a587c0124b62b4c8d2f91fb3", "2.22.0--r43hdfd78af_0": "sha256:eb5c8e889fcdfa299cb03595b86c668791c90432e9e1c99a3488dbc7797b079e", "2.26.0--r44hdfd78af_0": "sha256:bca560a70243a3ffe3bec02ac10659e3c442f175b781219555b67906d9865301"}, "docker": "quay.io/biocontainers/bioconductor-uniquorn", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-uniquorn.
shpc-registry automated BioContainers addition for bioconductor-uniquorn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-uniquorn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-uniquorn:2.26.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-uniquorn/2.26.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-uniquorn/2.26.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-uniquorn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-uniquorn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-uniquorn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-uniquorn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-uniquorn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-uniquorn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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