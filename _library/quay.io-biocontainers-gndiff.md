---
layout: container
name:  "quay.io/biocontainers/gndiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gndiff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gndiff/container.yaml"
updated_at: "2024-12-23 03:18:18.937284"
latest: "0.3.0--he881be0_0"
container_url: "https://biocontainers.pro/tools/gndiff"
aliases:
 - "gndiff"
versions:
 - "0.2.0--he881be0_0"
 - "0.3.0--he881be0_0"
 - "0.2.1--he881be0_0"
description: "singularity registry hpc automated addition for gndiff"
config: {"url": "https://biocontainers.pro/tools/gndiff", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gndiff", "latest": {"0.3.0--he881be0_0": "sha256:75aedb69713921dac68c75af6d59710779ce90c6c0f355a7f90064a9e7eabeb0"}, "tags": {"0.2.0--he881be0_0": "sha256:ccb9a26b2c6309efe0b397a4a180184828a184b0aaf700e22068464f20093a31", "0.3.0--he881be0_0": "sha256:75aedb69713921dac68c75af6d59710779ce90c6c0f355a7f90064a9e7eabeb0", "0.2.1--he881be0_0": "sha256:81b16ab43e940f2b8c8dec239d6acdaf5fcd36d32093ef542c6672dc7890b88a"}, "docker": "quay.io/biocontainers/gndiff", "aliases": {"gndiff": "/usr/local/bin/gndiff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gndiff.
singularity registry hpc automated addition for gndiff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gndiff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gndiff:0.3.0--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gndiff/0.3.0--he881be0_0
$ module help quay.io/biocontainers/gndiff/0.3.0--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gndiff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gndiff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gndiff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gndiff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gndiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gndiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gndiff

```bash
$ singularity exec <container> /usr/local/bin/gndiff
$ podman run --it --rm --entrypoint /usr/local/bin/gndiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gndiff   -v ${PWD} -w ${PWD} <container> -c " $@"
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