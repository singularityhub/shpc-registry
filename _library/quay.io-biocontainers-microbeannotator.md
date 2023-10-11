---
layout: container
name:  "quay.io/biocontainers/microbeannotator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/microbeannotator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/microbeannotator/container.yaml"
updated_at: "2023-10-11 03:04:48.470818"
latest: "2.0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/microbeannotator"
aliases:
 - "microbeannotator"
 - "microbeannotator_db_builder"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "2.0.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for microbeannotator"
config: {"url": "https://biocontainers.pro/tools/microbeannotator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for microbeannotator", "latest": {"2.0.5--pyhdfd78af_0": "sha256:7fce637b170fc3f0a329c9bcb12fc4f985af130267944f0006428e5bb76257ba"}, "tags": {"2.0.5--pyhdfd78af_0": "sha256:7fce637b170fc3f0a329c9bcb12fc4f985af130267944f0006428e5bb76257ba"}, "docker": "quay.io/biocontainers/microbeannotator", "aliases": {"microbeannotator": "/usr/local/bin/microbeannotator", "microbeannotator_db_builder": "/usr/local/bin/microbeannotator_db_builder", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/microbeannotator.
singularity registry hpc automated addition for microbeannotator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/microbeannotator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/microbeannotator:2.0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/microbeannotator/2.0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/microbeannotator/2.0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### microbeannotator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### microbeannotator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### microbeannotator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### microbeannotator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### microbeannotator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### microbeannotator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### microbeannotator

```bash
$ singularity exec <container> /usr/local/bin/microbeannotator
$ podman run --it --rm --entrypoint /usr/local/bin/microbeannotator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/microbeannotator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### microbeannotator_db_builder

```bash
$ singularity exec <container> /usr/local/bin/microbeannotator_db_builder
$ podman run --it --rm --entrypoint /usr/local/bin/microbeannotator_db_builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/microbeannotator_db_builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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