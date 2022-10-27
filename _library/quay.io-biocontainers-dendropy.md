---
layout: container
name:  "quay.io/biocontainers/dendropy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dendropy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dendropy/container.yaml"
updated_at: "2022-10-27 00:56:15.385202"
latest: "4.5.2--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/dendropy"

versions:
 - "4.5.2--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for dendropy"
config: {"url": "https://biocontainers.pro/tools/dendropy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dendropy", "latest": {"4.5.2--pyh3252c3a_0": "sha256:1c6595b3af0f838931fda400b692afe39373703c2dac6522c8ecc0d431aea6b0"}, "tags": {"4.5.2--pyh3252c3a_0": "sha256:1c6595b3af0f838931fda400b692afe39373703c2dac6522c8ecc0d431aea6b0"}, "docker": "quay.io/biocontainers/dendropy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/dendropy.
shpc-registry automated BioContainers addition for dendropy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dendropy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dendropy:4.5.2--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dendropy/4.5.2--pyh3252c3a_0
$ module help quay.io/biocontainers/dendropy/4.5.2--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dendropy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dendropy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dendropy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dendropy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dendropy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dendropy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### dendropy

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