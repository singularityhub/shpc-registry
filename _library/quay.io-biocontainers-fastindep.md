---
layout: container
name:  "quay.io/biocontainers/fastindep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastindep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastindep/container.yaml"
updated_at: "2023-10-23 03:09:54.104049"
latest: "1.0.0--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/fastindep"
aliases:
 - "fastindep"
 - "fastindep-symmetry"
versions:
 - "1.0.0--h9f5acd7_4"
 - "1.0.0--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for fastindep"
config: {"url": "https://biocontainers.pro/tools/fastindep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastindep", "latest": {"1.0.0--h4ac6f70_6": "sha256:79e9906c94cb203aef70c8b43ced7e66662927a0c2574e5923f4a2d3de04401b"}, "tags": {"1.0.0--h9f5acd7_4": "sha256:47d8e593f24782300e6cb95d799a35d48b5acea278d8be04cc743fea84580a7c", "1.0.0--h4ac6f70_6": "sha256:79e9906c94cb203aef70c8b43ced7e66662927a0c2574e5923f4a2d3de04401b"}, "docker": "quay.io/biocontainers/fastindep", "aliases": {"fastindep": "/usr/local/bin/fastindep", "fastindep-symmetry": "/usr/local/bin/fastindep-symmetry"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastindep.
shpc-registry automated BioContainers addition for fastindep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastindep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastindep:1.0.0--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastindep/1.0.0--h4ac6f70_6
$ module help quay.io/biocontainers/fastindep/1.0.0--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastindep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastindep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastindep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastindep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastindep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastindep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastindep

```bash
$ singularity exec <container> /usr/local/bin/fastindep
$ podman run --it --rm --entrypoint /usr/local/bin/fastindep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastindep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastindep-symmetry

```bash
$ singularity exec <container> /usr/local/bin/fastindep-symmetry
$ podman run --it --rm --entrypoint /usr/local/bin/fastindep-symmetry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastindep-symmetry   -v ${PWD} -w ${PWD} <container> -c " $@"
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