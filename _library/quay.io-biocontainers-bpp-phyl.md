---
layout: container
name:  "quay.io/biocontainers/bpp-phyl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bpp-phyl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bpp-phyl/container.yaml"
updated_at: "2023-10-28 03:11:29.642174"
latest: "2.4.1--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/bpp-phyl"

versions:
 - "2.4.1--h9f5acd7_3"
 - "2.4.1--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for bpp-phyl"
config: {"url": "https://biocontainers.pro/tools/bpp-phyl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bpp-phyl", "latest": {"2.4.1--h4ac6f70_4": "sha256:2466e48f22f7f2a0a971350d4e1da4bdfaf826555c0a0c53e91cdbd965328bb3"}, "tags": {"2.4.1--h9f5acd7_3": "sha256:e28a23d9256af333b44c8b5a972b0b6360a915b5b241b48f28f32b6fa4e3ff62", "2.4.1--h4ac6f70_4": "sha256:2466e48f22f7f2a0a971350d4e1da4bdfaf826555c0a0c53e91cdbd965328bb3"}, "docker": "quay.io/biocontainers/bpp-phyl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bpp-phyl.
shpc-registry automated BioContainers addition for bpp-phyl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bpp-phyl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bpp-phyl:2.4.1--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bpp-phyl/2.4.1--h4ac6f70_4
$ module help quay.io/biocontainers/bpp-phyl/2.4.1--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bpp-phyl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bpp-phyl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bpp-phyl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bpp-phyl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bpp-phyl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bpp-phyl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bpp-phyl

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