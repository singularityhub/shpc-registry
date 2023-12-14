---
layout: container
name:  "ghcr.io/autamus/py-libensemble"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/py-libensemble/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/py-libensemble/container.yaml"
updated_at: "2023-12-14 03:13:08.556414"
latest: "0.9.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/py-libensemble"

versions:
 - "0.7.2"
 - "0.8.0"
 - "latest"
 - "0.9.3"
description: "Library for managing ensemble-like collections of computations."
config: {"docker": "ghcr.io/autamus/py-libensemble", "url": "https://github.com/orgs/autamus/packages/container/package/py-libensemble", "maintainer": "@vsoch", "description": "Library for managing ensemble-like collections of computations.", "latest": {"0.9.3": "sha256:f36fa5319ce2c2098a8ea7a5dc0a1bd8eaa0e72d010a0e38d405a8eefa70c586"}, "tags": {"0.7.2": "sha256:590852c32b8b4e5ea6dc5d6909a64f3128f972b062eb362ee5ee3d2c51840b99", "0.8.0": "sha256:b594a04013badc5866635d4d4ade3c21acba4540fa4fa082d7fbb4fc1fc193fb", "latest": "sha256:f36fa5319ce2c2098a8ea7a5dc0a1bd8eaa0e72d010a0e38d405a8eefa70c586", "0.9.3": "sha256:f36fa5319ce2c2098a8ea7a5dc0a1bd8eaa0e72d010a0e38d405a8eefa70c586"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/py-libensemble.
Library for managing ensemble-like collections of computations.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/py-libensemble
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/py-libensemble:0.9.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/py-libensemble/0.9.3
$ module help ghcr.io/autamus/py-libensemble/0.9.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### py-libensemble-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### py-libensemble-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### py-libensemble-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### py-libensemble-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### py-libensemble-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### py-libensemble-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### py-libensemble

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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