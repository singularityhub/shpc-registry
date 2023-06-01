---
layout: container
name:  "quay.io/biocontainers/samblaster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samblaster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samblaster/container.yaml"
updated_at: "2023-06-01 03:41:42.561782"
latest: "0.1.26--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/samblaster"
aliases:
 - "samblaster"
versions:
 - "0.1.26--h9f5acd7_2"
 - "0.1.26--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for samblaster"
config: {"url": "https://biocontainers.pro/tools/samblaster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samblaster", "latest": {"0.1.26--h4ac6f70_4": "sha256:dc65616f9d96c1c42c706d818f7c6fd3880e8aeae0d824be8966c37ce992db3c"}, "tags": {"0.1.26--h9f5acd7_2": "sha256:60c9465e285cc975c65de5629e38979a1284e7fb9a9095d24a7ba33e365c2075", "0.1.26--h4ac6f70_4": "sha256:dc65616f9d96c1c42c706d818f7c6fd3880e8aeae0d824be8966c37ce992db3c"}, "docker": "quay.io/biocontainers/samblaster", "aliases": {"samblaster": "/usr/local/bin/samblaster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samblaster.
shpc-registry automated BioContainers addition for samblaster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samblaster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samblaster:0.1.26--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samblaster/0.1.26--h4ac6f70_4
$ module help quay.io/biocontainers/samblaster/0.1.26--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samblaster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samblaster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samblaster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samblaster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samblaster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samblaster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samblaster

```bash
$ singularity exec <container> /usr/local/bin/samblaster
$ podman run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
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