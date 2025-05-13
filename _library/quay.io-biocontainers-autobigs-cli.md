---
layout: container
name:  "quay.io/biocontainers/autobigs-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/autobigs-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/autobigs-cli/container.yaml"
updated_at: "2025-05-13 03:48:46.357855"
latest: "0.6.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/autobigs-cli"
aliases:
 - "autoBIGS"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "0.4.2--pyhdfd78af_0"
 - "0.6.5--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for autobigs-cli"
config: {"url": "https://biocontainers.pro/tools/autobigs-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for autobigs-cli", "latest": {"0.6.5--pyhdfd78af_0": "sha256:3002fc6f6275ecd1bce4485a073b29e5d6522794e3d919b39c6db84c7bb47f0a"}, "tags": {"0.4.2--pyhdfd78af_0": "sha256:44dd53a7148474ab206ae299d50683dd63d3211bf91332d5e8efa142dd753f5a", "0.6.5--pyhdfd78af_0": "sha256:3002fc6f6275ecd1bce4485a073b29e5d6522794e3d919b39c6db84c7bb47f0a", "0.5.0--pyhdfd78af_0": "sha256:e0263fd9e2e60f249c3a3f1a060d5d857d306227cf3fca7a7dff7ac3e5f9096e"}, "docker": "quay.io/biocontainers/autobigs-cli", "aliases": {"autoBIGS": "/usr/local/bin/autoBIGS", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/autobigs-cli.
singularity registry hpc automated addition for autobigs-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/autobigs-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/autobigs-cli:0.6.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/autobigs-cli/0.6.5--pyhdfd78af_0
$ module help quay.io/biocontainers/autobigs-cli/0.6.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autobigs-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autobigs-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autobigs-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autobigs-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autobigs-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autobigs-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autoBIGS

```bash
$ singularity exec <container> /usr/local/bin/autoBIGS
$ podman run --it --rm --entrypoint /usr/local/bin/autoBIGS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoBIGS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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