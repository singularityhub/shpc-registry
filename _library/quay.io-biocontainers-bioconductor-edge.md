---
layout: container
name:  "quay.io/biocontainers/bioconductor-edge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-edge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-edge/container.yaml"
updated_at: "2026-02-02 05:06:41.290550"
latest: "2.38.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-edge"
aliases:
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "2.26.0--r41hc0cfd56_2"
 - "2.30.0--r42hc0cfd56_0"
 - "2.30.0--r42ha9d7317_1"
 - "2.32.0--r43ha9d7317_0"
 - "2.34.0--r43ha9d7317_0"
 - "2.34.0--r43ha9d7317_1"
 - "2.38.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-edge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-edge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-edge", "latest": {"2.38.0--r44h3df3fcb_0": "sha256:ff55de47b80f7d68f8f38db54261379d7de28842355953bb8e4bf7e12224da14"}, "tags": {"2.26.0--r41hc0cfd56_2": "sha256:425ba51e871b7a00e342eb63ddc5a9d141a5d26b95881a8338ba313aa9052f19", "2.30.0--r42hc0cfd56_0": "sha256:faca9376c88095e52709ffdf1b381315b3e7ceb06affe6b1a968bbad6225fa9d", "2.30.0--r42ha9d7317_1": "sha256:295a4912b7d9a4ccb2c55e7d5217e202ae19482744dd0c8a4de1dce7bc6e79f1", "2.32.0--r43ha9d7317_0": "sha256:fc7a46f7bcbf8722e778c6ef605365d6fcd88ed25d04a06067944144038a766f", "2.34.0--r43ha9d7317_0": "sha256:512ccf7be23ca25655814696dec274b9d1963757c6b15b74c0c323948c96f588", "2.34.0--r43ha9d7317_1": "sha256:f4b1c693ea9bd04506c0aa300d68c43bcff89d331d10c784531eaba766c7aa94", "2.38.0--r44h3df3fcb_0": "sha256:ff55de47b80f7d68f8f38db54261379d7de28842355953bb8e4bf7e12224da14"}, "docker": "quay.io/biocontainers/bioconductor-edge", "aliases": {"f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-edge.
shpc-registry automated BioContainers addition for bioconductor-edge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-edge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-edge:2.38.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-edge/2.38.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-edge/2.38.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-edge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-edge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-edge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-edge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-edge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-edge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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