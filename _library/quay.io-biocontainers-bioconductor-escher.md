---
layout: container
name:  "quay.io/biocontainers/bioconductor-escher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-escher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-escher/container.yaml"
updated_at: "2025-03-10 03:18:24.799126"
latest: "1.6.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-escher"
aliases:
 - "git2"
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
 - "import"
 - "magick"
 - "magick-script"
 - "mogrify"
 - "montage"
 - "pkg-config"
 - "pkg-config.bin"
 - "stream"
 - "compare"
 - "hb-info"
 - "dvipdf"
 - "eps2eps"
 - "gs"
 - "gsbj"
 - "gsdj"
versions:
 - "1.0.0--r43hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.6.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-escher"
config: {"url": "https://biocontainers.pro/tools/bioconductor-escher", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-escher", "latest": {"1.6.0--r44hdfd78af_0": "sha256:152d68937054a64c33d7b067e43f277724787d8f306201e5830c8d261d621341"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:88da2d693c5beb8c363e5ef58bd791d818f1359f80cb6da6809049c16f41e0d0", "1.2.0--r43hdfd78af_0": "sha256:2721007ed34480d27cf9aa8cdf9e2de8ed7b449d2ed843553930ef06f86e12f5", "1.6.0--r44hdfd78af_0": "sha256:152d68937054a64c33d7b067e43f277724787d8f306201e5830c8d261d621341"}, "docker": "quay.io/biocontainers/bioconductor-escher", "aliases": {"git2": "/usr/local/bin/git2", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config", "animate": "/usr/local/bin/animate", "composite": "/usr/local/bin/composite", "conjure": "/usr/local/bin/conjure", "convert": "/usr/local/bin/convert", "display": "/usr/local/bin/display", "identify": "/usr/local/bin/identify", "import": "/usr/local/bin/import", "magick": "/usr/local/bin/magick", "magick-script": "/usr/local/bin/magick-script", "mogrify": "/usr/local/bin/mogrify", "montage": "/usr/local/bin/montage", "pkg-config": "/usr/local/bin/pkg-config", "pkg-config.bin": "/usr/local/bin/pkg-config.bin", "stream": "/usr/local/bin/stream", "compare": "/usr/local/bin/compare", "hb-info": "/usr/local/bin/hb-info", "dvipdf": "/usr/local/bin/dvipdf", "eps2eps": "/usr/local/bin/eps2eps", "gs": "/usr/local/bin/gs", "gsbj": "/usr/local/bin/gsbj", "gsdj": "/usr/local/bin/gsdj"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-escher.
singularity registry hpc automated addition for bioconductor-escher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-escher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-escher:1.6.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-escher/1.6.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-escher/1.6.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-escher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-escher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-escher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-escher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-escher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-escher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### git2

```bash
$ singularity exec <container> /usr/local/bin/git2
$ podman run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### import

```bash
$ singularity exec <container> /usr/local/bin/import
$ podman run --it --rm --entrypoint /usr/local/bin/import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magick

```bash
$ singularity exec <container> /usr/local/bin/magick
$ podman run --it --rm --entrypoint /usr/local/bin/magick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magick   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magick-script

```bash
$ singularity exec <container> /usr/local/bin/magick-script
$ podman run --it --rm --entrypoint /usr/local/bin/magick-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magick-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mogrify

```bash
$ singularity exec <container> /usr/local/bin/mogrify
$ podman run --it --rm --entrypoint /usr/local/bin/mogrify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mogrify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### montage

```bash
$ singularity exec <container> /usr/local/bin/montage
$ podman run --it --rm --entrypoint /usr/local/bin/montage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/montage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config

```bash
$ singularity exec <container> /usr/local/bin/pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config.bin

```bash
$ singularity exec <container> /usr/local/bin/pkg-config.bin
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stream

```bash
$ singularity exec <container> /usr/local/bin/stream
$ podman run --it --rm --entrypoint /usr/local/bin/stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare

```bash
$ singularity exec <container> /usr/local/bin/compare
$ podman run --it --rm --entrypoint /usr/local/bin/compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dvipdf

```bash
$ singularity exec <container> /usr/local/bin/dvipdf
$ podman run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eps2eps

```bash
$ singularity exec <container> /usr/local/bin/eps2eps
$ podman run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gs

```bash
$ singularity exec <container> /usr/local/bin/gs
$ podman run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsbj

```bash
$ singularity exec <container> /usr/local/bin/gsbj
$ podman run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsdj

```bash
$ singularity exec <container> /usr/local/bin/gsdj
$ podman run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
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