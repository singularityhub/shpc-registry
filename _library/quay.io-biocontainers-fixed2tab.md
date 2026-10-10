---
layout: container
name:  "quay.io/biocontainers/fixed2tab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fixed2tab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fixed2tab/container.yaml"
updated_at: "2026-10-10 19:20:47.161413"
latest: "0.1.0"
container_url: "https://biocontainers.pro/tools/fixed2tab"
aliases:
 - "fixed2tab"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "0.1.0"
description: "singularity registry hpc automated addition for fixed2tab"
config: {"url": "https://biocontainers.pro/tools/fixed2tab", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fixed2tab", "latest": {"0.1.0": "sha256:749d2edf892347c761d84a0c45910a2c5bc2b73df184d8251417942474d651ef"}, "tags": {"0.1.0": "sha256:749d2edf892347c761d84a0c45910a2c5bc2b73df184d8251417942474d651ef"}, "docker": "quay.io/biocontainers/fixed2tab", "aliases": {"fixed2tab": "/usr/local/bin/fixed2tab", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fixed2tab.
singularity registry hpc automated addition for fixed2tab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fixed2tab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fixed2tab:0.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fixed2tab/0.1.0
$ module help quay.io/biocontainers/fixed2tab/0.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fixed2tab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fixed2tab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fixed2tab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fixed2tab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fixed2tab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fixed2tab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fixed2tab

```bash
$ singularity exec <container> /usr/local/bin/fixed2tab
$ podman run --it --rm --entrypoint /usr/local/bin/fixed2tab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fixed2tab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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