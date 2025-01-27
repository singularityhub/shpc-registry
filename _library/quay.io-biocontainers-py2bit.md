---
layout: container
name:  "quay.io/biocontainers/py2bit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/py2bit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/py2bit/container.yaml"
updated_at: "2025-01-27 06:55:33.677080"
latest: "0.3.0--py310h1fe012e_11"
container_url: "https://biocontainers.pro/tools/py2bit"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.3.0--py38hbff2b2d_6"
 - "0.3.0--py310h1425a21_7"
 - "0.3.0--py39hf95cd2a_8"
 - "0.3.0--py310h1fe012e_11"
description: "shpc-registry automated BioContainers addition for py2bit"
config: {"url": "https://biocontainers.pro/tools/py2bit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for py2bit", "latest": {"0.3.0--py310h1fe012e_11": "sha256:aef80e34574e1fe568c1ef142ae8aca10b2dd9d34560ffe018817ce0036fad33"}, "tags": {"0.3.0--py38hbff2b2d_6": "sha256:1a862eb1ecd5913bd7b4834f327f18bb26ab9b0f6e20d8141a3c77ee01c58296", "0.3.0--py310h1425a21_7": "sha256:87deddb5652581e0790472d2ef1f5ea07883d764daa895127750084a281acbeb", "0.3.0--py39hf95cd2a_8": "sha256:e30553b4632bc4ab4270a6bffdb2a883cc4eaeffee7661c26875f60c3cabb7fa", "0.3.0--py310h1fe012e_11": "sha256:aef80e34574e1fe568c1ef142ae8aca10b2dd9d34560ffe018817ce0036fad33"}, "docker": "quay.io/biocontainers/py2bit", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/py2bit.
shpc-registry automated BioContainers addition for py2bit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/py2bit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/py2bit:0.3.0--py310h1fe012e_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/py2bit/0.3.0--py310h1fe012e_11
$ module help quay.io/biocontainers/py2bit/0.3.0--py310h1fe012e_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### py2bit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### py2bit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### py2bit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### py2bit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### py2bit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### py2bit-inspect-deffile:

```bash
$ singularity inspect -d <container>
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