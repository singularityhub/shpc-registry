---
layout: container
name:  "quay.io/biocontainers/blockbuster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blockbuster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blockbuster/container.yaml"
updated_at: "2025-01-28 03:34:19.739416"
latest: "0.0.1.1--h7b50bb2_8"
container_url: "https://biocontainers.pro/tools/blockbuster"
aliases:
 - "blockbuster.x"
versions:
 - "0.0.1.1--hec16e2b_5"
 - "0.0.1.1--h031d066_7"
 - "0.0.1.1--h7b50bb2_8"
description: "shpc-registry automated BioContainers addition for blockbuster"
config: {"url": "https://biocontainers.pro/tools/blockbuster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blockbuster", "latest": {"0.0.1.1--h7b50bb2_8": "sha256:5f8a9ae196042055eed6fa4af8d7a7c8a04566fdf65f638981bf1ced3f559de5"}, "tags": {"0.0.1.1--hec16e2b_5": "sha256:041e1ad87f7767e493d2a9c916d54d191fbc58f8d201db435f5fae7b7aed61cf", "0.0.1.1--h031d066_7": "sha256:da731e2735871a827b3caa58f635b6216609a432cb67e5118b6fdbe17371114f", "0.0.1.1--h7b50bb2_8": "sha256:5f8a9ae196042055eed6fa4af8d7a7c8a04566fdf65f638981bf1ced3f559de5"}, "docker": "quay.io/biocontainers/blockbuster", "aliases": {"blockbuster.x": "/usr/local/bin/blockbuster.x"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blockbuster.
shpc-registry automated BioContainers addition for blockbuster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blockbuster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blockbuster:0.0.1.1--h7b50bb2_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blockbuster/0.0.1.1--h7b50bb2_8
$ module help quay.io/biocontainers/blockbuster/0.0.1.1--h7b50bb2_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blockbuster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blockbuster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blockbuster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blockbuster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blockbuster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blockbuster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blockbuster.x

```bash
$ singularity exec <container> /usr/local/bin/blockbuster.x
$ podman run --it --rm --entrypoint /usr/local/bin/blockbuster.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockbuster.x   -v ${PWD} -w ${PWD} <container> -c " $@"
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