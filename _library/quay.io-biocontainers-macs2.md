---
layout: container
name:  "quay.io/biocontainers/macs2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/macs2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/macs2/container.yaml"
updated_at: "2025-10-08 03:48:12.625590"
latest: "2.2.9.1--py311haab0aaa_4"
container_url: "https://biocontainers.pro/tools/macs2"
aliases:
 - "macs2"
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "2.2.7.1--py38hbff2b2d_5"
 - "2.2.9.1--py38he5da3d1_0"
 - "2.2.9.1--py39hf95cd2a_0"
 - "2.2.9.1--py38h0020b31_1"
 - "2.2.9.1--py310h1fe012e_2"
 - "2.2.9.1--py39hbcbf7aa_3"
 - "2.2.9.1--py311haab0aaa_4"
description: "shpc-registry automated BioContainers addition for macs2"
config: {"url": "https://biocontainers.pro/tools/macs2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for macs2", "latest": {"2.2.9.1--py311haab0aaa_4": "sha256:6a3fca1b38c3a6fb8829708a7835c420302a91aa50b0c6e1df09d157fab31a1b"}, "tags": {"2.2.7.1--py38hbff2b2d_5": "sha256:dc79794e7724d93e9d8ccd1cc7f12f20027695a562fea2a85467c2c41e516b10", "2.2.9.1--py38he5da3d1_0": "sha256:2ced5035e7a83413034a77c12f5434fc35c823647431665e4ab2175afcc0445c", "2.2.9.1--py39hf95cd2a_0": "sha256:72c7bb1607500199d93008847805f7d6e035bd112237db6a0aff1edee1b79788", "2.2.9.1--py38h0020b31_1": "sha256:af9814c1ae91f811f35dce9033df57b28d6a4032d44eb5dba9ebe26539bf1deb", "2.2.9.1--py310h1fe012e_2": "sha256:92483b3cddae71c954853f38cee7ce1c49d0370d7624de051a8779275a2b8877", "2.2.9.1--py39hbcbf7aa_3": "sha256:626b8772df0f8814510a7020747bfad414b3fe61e766b9f146b87f32b2747efc", "2.2.9.1--py311haab0aaa_4": "sha256:6a3fca1b38c3a6fb8829708a7835c420302a91aa50b0c6e1df09d157fab31a1b"}, "docker": "quay.io/biocontainers/macs2", "aliases": {"macs2": "/usr/local/bin/macs2", "f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/macs2.
shpc-registry automated BioContainers addition for macs2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/macs2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/macs2:2.2.9.1--py311haab0aaa_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/macs2/2.2.9.1--py311haab0aaa_4
$ module help quay.io/biocontainers/macs2/2.2.9.1--py311haab0aaa_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### macs2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### macs2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### macs2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### macs2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### macs2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### macs2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### macs2

```bash
$ singularity exec <container> /usr/local/bin/macs2
$ podman run --it --rm --entrypoint /usr/local/bin/macs2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/macs2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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