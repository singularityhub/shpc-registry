---
layout: container
name:  "quay.io/biocontainers/pypgx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pypgx/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pypgx/container.yaml"
updated_at: "2022-10-27 00:27:39.927852"
latest: "0.9.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/pypgx"
aliases:
 - "fuc"
 - "pypgx"
versions:
 - "0.9.0--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for pypgx"
config: {"url": "https://biocontainers.pro/tools/pypgx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pypgx", "latest": {"0.9.0--pyh5e36f6f_0": "sha256:86f03a8935c7c972a8e1823eff4439c472b5cc86daff176929abf6a6f01957e2"}, "tags": {"0.9.0--pyh5e36f6f_0": "sha256:86f03a8935c7c972a8e1823eff4439c472b5cc86daff176929abf6a6f01957e2"}, "docker": "quay.io/biocontainers/pypgx", "aliases": {"fuc": "/usr/local/bin/fuc", "pypgx": "/usr/local/bin/pypgx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pypgx.
shpc-registry automated BioContainers addition for pypgx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pypgx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pypgx:0.9.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pypgx/0.9.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/pypgx/0.9.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pypgx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pypgx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pypgx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pypgx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pypgx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pypgx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fuc

```bash
$ singularity exec <container> /usr/local/bin/fuc
$ podman run --it --rm --entrypoint /usr/local/bin/fuc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypgx

```bash
$ singularity exec <container> /usr/local/bin/pypgx
$ podman run --it --rm --entrypoint /usr/local/bin/pypgx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypgx   -v ${PWD} -w ${PWD} <container> -c " $@"
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