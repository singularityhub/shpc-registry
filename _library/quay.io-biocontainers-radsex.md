---
layout: container
name:  "quay.io/biocontainers/radsex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/radsex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/radsex/container.yaml"
updated_at: "2023-09-15 03:15:38.108561"
latest: "1.2.0--h43eeafb_3"
container_url: "https://biocontainers.pro/tools/radsex"
aliases:
 - "radsex"
versions:
 - "1.2.0--h5b5514e_1"
 - "1.2.0--h43eeafb_3"
description: "shpc-registry automated BioContainers addition for radsex"
config: {"url": "https://biocontainers.pro/tools/radsex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for radsex", "latest": {"1.2.0--h43eeafb_3": "sha256:a112e23532db836103c8027f242e3c0d7624db5d08cc83ba09fbcb55fead3d96"}, "tags": {"1.2.0--h5b5514e_1": "sha256:ff19a1406972f5d4ea34c7f949eea7ee7a8165d5fe8546db4f6cee9676b9c063", "1.2.0--h43eeafb_3": "sha256:a112e23532db836103c8027f242e3c0d7624db5d08cc83ba09fbcb55fead3d96"}, "docker": "quay.io/biocontainers/radsex", "aliases": {"radsex": "/usr/local/bin/radsex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/radsex.
shpc-registry automated BioContainers addition for radsex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/radsex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/radsex:1.2.0--h43eeafb_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/radsex/1.2.0--h43eeafb_3
$ module help quay.io/biocontainers/radsex/1.2.0--h43eeafb_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### radsex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### radsex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### radsex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### radsex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### radsex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### radsex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### radsex

```bash
$ singularity exec <container> /usr/local/bin/radsex
$ podman run --it --rm --entrypoint /usr/local/bin/radsex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/radsex   -v ${PWD} -w ${PWD} <container> -c " $@"
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