---
layout: container
name:  "quay.io/biocontainers/bitmapperbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bitmapperbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bitmapperbs/container.yaml"
updated_at: "2024-05-27 03:41:30.953455"
latest: "1.0.2.3--hf5e1c6e_5"
container_url: "https://biocontainers.pro/tools/bitmapperbs"
aliases:
 - "bitmapperBS"
 - "psascan"
versions:
 - "1.0.2.3--h468198e_4"
 - "1.0.2.3--hf5e1c6e_5"
description: "shpc-registry automated BioContainers addition for bitmapperbs"
config: {"url": "https://biocontainers.pro/tools/bitmapperbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bitmapperbs", "latest": {"1.0.2.3--hf5e1c6e_5": "sha256:0338c4d3ef48be113a716d105822c07c36abd31a0817245d4c822aa707665f06"}, "tags": {"1.0.2.3--h468198e_4": "sha256:a2c4b026457f7f033c62f5a5c85413b478737039a20b1903625321f2b35cbdf9", "1.0.2.3--hf5e1c6e_5": "sha256:0338c4d3ef48be113a716d105822c07c36abd31a0817245d4c822aa707665f06"}, "docker": "quay.io/biocontainers/bitmapperbs", "aliases": {"bitmapperBS": "/usr/local/bin/bitmapperBS", "psascan": "/usr/local/bin/psascan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bitmapperbs.
shpc-registry automated BioContainers addition for bitmapperbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bitmapperbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bitmapperbs:1.0.2.3--hf5e1c6e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bitmapperbs/1.0.2.3--hf5e1c6e_5
$ module help quay.io/biocontainers/bitmapperbs/1.0.2.3--hf5e1c6e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bitmapperbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bitmapperbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bitmapperbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bitmapperbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bitmapperbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bitmapperbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bitmapperBS

```bash
$ singularity exec <container> /usr/local/bin/bitmapperBS
$ podman run --it --rm --entrypoint /usr/local/bin/bitmapperBS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bitmapperBS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psascan

```bash
$ singularity exec <container> /usr/local/bin/psascan
$ podman run --it --rm --entrypoint /usr/local/bin/psascan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psascan   -v ${PWD} -w ${PWD} <container> -c " $@"
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