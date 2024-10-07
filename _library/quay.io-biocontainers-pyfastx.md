---
layout: container
name:  "quay.io/biocontainers/pyfastx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyfastx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyfastx/container.yaml"
updated_at: "2024-10-07 03:26:17.564930"
latest: "2.1.0--py38h6bfa29d_3"
container_url: "https://biocontainers.pro/tools/pyfastx"
aliases:
 - "pyfastx"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.8.4--py38h4c6a040_1"
 - "2.1.0--py38h7cf9df2_0"
 - "2.0.2--py310h83093d7_0"
 - "1.1.0--py310h83093d7_3"
 - "1.0.1--py310h8472f5a_0"
 - "0.9.1--py310h8472f5a_0"
 - "2.1.0--py38h7cf9df2_1"
 - "2.1.0--py311h0152c62_2"
 - "2.1.0--py38h6bfa29d_3"
description: "shpc-registry automated BioContainers addition for pyfastx"
config: {"url": "https://biocontainers.pro/tools/pyfastx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyfastx", "latest": {"2.1.0--py38h6bfa29d_3": "sha256:83c58a5c84a9334aae7408ea373aa3c87ff53a45923d9caf06121f65a9ae678a"}, "tags": {"0.8.4--py38h4c6a040_1": "sha256:bea6d8242020df2cce630454adc91ff35ae182d9e9e516a9d1f4d64deda73cd7", "2.1.0--py38h7cf9df2_0": "sha256:f34d935114cb46ca94f5ed57d0c01d556f6e80f5c051b6740f950464e41c38c1", "2.0.2--py310h83093d7_0": "sha256:249797adbbaff4c586e4dd253669d9380e6833722b362261d2c49c475f2754dd", "1.1.0--py310h83093d7_3": "sha256:dfe659d377b1f7d1789063b409cfc9523de2706dc029435345d4ec8e42669a4c", "1.0.1--py310h8472f5a_0": "sha256:69f74c404b57677d290236558e92b4a3a15103f615bb2d7b30a55aebb77e0e4b", "0.9.1--py310h8472f5a_0": "sha256:c6643f412211a53846117160ae213471cf600282d2440952370d9462f27a1093", "2.1.0--py38h7cf9df2_1": "sha256:dea21a6a462306831ae9ce6843aae4b2151bc0cabd056db57e33453ceea9fb7e", "2.1.0--py311h0152c62_2": "sha256:122bed71a9d0e92e51c98be3bfa359cb81043680175ee4f0be8ac6453db0cfae", "2.1.0--py38h6bfa29d_3": "sha256:83c58a5c84a9334aae7408ea373aa3c87ff53a45923d9caf06121f65a9ae678a"}, "docker": "quay.io/biocontainers/pyfastx", "aliases": {"pyfastx": "/usr/local/bin/pyfastx", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyfastx.
shpc-registry automated BioContainers addition for pyfastx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyfastx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyfastx:2.1.0--py38h6bfa29d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyfastx/2.1.0--py38h6bfa29d_3
$ module help quay.io/biocontainers/pyfastx/2.1.0--py38h6bfa29d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyfastx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyfastx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyfastx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyfastx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyfastx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyfastx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyfastx

```bash
$ singularity exec <container> /usr/local/bin/pyfastx
$ podman run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
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