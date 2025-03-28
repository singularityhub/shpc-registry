---
layout: container
name:  "quay.io/biocontainers/seqan_tcoffee"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqan_tcoffee/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqan_tcoffee/container.yaml"
updated_at: "2025-03-28 03:24:47.051097"
latest: "1.13.8--haf24da9_5"
container_url: "https://biocontainers.pro/tools/seqan_tcoffee"
aliases:
 - "seqan_tcoffee"
versions:
 - "1.13.8--h19e8d03_2"
 - "1.13.8--h6dccd9a_4"
 - "1.13.8--haf24da9_5"
description: "shpc-registry automated BioContainers addition for seqan_tcoffee"
config: {"url": "https://biocontainers.pro/tools/seqan_tcoffee", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqan_tcoffee", "latest": {"1.13.8--haf24da9_5": "sha256:aa30e77d933b3d6dd1b81068d5e939580f2c7839a6f26b49593f1a24a5c981f5"}, "tags": {"1.13.8--h19e8d03_2": "sha256:f6e7db8052671cecc4f31871811b21b66b6b92229554313e1da7e39578eaa653", "1.13.8--h6dccd9a_4": "sha256:d223201425dc8b43c1eef3b2acf99b8b55aa740b70f82bec71076d2c2cad75d5", "1.13.8--haf24da9_5": "sha256:aa30e77d933b3d6dd1b81068d5e939580f2c7839a6f26b49593f1a24a5c981f5"}, "docker": "quay.io/biocontainers/seqan_tcoffee", "aliases": {"seqan_tcoffee": "/usr/local/bin/seqan_tcoffee"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqan_tcoffee.
shpc-registry automated BioContainers addition for seqan_tcoffee
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqan_tcoffee
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqan_tcoffee:1.13.8--haf24da9_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqan_tcoffee/1.13.8--haf24da9_5
$ module help quay.io/biocontainers/seqan_tcoffee/1.13.8--haf24da9_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqan_tcoffee-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqan_tcoffee-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqan_tcoffee-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqan_tcoffee-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqan_tcoffee-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqan_tcoffee-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqan_tcoffee

```bash
$ singularity exec <container> /usr/local/bin/seqan_tcoffee
$ podman run --it --rm --entrypoint /usr/local/bin/seqan_tcoffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqan_tcoffee   -v ${PWD} -w ${PWD} <container> -c " $@"
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