---
layout: container
name:  "quay.io/biocontainers/stream_atac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stream_atac/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stream_atac/container.yaml"
updated_at: "2022-10-29 05:53:46.313490"
latest: "0.3.5--py_5"
container_url: "https://biocontainers.pro/tools/stream_atac"
aliases:
 - "stream_atac"
 - "2to3-3.7"
 - "c89"
 - "c99"
 - "curve_keygen"
 - "f2py3.7"
 - "funzip"
 - "gif2h5"
 - "gio-launch-desktop"
 - "h52gif"
 - "h5c++"
versions:
 - "0.3.5--py_5"
description: "shpc-registry automated BioContainers addition for stream_atac"
config: {"url": "https://biocontainers.pro/tools/stream_atac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stream_atac", "latest": {"0.3.5--py_5": "sha256:5f33f127d097a5d4a3f3bd3492e8dc4b4a53c8757a183e22bbf6f90d9cf9b7c5"}, "tags": {"0.3.5--py_5": "sha256:5f33f127d097a5d4a3f3bd3492e8dc4b4a53c8757a183e22bbf6f90d9cf9b7c5"}, "docker": "quay.io/biocontainers/stream_atac", "aliases": {"stream_atac": "/usr/local/bin/stream_atac", "2to3-3.7": "/usr/local/bin/2to3-3.7", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99", "curve_keygen": "/usr/local/bin/curve_keygen", "f2py3.7": "/usr/local/bin/f2py3.7", "funzip": "/usr/local/bin/funzip", "gif2h5": "/usr/local/bin/gif2h5", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stream_atac.
shpc-registry automated BioContainers addition for stream_atac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stream_atac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stream_atac:0.3.5--py_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stream_atac/0.3.5--py_5
$ module help quay.io/biocontainers/stream_atac/0.3.5--py_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stream_atac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stream_atac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stream_atac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stream_atac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stream_atac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stream_atac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stream_atac

```bash
$ singularity exec <container> /usr/local/bin/stream_atac
$ podman run --it --rm --entrypoint /usr/local/bin/stream_atac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stream_atac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
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