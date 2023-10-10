---
layout: container
name:  "quay.io/biocontainers/sylph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sylph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sylph/container.yaml"
updated_at: "2023-10-10 02:59:40.854969"
latest: "0.1.0--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/sylph"
aliases:
 - "sylph"
versions:
 - "0.0.2--h4ac6f70_0"
 - "0.1.0--h4ac6f70_0"
 - "0.0.3--h4ac6f70_0"
description: "singularity registry hpc automated addition for sylph"
config: {"url": "https://biocontainers.pro/tools/sylph", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sylph", "latest": {"0.1.0--h4ac6f70_0": "sha256:ec01e69564473eeef93ebc9298537799d0cc085eef512f11fcc3279657e8f566"}, "tags": {"0.0.2--h4ac6f70_0": "sha256:e6fa763794572d58c513e5111e11c9950003ce74b35bb321a90b89c321acd37c", "0.1.0--h4ac6f70_0": "sha256:ec01e69564473eeef93ebc9298537799d0cc085eef512f11fcc3279657e8f566", "0.0.3--h4ac6f70_0": "sha256:56ca8c3397cba26b1b830de76fdadb70f46b05a3e27e7dcc64b8efb8e39955e9"}, "docker": "quay.io/biocontainers/sylph", "aliases": {"sylph": "/usr/local/bin/sylph"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sylph.
singularity registry hpc automated addition for sylph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sylph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sylph:0.1.0--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sylph/0.1.0--h4ac6f70_0
$ module help quay.io/biocontainers/sylph/0.1.0--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sylph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sylph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sylph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sylph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sylph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sylph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sylph

```bash
$ singularity exec <container> /usr/local/bin/sylph
$ podman run --it --rm --entrypoint /usr/local/bin/sylph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sylph   -v ${PWD} -w ${PWD} <container> -c " $@"
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