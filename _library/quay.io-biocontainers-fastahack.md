---
layout: container
name:  "quay.io/biocontainers/fastahack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastahack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastahack/container.yaml"
updated_at: "2024-03-09 02:27:36.686524"
latest: "2016.07.2--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/fastahack"
aliases:
 - "fastahack"
versions:
 - "2016.07.2--h9f5acd7_4"
 - "2016.07.2--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for fastahack"
config: {"url": "https://biocontainers.pro/tools/fastahack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastahack", "latest": {"2016.07.2--h4ac6f70_6": "sha256:825da41b36f482334955341165fc79b513cffc47c9e07b5f5cccc981f2766dc3"}, "tags": {"2016.07.2--h9f5acd7_4": "sha256:5fad12f37ddef35fe586482c52c534ae4f15c56a5f930e360303c49cb6d15794", "2016.07.2--h4ac6f70_6": "sha256:825da41b36f482334955341165fc79b513cffc47c9e07b5f5cccc981f2766dc3"}, "docker": "quay.io/biocontainers/fastahack", "aliases": {"fastahack": "/usr/local/bin/fastahack"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastahack.
shpc-registry automated BioContainers addition for fastahack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastahack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastahack:2016.07.2--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastahack/2016.07.2--h4ac6f70_6
$ module help quay.io/biocontainers/fastahack/2016.07.2--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastahack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastahack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastahack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastahack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastahack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastahack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastahack

```bash
$ singularity exec <container> /usr/local/bin/fastahack
$ podman run --it --rm --entrypoint /usr/local/bin/fastahack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastahack   -v ${PWD} -w ${PWD} <container> -c " $@"
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