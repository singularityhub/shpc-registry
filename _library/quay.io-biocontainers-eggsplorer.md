---
layout: container
name:  "quay.io/biocontainers/eggsplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eggsplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eggsplorer/container.yaml"
updated_at: "2026-11-06 09:11:54.333123"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/eggsplorer"
aliases:
 - "eggsplorer"
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "plotly_get_chrome"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for eggsplorer"
config: {"url": "https://biocontainers.pro/tools/eggsplorer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for eggsplorer", "latest": {"1.1.0--pyhdfd78af_0": "sha256:09691d29f57d22debcb27a3e2d097e4f8f38619b4810ace0fa291fc7423a4475"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:09691d29f57d22debcb27a3e2d097e4f8f38619b4810ace0fa291fc7423a4475"}, "docker": "quay.io/biocontainers/eggsplorer", "aliases": {"eggsplorer": "/usr/local/bin/eggsplorer", "idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eggsplorer.
singularity registry hpc automated addition for eggsplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eggsplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eggsplorer:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eggsplorer/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/eggsplorer/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eggsplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eggsplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eggsplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eggsplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eggsplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eggsplorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eggsplorer

```bash
$ singularity exec <container> /usr/local/bin/eggsplorer
$ podman run --it --rm --entrypoint /usr/local/bin/eggsplorer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eggsplorer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.15

```bash
$ singularity exec <container> /usr/local/bin/idle3.15
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.15

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.15
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15

```bash
$ singularity exec <container> /usr/local/bin/python3.15
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15-config

```bash
$ singularity exec <container> /usr/local/bin/python3.15-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
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