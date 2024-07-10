---
layout: container
name:  "quay.io/biocontainers/hca-matrix-downloader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hca-matrix-downloader/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hca-matrix-downloader/container.yaml"
updated_at: "2024-07-10 02:56:18.433102"
latest: "0.0.4--py_0"
container_url: "https://biocontainers.pro/tools/hca-matrix-downloader"
aliases:
 - "hca-matrix-downloader"
 - "hca-mtx-to-10x"
 - "chardetect"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.0.4--py_0"
description: "shpc-registry automated BioContainers addition for hca-matrix-downloader"
config: {"url": "https://biocontainers.pro/tools/hca-matrix-downloader", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hca-matrix-downloader", "latest": {"0.0.4--py_0": "sha256:d2dee94b3e230ada2369aca50d18492407ca30e67bdc468689aa78bbd63bd024"}, "tags": {"0.0.4--py_0": "sha256:d2dee94b3e230ada2369aca50d18492407ca30e67bdc468689aa78bbd63bd024"}, "docker": "quay.io/biocontainers/hca-matrix-downloader", "aliases": {"hca-matrix-downloader": "/usr/local/bin/hca-matrix-downloader", "hca-mtx-to-10x": "/usr/local/bin/hca-mtx-to-10x", "chardetect": "/usr/local/bin/chardetect", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hca-matrix-downloader.
shpc-registry automated BioContainers addition for hca-matrix-downloader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hca-matrix-downloader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hca-matrix-downloader:0.0.4--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hca-matrix-downloader/0.0.4--py_0
$ module help quay.io/biocontainers/hca-matrix-downloader/0.0.4--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hca-matrix-downloader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hca-matrix-downloader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hca-matrix-downloader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hca-matrix-downloader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hca-matrix-downloader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hca-matrix-downloader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hca-matrix-downloader

```bash
$ singularity exec <container> /usr/local/bin/hca-matrix-downloader
$ podman run --it --rm --entrypoint /usr/local/bin/hca-matrix-downloader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hca-matrix-downloader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hca-mtx-to-10x

```bash
$ singularity exec <container> /usr/local/bin/hca-mtx-to-10x
$ podman run --it --rm --entrypoint /usr/local/bin/hca-mtx-to-10x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hca-mtx-to-10x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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