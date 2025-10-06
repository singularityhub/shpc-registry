---
layout: container
name:  "quay.io/biocontainers/mlrho"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mlrho/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mlrho/container.yaml"
updated_at: "2025-10-06 03:25:35.455985"
latest: "2.9--h2d4b398_9"
container_url: "https://biocontainers.pro/tools/mlrho"
aliases:
 - "mlRho"
versions:
 - "2.9--hde3ca97_6"
 - "2.9--hde3ca97_7"
 - "2.9--h95f4acd_8"
 - "2.9--h2d4b398_9"
description: "shpc-registry automated BioContainers addition for mlrho"
config: {"url": "https://biocontainers.pro/tools/mlrho", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mlrho", "latest": {"2.9--h2d4b398_9": "sha256:209d66a2e4669eec66cfc6630cb9178c4573bb899a08ded0918ce85953372b87"}, "tags": {"2.9--hde3ca97_6": "sha256:940a6a493ecca35cd3a585f2f62faf465193f054311183146c30de13327b1cae", "2.9--hde3ca97_7": "sha256:f88f61d4152a07fa3a69e31db3702233c3fcdb61f59307382e063300c9248bc0", "2.9--h95f4acd_8": "sha256:86771317af267aa38998e057135db0dbe7d31f8cc32162bb0e63571052523e71", "2.9--h2d4b398_9": "sha256:209d66a2e4669eec66cfc6630cb9178c4573bb899a08ded0918ce85953372b87"}, "docker": "quay.io/biocontainers/mlrho", "aliases": {"mlRho": "/usr/local/bin/mlRho"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mlrho.
shpc-registry automated BioContainers addition for mlrho
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mlrho
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mlrho:2.9--h2d4b398_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mlrho/2.9--h2d4b398_9
$ module help quay.io/biocontainers/mlrho/2.9--h2d4b398_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mlrho-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mlrho-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mlrho-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mlrho-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mlrho-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mlrho-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mlRho

```bash
$ singularity exec <container> /usr/local/bin/mlRho
$ podman run --it --rm --entrypoint /usr/local/bin/mlRho   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlRho   -v ${PWD} -w ${PWD} <container> -c " $@"
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