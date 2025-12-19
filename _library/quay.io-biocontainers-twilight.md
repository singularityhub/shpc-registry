---
layout: container
name:  "quay.io/biocontainers/twilight"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/twilight/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/twilight/container.yaml"
updated_at: "2025-12-19 05:22:26.781078"
latest: "0.2.2--h6bb9b41_0"
container_url: "https://biocontainers.pro/tools/twilight"
aliases:
 - "twilight"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.1.1--h5ca1c30_0"
 - "0.1.2--h5ca1c30_1"
 - "0.1.3--h6bb9b41_2"
 - "0.1.4--h6bb9b41_0"
 - "0.1.4a--h6bb9b41_0"
 - "0.2.0--h6bb9b41_0"
 - "0.2.1--h6bb9b41_0"
 - "0.2.2--h6bb9b41_0"
description: "singularity registry hpc automated addition for twilight"
config: {"url": "https://biocontainers.pro/tools/twilight", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for twilight", "latest": {"0.2.2--h6bb9b41_0": "sha256:3070eb896e72f75b48a9ddcf509e292ebe0b95068e64b293340e28b178449624"}, "tags": {"0.1.1--h5ca1c30_0": "sha256:5f9fc2cf6f69becab69808399ecc7b236dc7addb60733ff5ff0c7fadff604e8d", "0.1.2--h5ca1c30_1": "sha256:71f29b4dc9e76102ed490735b0f5d67919c63d6ab18f062d2d6d05361ef7fc71", "0.1.3--h6bb9b41_2": "sha256:53a3fdf599337607fb8661c24184aa0f5db54a82547ccddde7787c447b829012", "0.1.4--h6bb9b41_0": "sha256:f22960b03460001376d1b378f8f0bc3e417747c9b9674738520dba0417e8e301", "0.1.4a--h6bb9b41_0": "sha256:9312306a40414223a3e58e2b867b3727e1918896895cddcb84f0f738e30ca876", "0.2.0--h6bb9b41_0": "sha256:e70406464184591ef0a5beec4dbb57349fc66d2bd5075358220d3a2ec7e730a2", "0.2.1--h6bb9b41_0": "sha256:c556b1e4dccc57c62208709be622f2e877bb6fbd0ac588282c1ba007d99a5b9c", "0.2.2--h6bb9b41_0": "sha256:3070eb896e72f75b48a9ddcf509e292ebe0b95068e64b293340e28b178449624"}, "docker": "quay.io/biocontainers/twilight", "aliases": {"twilight": "/usr/local/bin/twilight", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/twilight.
singularity registry hpc automated addition for twilight
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/twilight
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/twilight:0.2.2--h6bb9b41_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/twilight/0.2.2--h6bb9b41_0
$ module help quay.io/biocontainers/twilight/0.2.2--h6bb9b41_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### twilight-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### twilight-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### twilight-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### twilight-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### twilight-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### twilight-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### twilight

```bash
$ singularity exec <container> /usr/local/bin/twilight
$ podman run --it --rm --entrypoint /usr/local/bin/twilight   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twilight   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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