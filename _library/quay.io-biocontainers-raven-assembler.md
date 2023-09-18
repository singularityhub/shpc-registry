---
layout: container
name:  "quay.io/biocontainers/raven-assembler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/raven-assembler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/raven-assembler/container.yaml"
updated_at: "2023-09-18 02:33:05.807042"
latest: "1.8.1--h43eeafb_3"
container_url: "https://biocontainers.pro/tools/raven-assembler"
aliases:
 - "raven"
versions:
 - "1.8.1--h5b5514e_1"
 - "1.8.1--h43eeafb_3"
description: "shpc-registry automated BioContainers addition for raven-assembler"
config: {"url": "https://biocontainers.pro/tools/raven-assembler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for raven-assembler", "latest": {"1.8.1--h43eeafb_3": "sha256:f4fb9dce3e189cdc0e74e5c3fa0d043e532c507e20e96f44a394a89c94438312"}, "tags": {"1.8.1--h5b5514e_1": "sha256:1a439066b3b6d95a587984d3225653a785294258ed5fc38c6ab5391a7beba8fe", "1.8.1--h43eeafb_3": "sha256:f4fb9dce3e189cdc0e74e5c3fa0d043e532c507e20e96f44a394a89c94438312"}, "docker": "quay.io/biocontainers/raven-assembler", "aliases": {"raven": "/usr/local/bin/raven"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/raven-assembler.
shpc-registry automated BioContainers addition for raven-assembler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/raven-assembler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/raven-assembler:1.8.1--h43eeafb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/raven-assembler/1.8.1--h43eeafb_3
$ module help quay.io/biocontainers/raven-assembler/1.8.1--h43eeafb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### raven-assembler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### raven-assembler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### raven-assembler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### raven-assembler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### raven-assembler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### raven-assembler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### raven

```bash
$ singularity exec <container> /usr/local/bin/raven
$ podman run --it --rm --entrypoint /usr/local/bin/raven   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raven   -v ${PWD} -w ${PWD} <container> -c " $@"
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