---
layout: container
name:  "quay.io/biocontainers/cytome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cytome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cytome/container.yaml"
updated_at: "2026-10-10 19:43:21.524628"
latest: "0.3.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cytome"
aliases:
 - "cytome"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
versions:
 - "0.3.6--pyhdfd78af_0"
description: "singularity registry hpc automated addition for cytome"
config: {"url": "https://biocontainers.pro/tools/cytome", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cytome", "latest": {"0.3.6--pyhdfd78af_0": "sha256:21218472e1ee2419a07d91c9fbf9c99de4afdd79249513a2a1b5fcf40e105d26"}, "tags": {"0.3.6--pyhdfd78af_0": "sha256:21218472e1ee2419a07d91c9fbf9c99de4afdd79249513a2a1b5fcf40e105d26"}, "docker": "quay.io/biocontainers/cytome", "aliases": {"cytome": "/usr/local/bin/cytome", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cytome.
singularity registry hpc automated addition for cytome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cytome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cytome:0.3.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cytome/0.3.6--pyhdfd78af_0
$ module help quay.io/biocontainers/cytome/0.3.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cytome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cytome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cytome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cytome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cytome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cytome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cytome

```bash
$ singularity exec <container> /usr/local/bin/cytome
$ podman run --it --rm --entrypoint /usr/local/bin/cytome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cytome   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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