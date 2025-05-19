---
layout: container
name:  "quay.io/biocontainers/cyvcf2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cyvcf2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cyvcf2/container.yaml"
updated_at: "2025-05-19 03:44:23.518986"
latest: "0.31.1--py311h94e71d4_1"
container_url: "https://biocontainers.pro/tools/cyvcf2"
aliases:
 - "cyvcf2"
 - "coloredlogs"
 - "humanfriendly"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
versions:
 - "0.8.4--py36h355e19c_4"
 - "0.10.8--py36hbbd59f4_2"
 - "0.30.28--py39h7ec6a44_1"
 - "0.20.9--py38h00803a1_0"
 - "0.11.7--py37hce88a48_0"
 - "0.10.10--py36hbbd59f4_0"
 - "0.8.4--py27h355e19c_4"
 - "0.31.0--py312h16c6d63_1"
 - "0.10.10--py37hbbd59f4_0"
 - "0.31.1--py311h94e71d4_0"
 - "0.31.1--py311h94e71d4_1"
description: "shpc-registry automated BioContainers addition for cyvcf2"
config: {"url": "https://biocontainers.pro/tools/cyvcf2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cyvcf2", "latest": {"0.31.1--py311h94e71d4_1": "sha256:afedf8360e16fdeeddef18cb77d158d8e06e5fd2c734c27b3675aa0d743784b7"}, "tags": {"0.8.4--py36h355e19c_4": "sha256:5f1ffb1a1642e043f4e6bb7daa882ae20cad89db9f10b57b59b69b9acb9606b4", "0.10.8--py36hbbd59f4_2": "sha256:0a5ca70ce80cf0f3c31e3c25c1eff7961ec2b9b8379e79cca458549035853629", "0.30.28--py39h7ec6a44_1": "sha256:6f4dde8e0d34c450af2bf8cb62e41e5b3da2875dfbaa69699b3c1f8eab3627bf", "0.20.9--py38h00803a1_0": "sha256:17b75f1b5bd4076db8295af381b317a6afb9087714c825efc822bcff4c55a80a", "0.11.7--py37hce88a48_0": "sha256:238c669d0fcaab8c18c6ee5fa2d049ee79e39a8e0c0ef2401e08915160182881", "0.10.10--py36hbbd59f4_0": "sha256:fae7acdab5a188f193c5ee87d6ecc19ae53b9c180108d370ecedcdde5b553099", "0.8.4--py27h355e19c_4": "sha256:1568592b7934e88b41de68f15ef17a331d8dc2b128e37d4b687a5a027e8aab59", "0.31.0--py312h16c6d63_1": "sha256:9a59c60e3c54770c19f314155c35d610cdafa174c6a03c1dfa55f8f3609b7397", "0.10.10--py37hbbd59f4_0": "sha256:0689328d53636468446e161f4d0ef6f82720b76ac1c12d008eaac27cbaa9febf", "0.31.1--py311h94e71d4_0": "sha256:a2c56a490a87acb37b61e2b2a99f32b45c08920fbd6c1d6cc09dbebf01641719", "0.31.1--py311h94e71d4_1": "sha256:afedf8360e16fdeeddef18cb77d158d8e06e5fd2c734c27b3675aa0d743784b7"}, "docker": "quay.io/biocontainers/cyvcf2", "aliases": {"cyvcf2": "/usr/local/bin/cyvcf2", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cyvcf2.
shpc-registry automated BioContainers addition for cyvcf2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cyvcf2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cyvcf2:0.31.1--py311h94e71d4_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cyvcf2/0.31.1--py311h94e71d4_1
$ module help quay.io/biocontainers/cyvcf2/0.31.1--py311h94e71d4_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cyvcf2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cyvcf2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cyvcf2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cyvcf2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cyvcf2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cyvcf2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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