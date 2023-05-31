---
layout: container
name:  "quay.io/biocontainers/ma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ma/container.yaml"
updated_at: "2023-05-31 03:08:08.392929"
latest: "2.0.1--py39h6935b12_0"
container_url: "https://biocontainers.pro/tools/ma"
aliases:
 - "lzma"
 - "lzmadec"
 - "lzmainfo"
 - "maCMD"
 - "unlzma"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "2.0.1--py39h6935b12_0"
description: "shpc-registry automated BioContainers addition for ma"
config: {"url": "https://biocontainers.pro/tools/ma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ma", "latest": {"2.0.1--py39h6935b12_0": "sha256:358d1489fd28aff879ba1a502d28b03db9c16aee7aa028b1bdcff68636b3213d"}, "tags": {"2.0.1--py39h6935b12_0": "sha256:358d1489fd28aff879ba1a502d28b03db9c16aee7aa028b1bdcff68636b3213d"}, "docker": "quay.io/biocontainers/ma", "aliases": {"lzma": "/usr/local/bin/lzma", "lzmadec": "/usr/local/bin/lzmadec", "lzmainfo": "/usr/local/bin/lzmainfo", "maCMD": "/usr/local/bin/maCMD", "unlzma": "/usr/local/bin/unlzma", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ma.
shpc-registry automated BioContainers addition for ma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ma:2.0.1--py39h6935b12_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ma/2.0.1--py39h6935b12_0
$ module help quay.io/biocontainers/ma/2.0.1--py39h6935b12_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lzma

```bash
$ singularity exec <container> /usr/local/bin/lzma
$ podman run --it --rm --entrypoint /usr/local/bin/lzma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lzma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lzmadec

```bash
$ singularity exec <container> /usr/local/bin/lzmadec
$ podman run --it --rm --entrypoint /usr/local/bin/lzmadec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lzmadec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lzmainfo

```bash
$ singularity exec <container> /usr/local/bin/lzmainfo
$ podman run --it --rm --entrypoint /usr/local/bin/lzmainfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lzmainfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maCMD

```bash
$ singularity exec <container> /usr/local/bin/maCMD
$ podman run --it --rm --entrypoint /usr/local/bin/maCMD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maCMD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unlzma

```bash
$ singularity exec <container> /usr/local/bin/unlzma
$ podman run --it --rm --entrypoint /usr/local/bin/unlzma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unlzma   -v ${PWD} -w ${PWD} <container> -c " $@"
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