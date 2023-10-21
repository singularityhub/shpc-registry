---
layout: container
name:  "quay.io/biocontainers/fqgrep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fqgrep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fqgrep/container.yaml"
updated_at: "2023-10-21 03:17:57.792633"
latest: "1.0.3--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/fqgrep"
aliases:
 - "fqgrep"
versions:
 - "1.0.2--h9f5acd7_0"
 - "1.0.2--h4ac6f70_2"
 - "1.0.3--h4ac6f70_0"
description: "singularity registry hpc automated addition for fqgrep"
config: {"url": "https://biocontainers.pro/tools/fqgrep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fqgrep", "latest": {"1.0.3--h4ac6f70_0": "sha256:b26aab4f7088c444f339e81122635f08ed5dbcdff86a6de82841e5bfd026a3f7"}, "tags": {"1.0.2--h9f5acd7_0": "sha256:42a060b8612a1115c65fbe88746e107e085419d9a9718c9c34d3776cddc41e0d", "1.0.2--h4ac6f70_2": "sha256:21847e08814941818b19fe792d508447a1554f72e9f3e5c1debdd5aaba43fc4e", "1.0.3--h4ac6f70_0": "sha256:b26aab4f7088c444f339e81122635f08ed5dbcdff86a6de82841e5bfd026a3f7"}, "docker": "quay.io/biocontainers/fqgrep", "aliases": {"fqgrep": "/usr/local/bin/fqgrep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fqgrep.
singularity registry hpc automated addition for fqgrep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fqgrep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fqgrep:1.0.3--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fqgrep/1.0.3--h4ac6f70_0
$ module help quay.io/biocontainers/fqgrep/1.0.3--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fqgrep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fqgrep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fqgrep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fqgrep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fqgrep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fqgrep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqgrep

```bash
$ singularity exec <container> /usr/local/bin/fqgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fqgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
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