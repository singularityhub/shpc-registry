---
layout: container
name:  "quay.io/biocontainers/parasail-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parasail-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/parasail-python/container.yaml"
updated_at: "2025-11-23 04:08:08.002631"
latest: "1.3.4--py310h5140242_5"
container_url: "https://biocontainers.pro/tools/parasail-python"
aliases:
 - "f2py3.8"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "1.2.4--py38h3b68952_2"
 - "1.3.4--py38h5cf8b27_0"
 - "1.2.4--py310hc8f18ef_2"
 - "1.3.4--py310h6cc9453_1"
 - "1.3.4--py38h40d3509_2"
 - "1.3.4--py39h746d604_3"
 - "1.3.4--py312hdcc493e_4"
 - "1.3.4--py310h5140242_5"
description: "shpc-registry automated BioContainers addition for parasail-python"
config: {"url": "https://biocontainers.pro/tools/parasail-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parasail-python", "latest": {"1.3.4--py310h5140242_5": "sha256:7aee924e91b3c4f477fbacf2a7173b848110b03f3f43d67b66f9398be8b8b87f"}, "tags": {"1.2.4--py38h3b68952_2": "sha256:78d3565f88b8f4c480b9387548012eb06b6cc43c8c65ae993e0d8ceaaadd25c9", "1.3.4--py38h5cf8b27_0": "sha256:4551a9a8297d0b7237d5caa607ee94e26a86fec877ff27817e50aaa291b51ad0", "1.2.4--py310hc8f18ef_2": "sha256:8d2b4a6d5bffcffa63ea0a61dbef42883bcaf30fabe33ef6c2fcff46368b66fd", "1.3.4--py310h6cc9453_1": "sha256:56782758e25a35b24d299b9752fbaf01f85be168eb6fe805fa2387a54e1073cc", "1.3.4--py38h40d3509_2": "sha256:93fed0ff73854d5f32099a0f118defc0b4b1ebdae069e1f178de487db9e26ffa", "1.3.4--py39h746d604_3": "sha256:6bf4ca399b9710aa17df65656d8080f73b3b3d63e238770b78c4f7e06d8567c3", "1.3.4--py312hdcc493e_4": "sha256:b4a50a204ad4280bff805862e1f2f7ed9c61286bc32055750f8638dba76bb1d5", "1.3.4--py310h5140242_5": "sha256:7aee924e91b3c4f477fbacf2a7173b848110b03f3f43d67b66f9398be8b8b87f"}, "docker": "quay.io/biocontainers/parasail-python", "aliases": {"f2py3.8": "/usr/local/bin/f2py3.8", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parasail-python.
shpc-registry automated BioContainers addition for parasail-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parasail-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parasail-python:1.3.4--py310h5140242_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parasail-python/1.3.4--py310h5140242_5
$ module help quay.io/biocontainers/parasail-python/1.3.4--py310h5140242_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parasail-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parasail-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parasail-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parasail-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parasail-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parasail-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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