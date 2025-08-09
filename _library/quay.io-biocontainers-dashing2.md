---
layout: container
name:  "quay.io/biocontainers/dashing2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dashing2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dashing2/container.yaml"
updated_at: "2025-08-09 03:58:13.077293"
latest: "2.1.20--he9e5f93_0"
container_url: "https://biocontainers.pro/tools/dashing2"
aliases:
 - "dashing2"
 - "dashing2-64"
 - "dashing2-tmp"
versions:
 - "2.1.20--he9e5f93_0"
description: "singularity registry hpc automated addition for dashing2"
config: {"url": "https://biocontainers.pro/tools/dashing2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dashing2", "latest": {"2.1.20--he9e5f93_0": "sha256:98a375decdd6f495743632932cb9dedd55afc1111a30cac45ac468c77cddef38"}, "tags": {"2.1.20--he9e5f93_0": "sha256:98a375decdd6f495743632932cb9dedd55afc1111a30cac45ac468c77cddef38"}, "docker": "quay.io/biocontainers/dashing2", "aliases": {"dashing2": "/usr/local/bin/dashing2", "dashing2-64": "/usr/local/bin/dashing2-64", "dashing2-tmp": "/usr/local/bin/dashing2-tmp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dashing2.
singularity registry hpc automated addition for dashing2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dashing2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dashing2:2.1.20--he9e5f93_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dashing2/2.1.20--he9e5f93_0
$ module help quay.io/biocontainers/dashing2/2.1.20--he9e5f93_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dashing2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dashing2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dashing2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dashing2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dashing2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dashing2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dashing2

```bash
$ singularity exec <container> /usr/local/bin/dashing2
$ podman run --it --rm --entrypoint /usr/local/bin/dashing2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dashing2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dashing2-64

```bash
$ singularity exec <container> /usr/local/bin/dashing2-64
$ podman run --it --rm --entrypoint /usr/local/bin/dashing2-64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dashing2-64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dashing2-tmp

```bash
$ singularity exec <container> /usr/local/bin/dashing2-tmp
$ podman run --it --rm --entrypoint /usr/local/bin/dashing2-tmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dashing2-tmp   -v ${PWD} -w ${PWD} <container> -c " $@"
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