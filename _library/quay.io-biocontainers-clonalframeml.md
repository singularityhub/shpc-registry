---
layout: container
name:  "quay.io/biocontainers/clonalframeml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clonalframeml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clonalframeml/container.yaml"
updated_at: "2024-01-27 02:35:24.956738"
latest: "1.12--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/clonalframeml"
aliases:
 - "ClonalFrameML"
versions:
 - "1.12--h9f5acd7_2"
 - "1.12--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for clonalframeml"
config: {"url": "https://biocontainers.pro/tools/clonalframeml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clonalframeml", "latest": {"1.12--h4ac6f70_4": "sha256:cad83cd06985e9a0437da72445da60a02853cc2b053c25b3463d5fb5e5c033d4"}, "tags": {"1.12--h9f5acd7_2": "sha256:e77baeb614d82f8364bd5f47a5a7604e9fad570818843f63095359dfd10216a2", "1.12--h4ac6f70_4": "sha256:cad83cd06985e9a0437da72445da60a02853cc2b053c25b3463d5fb5e5c033d4"}, "docker": "quay.io/biocontainers/clonalframeml", "aliases": {"ClonalFrameML": "/usr/local/bin/ClonalFrameML"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clonalframeml.
shpc-registry automated BioContainers addition for clonalframeml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clonalframeml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clonalframeml:1.12--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clonalframeml/1.12--h4ac6f70_4
$ module help quay.io/biocontainers/clonalframeml/1.12--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clonalframeml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clonalframeml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clonalframeml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clonalframeml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clonalframeml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clonalframeml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ClonalFrameML

```bash
$ singularity exec <container> /usr/local/bin/ClonalFrameML
$ podman run --it --rm --entrypoint /usr/local/bin/ClonalFrameML   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ClonalFrameML   -v ${PWD} -w ${PWD} <container> -c " $@"
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