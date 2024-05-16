---
layout: container
name:  "quay.io/biocontainers/samcut"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samcut/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samcut/container.yaml"
updated_at: "2024-05-16 02:34:57.903167"
latest: "0.1.1--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/samcut"
aliases:
 - "samcut"
versions:
 - "0.1.1--h9f5acd7_0"
 - "0.1.1--h4ac6f70_2"
description: "singularity registry hpc automated addition for samcut"
config: {"url": "https://biocontainers.pro/tools/samcut", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for samcut", "latest": {"0.1.1--h4ac6f70_2": "sha256:0200727e4f6e61131f6b47c9c529c7c8d31642fefab7fefe348437d57601fe9f"}, "tags": {"0.1.1--h9f5acd7_0": "sha256:73b9841040f07589bd6389ac9b4828a9ce419cec1c21f8fc9580c60606fa37be", "0.1.1--h4ac6f70_2": "sha256:0200727e4f6e61131f6b47c9c529c7c8d31642fefab7fefe348437d57601fe9f"}, "docker": "quay.io/biocontainers/samcut", "aliases": {"samcut": "/usr/local/bin/samcut"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samcut.
singularity registry hpc automated addition for samcut
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samcut
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samcut:0.1.1--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samcut/0.1.1--h4ac6f70_2
$ module help quay.io/biocontainers/samcut/0.1.1--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samcut-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samcut-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samcut-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samcut-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samcut-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samcut-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samcut

```bash
$ singularity exec <container> /usr/local/bin/samcut
$ podman run --it --rm --entrypoint /usr/local/bin/samcut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samcut   -v ${PWD} -w ${PWD} <container> -c " $@"
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