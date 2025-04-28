---
layout: container
name:  "quay.io/biocontainers/cd-hit-auxtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cd-hit-auxtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cd-hit-auxtools/container.yaml"
updated_at: "2025-04-28 03:27:40.441490"
latest: "4.8.1--h9948957_4"
container_url: "https://biocontainers.pro/tools/cd-hit-auxtools"
aliases:
 - "cd-hit-dup"
 - "cd-hit-lap"
 - "read-linker"
versions:
 - "4.8.1--h9f5acd7_2"
 - "4.8.1--h4ac6f70_3"
 - "4.8.1--h9948957_4"
description: "shpc-registry automated BioContainers addition for cd-hit-auxtools"
config: {"url": "https://biocontainers.pro/tools/cd-hit-auxtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cd-hit-auxtools", "latest": {"4.8.1--h9948957_4": "sha256:0c03649147acf5f5aeb812433410fcf5675734d93208786dc6836782ddfe097f"}, "tags": {"4.8.1--h9f5acd7_2": "sha256:a7cbdf49e5f9f4f6533e8b8e1b23260f79c3e5fca3acd6e0c1ae8a0db9da32b0", "4.8.1--h4ac6f70_3": "sha256:34caae56cdd57c0fb8c20cb586e4092d0c1cbad6777b67d039a294be647a5a87", "4.8.1--h9948957_4": "sha256:0c03649147acf5f5aeb812433410fcf5675734d93208786dc6836782ddfe097f"}, "docker": "quay.io/biocontainers/cd-hit-auxtools", "aliases": {"cd-hit-dup": "/usr/local/bin/cd-hit-dup", "cd-hit-lap": "/usr/local/bin/cd-hit-lap", "read-linker": "/usr/local/bin/read-linker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cd-hit-auxtools.
shpc-registry automated BioContainers addition for cd-hit-auxtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cd-hit-auxtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cd-hit-auxtools:4.8.1--h9948957_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cd-hit-auxtools/4.8.1--h9948957_4
$ module help quay.io/biocontainers/cd-hit-auxtools/4.8.1--h9948957_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cd-hit-auxtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cd-hit-auxtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cd-hit-auxtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cd-hit-auxtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cd-hit-auxtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cd-hit-auxtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cd-hit-dup

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-dup
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-dup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-dup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-lap

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-lap
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-lap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-lap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read-linker

```bash
$ singularity exec <container> /usr/local/bin/read-linker
$ podman run --it --rm --entrypoint /usr/local/bin/read-linker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read-linker   -v ${PWD} -w ${PWD} <container> -c " $@"
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