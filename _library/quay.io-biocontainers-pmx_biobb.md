---
layout: container
name:  "quay.io/biocontainers/pmx_biobb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pmx_biobb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pmx_biobb/container.yaml"
updated_at: "2024-11-17 03:22:22.339420"
latest: "4.1.3--py37ha2f2a80_1"
container_url: "https://biocontainers.pro/tools/pmx_biobb"
aliases:
 - "pmx"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "futurize"
 - "pasteurize"
 - "f2py3.7"
 - "img2webp"
 - "cwebp"
versions:
 - "1.0.0--py37hc94c342_3"
 - "2.0.0--py37h1aed7a7_2"
 - "3.0.3--py310h8537716_4"
 - "4.1.3--py37ha2f2a80_1"
 - "4.0.2--py310h95c5ba8_0"
 - "4.0.2--py38h0928705_0"
description: "shpc-registry automated BioContainers addition for pmx_biobb"
config: {"url": "https://biocontainers.pro/tools/pmx_biobb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pmx_biobb", "latest": {"4.1.3--py37ha2f2a80_1": "sha256:278cf4b2c77a7084879ec355989b49fdadf7c0db231baee4a351d49cced82c64"}, "tags": {"1.0.0--py37hc94c342_3": "sha256:131e2e50a98da7e1dfe8d1f4c33e80d3cf1ef6d5c87486115800d4252a38e12d", "2.0.0--py37h1aed7a7_2": "sha256:b1cbde276643af57a90c86ddb13bc63546a3098d9b555d97d815265ba663e92f", "3.0.3--py310h8537716_4": "sha256:1393d4751b3962a9000fecdd30c09495c9c153096a3246911d5fe5c4db994217", "4.1.3--py37ha2f2a80_1": "sha256:278cf4b2c77a7084879ec355989b49fdadf7c0db231baee4a351d49cced82c64", "4.0.2--py310h95c5ba8_0": "sha256:ff09c3f07f56190e9b15cdc4bd778f8127835828920d198a646e73fe96a1a9c7", "4.0.2--py38h0928705_0": "sha256:44183bd3dc361c176dd4489dcd73fcc60df2b36fce8a60c2bed73a8ea30a9b85"}, "docker": "quay.io/biocontainers/pmx_biobb", "aliases": {"pmx": "/usr/local/bin/pmx", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.7": "/usr/local/bin/f2py3.7", "img2webp": "/usr/local/bin/img2webp", "cwebp": "/usr/local/bin/cwebp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pmx_biobb.
shpc-registry automated BioContainers addition for pmx_biobb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pmx_biobb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pmx_biobb:4.1.3--py37ha2f2a80_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pmx_biobb/4.1.3--py37ha2f2a80_1
$ module help quay.io/biocontainers/pmx_biobb/4.1.3--py37ha2f2a80_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pmx_biobb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pmx_biobb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pmx_biobb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pmx_biobb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pmx_biobb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pmx_biobb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pmx

```bash
$ singularity exec <container> /usr/local/bin/pmx
$ podman run --it --rm --entrypoint /usr/local/bin/pmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2webp

```bash
$ singularity exec <container> /usr/local/bin/img2webp
$ podman run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
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