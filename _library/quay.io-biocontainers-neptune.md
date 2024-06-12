---
layout: container
name:  "quay.io/biocontainers/neptune"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/neptune/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/neptune/container.yaml"
updated_at: "2024-06-12 03:00:32.126541"
latest: "1.2.5--py_3"
container_url: "https://biocontainers.pro/tools/neptune"
aliases:
 - "neptune"
 - "neptune-conda"
 - "build.sh"
 - "common.go"
 - "rchive.go"
 - "setup-deps.log"
 - "setup.sh"
 - "xtract.go"
 - "metadata_conda_debug.yaml"
 - "bt-context.txt"
 - "bt-link"
 - "bt-load"
versions:
 - "1.2.5--py_3"
description: "shpc-registry automated BioContainers addition for neptune"
config: {"url": "https://biocontainers.pro/tools/neptune", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for neptune", "latest": {"1.2.5--py_3": "sha256:55720f01c26422bc1218b46f4d99e3ac46f3d5569545da3ed32b0ff900f7c0c2"}, "tags": {"1.2.5--py_3": "sha256:55720f01c26422bc1218b46f4d99e3ac46f3d5569545da3ed32b0ff900f7c0c2"}, "docker": "quay.io/biocontainers/neptune", "aliases": {"neptune": "/usr/local/bin/neptune", "neptune-conda": "/usr/local/bin/neptune-conda", "build.sh": "/usr/local/bin/build.sh", "common.go": "/usr/local/bin/common.go", "rchive.go": "/usr/local/bin/rchive.go", "setup-deps.log": "/usr/local/bin/setup-deps.log", "setup.sh": "/usr/local/bin/setup.sh", "xtract.go": "/usr/local/bin/xtract.go", "metadata_conda_debug.yaml": "/usr/local/bin/metadata_conda_debug.yaml", "bt-context.txt": "/usr/local/bin/bt-context.txt", "bt-link": "/usr/local/bin/bt-link", "bt-load": "/usr/local/bin/bt-load"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/neptune.
shpc-registry automated BioContainers addition for neptune
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/neptune
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/neptune:1.2.5--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/neptune/1.2.5--py_3
$ module help quay.io/biocontainers/neptune/1.2.5--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### neptune-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### neptune-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### neptune-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### neptune-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### neptune-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### neptune-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### neptune

```bash
$ singularity exec <container> /usr/local/bin/neptune
$ podman run --it --rm --entrypoint /usr/local/bin/neptune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/neptune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### neptune-conda

```bash
$ singularity exec <container> /usr/local/bin/neptune-conda
$ podman run --it --rm --entrypoint /usr/local/bin/neptune-conda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/neptune-conda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build.sh

```bash
$ singularity exec <container> /usr/local/bin/build.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### common.go

```bash
$ singularity exec <container> /usr/local/bin/common.go
$ podman run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rchive.go

```bash
$ singularity exec <container> /usr/local/bin/rchive.go
$ podman run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup-deps.log

```bash
$ singularity exec <container> /usr/local/bin/setup-deps.log
$ podman run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.sh

```bash
$ singularity exec <container> /usr/local/bin/setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtract.go

```bash
$ singularity exec <container> /usr/local/bin/xtract.go
$ podman run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metadata_conda_debug.yaml

```bash
$ singularity exec <container> /usr/local/bin/metadata_conda_debug.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metadata_conda_debug.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-context.txt

```bash
$ singularity exec <container> /usr/local/bin/bt-context.txt
$ podman run --it --rm --entrypoint /usr/local/bin/bt-context.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-context.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-link

```bash
$ singularity exec <container> /usr/local/bin/bt-link
$ podman run --it --rm --entrypoint /usr/local/bin/bt-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bt-load

```bash
$ singularity exec <container> /usr/local/bin/bt-load
$ podman run --it --rm --entrypoint /usr/local/bin/bt-load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bt-load   -v ${PWD} -w ${PWD} <container> -c " $@"
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