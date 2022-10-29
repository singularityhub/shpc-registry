---
layout: container
name:  "quay.io/biocontainers/dgenies"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dgenies/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dgenies/container.yaml"
updated_at: "2022-10-29 05:43:00.525006"
latest: "1.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dgenies"
aliases:
 - "dgenies"
 - "2to3-3.10"
 - "brotli"
 - "cwebp"
 - "dwebp"
 - "f2py3.10"
 - "flask"
 - "fonttools"
 - "gif2rgb"
 - "gif2webp"
 - "gifbuild"
versions:
 - "1.4.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for dgenies"
config: {"url": "https://biocontainers.pro/tools/dgenies", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dgenies", "latest": {"1.4.0--pyhdfd78af_0": "sha256:92b1753c5363f783f3d0bff390d2d14094a8852f3bb08c8be76b1cbf0bb14989"}, "tags": {"1.4.0--pyhdfd78af_0": "sha256:92b1753c5363f783f3d0bff390d2d14094a8852f3bb08c8be76b1cbf0bb14989"}, "docker": "quay.io/biocontainers/dgenies", "aliases": {"dgenies": "/usr/local/bin/dgenies", "2to3-3.10": "/usr/local/bin/2to3-3.10", "brotli": "/usr/local/bin/brotli", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "f2py3.10": "/usr/local/bin/f2py3.10", "flask": "/usr/local/bin/flask", "fonttools": "/usr/local/bin/fonttools", "gif2rgb": "/usr/local/bin/gif2rgb", "gif2webp": "/usr/local/bin/gif2webp", "gifbuild": "/usr/local/bin/gifbuild"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dgenies.
shpc-registry automated BioContainers addition for dgenies
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dgenies
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dgenies:1.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dgenies/1.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/dgenies/1.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dgenies-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dgenies-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dgenies-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dgenies-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dgenies-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dgenies-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dgenies

```bash
$ singularity exec <container> /usr/local/bin/dgenies
$ podman run --it --rm --entrypoint /usr/local/bin/dgenies   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgenies   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2webp

```bash
$ singularity exec <container> /usr/local/bin/gif2webp
$ podman run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
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