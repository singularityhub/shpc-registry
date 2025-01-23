---
layout: container
name:  "quay.io/biocontainers/sniffles"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sniffles/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sniffles/container.yaml"
updated_at: "2025-01-23 03:26:11.735596"
latest: "2.5.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sniffles"
aliases:
 - "sniffles"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "2.0.7--pyhdfd78af_0"
 - "2.2--pyhdfd78af_0"
 - "2.3.2--pyhdfd78af_1"
 - "2.3.3--pyhdfd78af_0"
 - "2.4--pyhdfd78af_0"
 - "2.5.2--pyhdfd78af_0"
 - "2.5.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for sniffles"
config: {"url": "https://biocontainers.pro/tools/sniffles", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sniffles", "latest": {"2.5.3--pyhdfd78af_0": "sha256:dc26bf009abd20786cfc44c40aa2f3dacf12c905f1ad3d3f33da24a02ca7cf7e"}, "tags": {"2.0.7--pyhdfd78af_0": "sha256:94157be1208ad01a748e68fd6a5d88b29c515136c31908fcf51bee11f687a769", "2.2--pyhdfd78af_0": "sha256:feb1c41eae608ebc2c2cb594144bb3c221b87d9bb691d0af6ad06b49fd54573a", "2.3.2--pyhdfd78af_1": "sha256:441c6a4e7e98174ecdc2af4e2c79fbddabd307c63c821e2f408b9ce6a21e9f19", "2.3.3--pyhdfd78af_0": "sha256:f90f43f4b292a05c980ec801edcca5ec2e6080f946f5e955fe70cc2d9d16a723", "2.4--pyhdfd78af_0": "sha256:62c8865168e9d6de67615a06f6b20f2a9e4bc65b4349d7ae4c75d17d22d82597", "2.5.2--pyhdfd78af_0": "sha256:578ae5bfc8147b9aac0687efbbacea9d6e9db7c7a4741554bae4a99643272953", "2.5.3--pyhdfd78af_0": "sha256:dc26bf009abd20786cfc44c40aa2f3dacf12c905f1ad3d3f33da24a02ca7cf7e"}, "docker": "quay.io/biocontainers/sniffles", "aliases": {"sniffles": "/usr/local/bin/sniffles", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sniffles.
shpc-registry automated BioContainers addition for sniffles
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sniffles
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sniffles:2.5.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sniffles/2.5.3--pyhdfd78af_0
$ module help quay.io/biocontainers/sniffles/2.5.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sniffles-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sniffles-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sniffles-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sniffles-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sniffles-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sniffles-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sniffles

```bash
$ singularity exec <container> /usr/local/bin/sniffles
$ podman run --it --rm --entrypoint /usr/local/bin/sniffles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sniffles   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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