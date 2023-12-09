---
layout: container
name:  "quay.io/biocontainers/prophex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prophex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prophex/container.yaml"
updated_at: "2023-12-09 02:59:14.410817"
latest: "0.1.1--he4a0461_5"
container_url: "https://biocontainers.pro/tools/prophex"
aliases:
 - "prophex"
versions:
 - "0.1.1--h7132678_3"
 - "0.1.1--h7132678_4"
 - "0.1.1--he4a0461_5"
description: "shpc-registry automated BioContainers addition for prophex"
config: {"url": "https://biocontainers.pro/tools/prophex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prophex", "latest": {"0.1.1--he4a0461_5": "sha256:2ceb8948b221d46cf25f4af238c412d65b646ffbbd4b64da0b8cb48ab4daa976"}, "tags": {"0.1.1--h7132678_3": "sha256:d1e9926dbe7546f027d828acf08759bdbf80fce3cbbdaba00752e15e48cc619b", "0.1.1--h7132678_4": "sha256:198c57c974a4ec2dced0557018d7b29f40e3f67ced0cd5dc65554e506fa9a824", "0.1.1--he4a0461_5": "sha256:2ceb8948b221d46cf25f4af238c412d65b646ffbbd4b64da0b8cb48ab4daa976"}, "docker": "quay.io/biocontainers/prophex", "aliases": {"prophex": "/usr/local/bin/prophex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prophex.
shpc-registry automated BioContainers addition for prophex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prophex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prophex:0.1.1--he4a0461_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prophex/0.1.1--he4a0461_5
$ module help quay.io/biocontainers/prophex/0.1.1--he4a0461_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prophex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prophex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prophex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prophex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prophex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prophex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prophex

```bash
$ singularity exec <container> /usr/local/bin/prophex
$ podman run --it --rm --entrypoint /usr/local/bin/prophex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prophex   -v ${PWD} -w ${PWD} <container> -c " $@"
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