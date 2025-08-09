---
layout: container
name:  "quay.io/biocontainers/grz-pydantic-models"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grz-pydantic-models/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grz-pydantic-models/container.yaml"
updated_at: "2025-08-09 03:44:15.757880"
latest: "2.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/grz-pydantic-models"
aliases:
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "1.2.1--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_0"
 - "1.3.0--pyhdfd78af_0"
 - "2.0.2--pyhdfd78af_0"
 - "1.5.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for grz-pydantic-models"
config: {"url": "https://biocontainers.pro/tools/grz-pydantic-models", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grz-pydantic-models", "latest": {"2.0.2--pyhdfd78af_0": "sha256:433c9631820b062abb44dd28b242f48a7fb769ebc174afe1ad285dbd1351efc5"}, "tags": {"1.2.1--pyhdfd78af_0": "sha256:abbfad8a96a77ca3acc6ddf73afb7f95d5629e8861168b9857d8da9cacd8c05d", "1.4.0--pyhdfd78af_0": "sha256:5323198c250fafa7dd26226804405c74e6fdbf85b9c713e502c04dd028edbc56", "1.3.0--pyhdfd78af_0": "sha256:09736cae59fe85cb5ed09d846edf856ae018ddc2b59da2a4226a05fa3989a220", "2.0.2--pyhdfd78af_0": "sha256:433c9631820b062abb44dd28b242f48a7fb769ebc174afe1ad285dbd1351efc5", "1.5.0--pyhdfd78af_0": "sha256:f7aa6e9cb5ad88b0b05c235ea86cf558f685e22f93ef221814433814fc1f354f"}, "docker": "quay.io/biocontainers/grz-pydantic-models", "aliases": {"idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grz-pydantic-models.
singularity registry hpc automated addition for grz-pydantic-models
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grz-pydantic-models
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grz-pydantic-models:2.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grz-pydantic-models/2.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/grz-pydantic-models/2.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grz-pydantic-models-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grz-pydantic-models-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grz-pydantic-models-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grz-pydantic-models-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grz-pydantic-models-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grz-pydantic-models-inspect-deffile:

```bash
$ singularity inspect -d <container>
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