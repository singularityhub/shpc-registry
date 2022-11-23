---
layout: container
name:  "quay.io/biocontainers/burrito"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/burrito/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/burrito/container.yaml"
updated_at: "2022-11-23 00:28:51.634694"
latest: "0.9.1--pyh864c0ab_3"
container_url: "https://biocontainers.pro/tools/burrito"

versions:
 - "0.9.1--pyh864c0ab_3"
description: "shpc-registry automated BioContainers addition for burrito"
config: {"url": "https://biocontainers.pro/tools/burrito", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for burrito", "latest": {"0.9.1--pyh864c0ab_3": "sha256:58bbe8b962dbada1860217b63e055d6dbc9390a35846804674d66440781e77dd"}, "tags": {"0.9.1--pyh864c0ab_3": "sha256:58bbe8b962dbada1860217b63e055d6dbc9390a35846804674d66440781e77dd"}, "docker": "quay.io/biocontainers/burrito"}
---

This module is a singularity container wrapper for quay.io/biocontainers/burrito.
shpc-registry automated BioContainers addition for burrito
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/burrito
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/burrito:0.9.1--pyh864c0ab_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/burrito/0.9.1--pyh864c0ab_3
$ module help quay.io/biocontainers/burrito/0.9.1--pyh864c0ab_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### burrito-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### burrito-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### burrito-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### burrito-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### burrito-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### burrito-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### burrito

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