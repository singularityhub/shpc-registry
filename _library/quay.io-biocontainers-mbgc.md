---
layout: container
name:  "quay.io/biocontainers/mbgc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mbgc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mbgc/container.yaml"
updated_at: "2024-11-15 03:03:01.365360"
latest: "2.0.1--h4ac6f70_1"
container_url: "https://biocontainers.pro/tools/mbgc"
aliases:
 - "mbgc"
versions:
 - "1.2.1--h9f5acd7_1"
 - "1.2.1--h4ac6f70_3"
 - "2.0--h4ac6f70_0"
 - "2.0.1--h4ac6f70_0"
 - "2.0.1--h4ac6f70_1"
description: "shpc-registry automated BioContainers addition for mbgc"
config: {"url": "https://biocontainers.pro/tools/mbgc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mbgc", "latest": {"2.0.1--h4ac6f70_1": "sha256:38bf8ed0ede5d968a1dcd04e5e40f0b2cbcd0c25a933a3dcdfaf39c98f41ee84"}, "tags": {"1.2.1--h9f5acd7_1": "sha256:98e821540be1bd54912c3e3475921d619ae651b482d4a06058ec9002dd9044f6", "1.2.1--h4ac6f70_3": "sha256:e9acba885079d6ad1353f6a6577c2c61cb39609fb94e48b179c7074b3118b5bb", "2.0--h4ac6f70_0": "sha256:367110953356f713322f8244277abd015301e824d9175a7f6ebe93c779b8ee8b", "2.0.1--h4ac6f70_0": "sha256:88342798e7a43a016b28ca6f4a6965b4e073ba0ea46fd0daa45f72e5c62536a4", "2.0.1--h4ac6f70_1": "sha256:38bf8ed0ede5d968a1dcd04e5e40f0b2cbcd0c25a933a3dcdfaf39c98f41ee84"}, "docker": "quay.io/biocontainers/mbgc", "aliases": {"mbgc": "/usr/local/bin/mbgc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mbgc.
shpc-registry automated BioContainers addition for mbgc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mbgc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mbgc:2.0.1--h4ac6f70_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mbgc/2.0.1--h4ac6f70_1
$ module help quay.io/biocontainers/mbgc/2.0.1--h4ac6f70_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mbgc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mbgc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mbgc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mbgc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mbgc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mbgc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mbgc

```bash
$ singularity exec <container> /usr/local/bin/mbgc
$ podman run --it --rm --entrypoint /usr/local/bin/mbgc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mbgc   -v ${PWD} -w ${PWD} <container> -c " $@"
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