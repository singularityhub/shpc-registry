---
layout: container
name:  "quay.io/biocontainers/liftoff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/liftoff/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/liftoff/container.yaml"
updated_at: "2022-10-29 05:58:25.916623"
latest: "1.6.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/liftoff"
aliases:
 - "liftoff"
 - "2to3-3.9"
 - "activate-global-python-argcomplete"
 - "brotli"
 - "cwebp"
 - "dwebp"
 - "f2py3.9"
 - "faidx"
 - "fonttools"
 - "gffutils-cli"
 - "gif2rgb"
versions:
 - "1.6.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for liftoff"
config: {"url": "https://biocontainers.pro/tools/liftoff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for liftoff", "latest": {"1.6.3--pyhdfd78af_0": "sha256:63d9a69375519259f155e2f0b0a61b4c95287684f324c7193e2cead7e4ef5894"}, "tags": {"1.6.3--pyhdfd78af_0": "sha256:63d9a69375519259f155e2f0b0a61b4c95287684f324c7193e2cead7e4ef5894"}, "docker": "quay.io/biocontainers/liftoff", "aliases": {"liftoff": "/usr/local/bin/liftoff", "2to3-3.9": "/usr/local/bin/2to3-3.9", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "brotli": "/usr/local/bin/brotli", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "f2py3.9": "/usr/local/bin/f2py3.9", "faidx": "/usr/local/bin/faidx", "fonttools": "/usr/local/bin/fonttools", "gffutils-cli": "/usr/local/bin/gffutils-cli", "gif2rgb": "/usr/local/bin/gif2rgb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/liftoff.
shpc-registry automated BioContainers addition for liftoff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/liftoff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/liftoff:1.6.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/liftoff/1.6.3--pyhdfd78af_0
$ module help quay.io/biocontainers/liftoff/1.6.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### liftoff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### liftoff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### liftoff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### liftoff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### liftoff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### liftoff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### liftoff

```bash
$ singularity exec <container> /usr/local/bin/liftoff
$ podman run --it --rm --entrypoint /usr/local/bin/liftoff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/liftoff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
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