---
layout: container
name:  "quay.io/biocontainers/gefast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gefast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gefast/container.yaml"
updated_at: "2025-12-01 05:19:53.290508"
latest: "2.0.1--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/gefast"
aliases:
 - "GeFaST"
versions:
 - "2.0.1--h9f5acd7_1"
 - "2.0.1--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for gefast"
config: {"url": "https://biocontainers.pro/tools/gefast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gefast", "latest": {"2.0.1--h4ac6f70_3": "sha256:148956a13ff704c63f68f785c7da3dd335ed07a97764fffcfc04614d6203159d"}, "tags": {"2.0.1--h9f5acd7_1": "sha256:cb17e28f40249c0092129cbfea891eebfc450b4a9f6392c654fab19cd154bce1", "2.0.1--h4ac6f70_3": "sha256:148956a13ff704c63f68f785c7da3dd335ed07a97764fffcfc04614d6203159d"}, "docker": "quay.io/biocontainers/gefast", "aliases": {"GeFaST": "/usr/local/bin/GeFaST"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gefast.
shpc-registry automated BioContainers addition for gefast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gefast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gefast:2.0.1--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gefast/2.0.1--h4ac6f70_3
$ module help quay.io/biocontainers/gefast/2.0.1--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gefast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gefast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gefast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gefast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gefast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gefast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeFaST

```bash
$ singularity exec <container> /usr/local/bin/GeFaST
$ podman run --it --rm --entrypoint /usr/local/bin/GeFaST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeFaST   -v ${PWD} -w ${PWD} <container> -c " $@"
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