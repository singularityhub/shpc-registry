---
layout: container
name:  "quay.io/biocontainers/hic-straw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hic-straw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hic-straw/container.yaml"
updated_at: "2025-04-14 03:41:22.887951"
latest: "1.3.1--py311hb99c5bc_6"
container_url: "https://biocontainers.pro/tools/hic-straw"
aliases:
 - "pybind11-config"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.3.1--py39hc1feb53_0"
 - "1.3.1--py38h5e0e482_3"
 - "1.3.1--py310h54163ca_3"
 - "1.3.1--py311h2e16732_4"
 - "1.3.1--py310h227bcd1_5"
 - "1.3.1--py311hb99c5bc_6"
description: "singularity registry hpc automated addition for hic-straw"
config: {"url": "https://biocontainers.pro/tools/hic-straw", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hic-straw", "latest": {"1.3.1--py311hb99c5bc_6": "sha256:933d103286fddba9be8ee235f67d74aa95031395b786d0f48cf54d6a99c64ccd"}, "tags": {"1.3.1--py39hc1feb53_0": "sha256:5ae5c5519433b49a3380233146c62f4031cbbcba07101fd8d38d409abc0136d4", "1.3.1--py38h5e0e482_3": "sha256:dfd1140240fe4fd58d94f81d6568ce883b22604ef31d8dd9aaecf236820fd788", "1.3.1--py310h54163ca_3": "sha256:fd163c815b2706854ebb3ec10fed75f8281a2104851307ad2f79ab67f253a70e", "1.3.1--py311h2e16732_4": "sha256:4b3b5b285e1158d72c3cffd2076e3c097e3ade755863a86c08e37a9a50d4d0b3", "1.3.1--py310h227bcd1_5": "sha256:bc5ec26d3924bd3941f22a5af656ccc0ee9d6e6abaf8dc3b046057f916d94299", "1.3.1--py311hb99c5bc_6": "sha256:933d103286fddba9be8ee235f67d74aa95031395b786d0f48cf54d6a99c64ccd"}, "docker": "quay.io/biocontainers/hic-straw", "aliases": {"pybind11-config": "/usr/local/bin/pybind11-config", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hic-straw.
singularity registry hpc automated addition for hic-straw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hic-straw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hic-straw:1.3.1--py311hb99c5bc_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hic-straw/1.3.1--py311hb99c5bc_6
$ module help quay.io/biocontainers/hic-straw/1.3.1--py311hb99c5bc_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hic-straw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hic-straw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hic-straw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hic-straw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hic-straw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hic-straw-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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