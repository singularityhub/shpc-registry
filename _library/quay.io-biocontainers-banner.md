---
layout: container
name:  "quay.io/biocontainers/banner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/banner/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/banner/container.yaml"
updated_at: "2022-10-27 00:27:43.721601"
latest: "0.0.2--py_0"
container_url: "https://biocontainers.pro/tools/banner"
aliases:
 - "banner"
versions:
 - "0.0.2--py_0"
description: "shpc-registry automated BioContainers addition for banner"
config: {"url": "https://biocontainers.pro/tools/banner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for banner", "latest": {"0.0.2--py_0": "sha256:a86222352f6573a5cdc8925b24f28c762238b465e0359acf27d7200ff4880d94"}, "tags": {"0.0.2--py_0": "sha256:a86222352f6573a5cdc8925b24f28c762238b465e0359acf27d7200ff4880d94"}, "docker": "quay.io/biocontainers/banner", "aliases": {"banner": "/usr/local/bin/banner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/banner.
shpc-registry automated BioContainers addition for banner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/banner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/banner:0.0.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/banner/0.0.2--py_0
$ module help quay.io/biocontainers/banner/0.0.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### banner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### banner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### banner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### banner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### banner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### banner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### banner

```bash
$ singularity exec <container> /usr/local/bin/banner
$ podman run --it --rm --entrypoint /usr/local/bin/banner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/banner   -v ${PWD} -w ${PWD} <container> -c " $@"
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