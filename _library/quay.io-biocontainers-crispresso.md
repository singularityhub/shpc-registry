---
layout: container
name:  "quay.io/biocontainers/crispresso"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crispresso/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crispresso/container.yaml"
updated_at: "2025-05-03 03:23:55.654903"
latest: "1.0.13--py27h9801fc8_5"
container_url: "https://biocontainers.pro/tools/crispresso"

versions:
 - "1.0.8--py27_0"
 - "1.0.13--py27h9801fc8_5"
description: "shpc-registry automated BioContainers addition for crispresso"
config: {"url": "https://biocontainers.pro/tools/crispresso", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crispresso", "latest": {"1.0.13--py27h9801fc8_5": "sha256:f24bf87ca5557adb745aa8b5515877de2be5cda69c26224f00c9e3994ecbc8b3"}, "tags": {"1.0.8--py27_0": "sha256:dc5f9bd14869816609980bda9b609004dd4d9083ec7f58d7256db16550d0b777", "1.0.13--py27h9801fc8_5": "sha256:f24bf87ca5557adb745aa8b5515877de2be5cda69c26224f00c9e3994ecbc8b3"}, "docker": "quay.io/biocontainers/crispresso"}
---

This module is a singularity container wrapper for quay.io/biocontainers/crispresso.
shpc-registry automated BioContainers addition for crispresso
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crispresso
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crispresso:1.0.13--py27h9801fc8_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crispresso/1.0.13--py27h9801fc8_5
$ module help quay.io/biocontainers/crispresso/1.0.13--py27h9801fc8_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crispresso-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crispresso-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crispresso-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crispresso-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crispresso-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crispresso-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### crispresso

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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