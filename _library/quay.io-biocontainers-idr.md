---
layout: container
name:  "quay.io/biocontainers/idr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/idr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/idr/container.yaml"
updated_at: "2024-01-08 03:05:27.325209"
latest: "2.0.4.2--py39hec16e2b_10"
container_url: "https://biocontainers.pro/tools/idr"

versions:
 - "2.0.4.2--py310h79ef01b_7"
 - "2.0.4.2--py310hd6be1da_9"
 - "2.0.4.2--py39hec16e2b_10"
description: "shpc-registry automated BioContainers addition for idr"
config: {"url": "https://biocontainers.pro/tools/idr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for idr", "latest": {"2.0.4.2--py39hec16e2b_10": "sha256:dda3970b287259f6de70d18b6c24f11eab3efdf0207175334e0c19b0f5df374f"}, "tags": {"2.0.4.2--py310h79ef01b_7": "sha256:da07c884c7b8debefb1422a91c63a45647a029dd8e7b0674578d36bc5f03f5f9", "2.0.4.2--py310hd6be1da_9": "sha256:06d16c46e2ffb311eadb4ec7b6dd572a472b61ff0d7e851cfb00a5d124d4d306", "2.0.4.2--py39hec16e2b_10": "sha256:dda3970b287259f6de70d18b6c24f11eab3efdf0207175334e0c19b0f5df374f"}, "docker": "quay.io/biocontainers/idr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/idr.
shpc-registry automated BioContainers addition for idr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/idr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/idr:2.0.4.2--py39hec16e2b_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/idr/2.0.4.2--py39hec16e2b_10
$ module help quay.io/biocontainers/idr/2.0.4.2--py39hec16e2b_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### idr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### idr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### idr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### idr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### idr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### idr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### idr

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