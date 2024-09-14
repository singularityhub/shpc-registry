---
layout: container
name:  "quay.io/biocontainers/svist4get"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svist4get/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svist4get/container.yaml"
updated_at: "2024-09-14 02:56:29.793974"
latest: "1.3.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/svist4get"
aliases:
 - "svist4get"
 - "svist4get_copier"
 - "x86_64-conda-linux-gnu-pkg-config"
 - "Magick++-config"
 - "MagickCore-config"
 - "MagickWand-config"
 - "animate"
 - "composite"
 - "conjure"
 - "convert"
 - "display"
 - "identify"
versions:
 - "1.3.1--pyhdfd78af_0"
 - "1.3.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for svist4get"
config: {"url": "https://biocontainers.pro/tools/svist4get", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svist4get", "latest": {"1.3.1.1--pyhdfd78af_0": "sha256:97c8fb95d753883db9f0555015cad00e196affb9561a401fc68d5426c34c1bf5"}, "tags": {"1.3.1--pyhdfd78af_0": "sha256:e65fe58212741e88b990a9785e532832e301a207bd6841c7d41364d6a4368473", "1.3.1.1--pyhdfd78af_0": "sha256:97c8fb95d753883db9f0555015cad00e196affb9561a401fc68d5426c34c1bf5"}, "docker": "quay.io/biocontainers/svist4get", "aliases": {"svist4get": "/usr/local/bin/svist4get", "svist4get_copier": "/usr/local/bin/svist4get_copier", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config", "animate": "/usr/local/bin/animate", "composite": "/usr/local/bin/composite", "conjure": "/usr/local/bin/conjure", "convert": "/usr/local/bin/convert", "display": "/usr/local/bin/display", "identify": "/usr/local/bin/identify"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svist4get.
shpc-registry automated BioContainers addition for svist4get
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svist4get
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svist4get:1.3.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svist4get/1.3.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/svist4get/1.3.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svist4get-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svist4get-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svist4get-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svist4get-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svist4get-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svist4get-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### svist4get

```bash
$ singularity exec <container> /usr/local/bin/svist4get
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svist4get_copier

```bash
$ singularity exec <container> /usr/local/bin/svist4get_copier
$ podman run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svist4get_copier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Magick++-config

```bash
$ singularity exec <container> /usr/local/bin/Magick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickCore-config

```bash
$ singularity exec <container> /usr/local/bin/MagickCore-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickWand-config

```bash
$ singularity exec <container> /usr/local/bin/MagickWand-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### animate

```bash
$ singularity exec <container> /usr/local/bin/animate
$ podman run --it --rm --entrypoint /usr/local/bin/animate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/animate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### composite

```bash
$ singularity exec <container> /usr/local/bin/composite
$ podman run --it --rm --entrypoint /usr/local/bin/composite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/composite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conjure

```bash
$ singularity exec <container> /usr/local/bin/conjure
$ podman run --it --rm --entrypoint /usr/local/bin/conjure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conjure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert

```bash
$ singularity exec <container> /usr/local/bin/convert
$ podman run --it --rm --entrypoint /usr/local/bin/convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### display

```bash
$ singularity exec <container> /usr/local/bin/display
$ podman run --it --rm --entrypoint /usr/local/bin/display   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/display   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### identify

```bash
$ singularity exec <container> /usr/local/bin/identify
$ podman run --it --rm --entrypoint /usr/local/bin/identify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/identify   -v ${PWD} -w ${PWD} <container> -c " $@"
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