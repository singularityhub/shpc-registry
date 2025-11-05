---
layout: container
name:  "quay.io/biocontainers/madre"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/madre/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/madre/container.yaml"
updated_at: "2025-11-05 03:29:43.867633"
latest: "0.0.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/madre"
aliases:
 - "calculate-abundances"
 - "database-reduction"
 - "madre"
 - "read-classification"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "0.0.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for madre"
config: {"url": "https://biocontainers.pro/tools/madre", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for madre", "latest": {"0.0.4--pyhdfd78af_0": "sha256:5cf7ea6c568efcebc2d193f8370c92dfbade18b0829098acc578edd90a54b228"}, "tags": {"0.0.4--pyhdfd78af_0": "sha256:5cf7ea6c568efcebc2d193f8370c92dfbade18b0829098acc578edd90a54b228"}, "docker": "quay.io/biocontainers/madre", "aliases": {"calculate-abundances": "/usr/local/bin/calculate-abundances", "database-reduction": "/usr/local/bin/database-reduction", "madre": "/usr/local/bin/madre", "read-classification": "/usr/local/bin/read-classification", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/madre.
singularity registry hpc automated addition for madre
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/madre
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/madre:0.0.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/madre/0.0.4--pyhdfd78af_0
$ module help quay.io/biocontainers/madre/0.0.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### madre-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### madre-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### madre-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### madre-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### madre-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### madre-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### calculate-abundances

```bash
$ singularity exec <container> /usr/local/bin/calculate-abundances
$ podman run --it --rm --entrypoint /usr/local/bin/calculate-abundances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculate-abundances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### database-reduction

```bash
$ singularity exec <container> /usr/local/bin/database-reduction
$ podman run --it --rm --entrypoint /usr/local/bin/database-reduction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/database-reduction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### madre

```bash
$ singularity exec <container> /usr/local/bin/madre
$ podman run --it --rm --entrypoint /usr/local/bin/madre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/madre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read-classification

```bash
$ singularity exec <container> /usr/local/bin/read-classification
$ podman run --it --rm --entrypoint /usr/local/bin/read-classification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read-classification   -v ${PWD} -w ${PWD} <container> -c " $@"
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