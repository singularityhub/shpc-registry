---
layout: container
name:  "quay.io/biocontainers/pangenie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pangenie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pangenie/container.yaml"
updated_at: "2026-01-26 04:29:24.194448"
latest: "4.2.1--h077b44d_0"
container_url: "https://biocontainers.pro/tools/pangenie"
aliases:
 - "Analyze-UK"
 - "PanGenie"
 - "PanGenie-index"
 - "PanGenie-sampling"
 - "PanGenie-vcf"
 - "jellyfish"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "4.2.1--h077b44d_0"
description: "singularity registry hpc automated addition for pangenie"
config: {"url": "https://biocontainers.pro/tools/pangenie", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pangenie", "latest": {"4.2.1--h077b44d_0": "sha256:db24bebb23958d0ecfe765dc73bae5bfea58970552561285832c823efc02e66a"}, "tags": {"4.2.1--h077b44d_0": "sha256:db24bebb23958d0ecfe765dc73bae5bfea58970552561285832c823efc02e66a"}, "docker": "quay.io/biocontainers/pangenie", "aliases": {"Analyze-UK": "/usr/local/bin/Analyze-UK", "PanGenie": "/usr/local/bin/PanGenie", "PanGenie-index": "/usr/local/bin/PanGenie-index", "PanGenie-sampling": "/usr/local/bin/PanGenie-sampling", "PanGenie-vcf": "/usr/local/bin/PanGenie-vcf", "jellyfish": "/usr/local/bin/jellyfish", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pangenie.
singularity registry hpc automated addition for pangenie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pangenie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pangenie:4.2.1--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pangenie/4.2.1--h077b44d_0
$ module help quay.io/biocontainers/pangenie/4.2.1--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pangenie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pangenie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pangenie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pangenie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pangenie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pangenie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Analyze-UK

```bash
$ singularity exec <container> /usr/local/bin/Analyze-UK
$ podman run --it --rm --entrypoint /usr/local/bin/Analyze-UK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Analyze-UK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PanGenie

```bash
$ singularity exec <container> /usr/local/bin/PanGenie
$ podman run --it --rm --entrypoint /usr/local/bin/PanGenie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PanGenie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PanGenie-index

```bash
$ singularity exec <container> /usr/local/bin/PanGenie-index
$ podman run --it --rm --entrypoint /usr/local/bin/PanGenie-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PanGenie-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PanGenie-sampling

```bash
$ singularity exec <container> /usr/local/bin/PanGenie-sampling
$ podman run --it --rm --entrypoint /usr/local/bin/PanGenie-sampling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PanGenie-sampling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PanGenie-vcf

```bash
$ singularity exec <container> /usr/local/bin/PanGenie-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/PanGenie-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PanGenie-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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