---
layout: container
name:  "quay.io/biocontainers/bioconductor-spatialomicsoverlay"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spatialomicsoverlay/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spatialomicsoverlay/container.yaml"
updated_at: "2024-10-01 03:11:32.383795"
latest: "1.2.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spatialomicsoverlay"
aliases:
 - "jwebserver"
 - "geosop"
 - "x86_64-conda-linux-gnu-pkg-config"
 - "geos-config"
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
 - "jpackage"
 - "hb-info"
 - "f2py3.11"
 - "dvipdf"
versions:
 - "1.0.0--r43hdfd78af_0"
 - "1.2.1--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-spatialomicsoverlay"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spatialomicsoverlay", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-spatialomicsoverlay", "latest": {"1.2.1--r43hdfd78af_0": "sha256:cce406de0754a86b6fbf7129951b78915eb1fc885c5f1e488113e9bb65febd95"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:8de92ac035a8cf3f4d0d61cec8bf8b0284fb4e7002f29b88a03c6c446d79e6a0", "1.2.1--r43hdfd78af_0": "sha256:cce406de0754a86b6fbf7129951b78915eb1fc885c5f1e488113e9bb65febd95"}, "docker": "quay.io/biocontainers/bioconductor-spatialomicsoverlay", "aliases": {"jwebserver": "/usr/local/bin/jwebserver", "geosop": "/usr/local/bin/geosop", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "geos-config": "/usr/local/bin/geos-config", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config", "animate": "/usr/local/bin/animate", "composite": "/usr/local/bin/composite", "conjure": "/usr/local/bin/conjure", "convert": "/usr/local/bin/convert", "display": "/usr/local/bin/display", "identify": "/usr/local/bin/identify", "import": "/usr/local/bin/import", "magick": "/usr/local/bin/magick", "magick-script": "/usr/local/bin/magick-script", "mogrify": "/usr/local/bin/mogrify", "montage": "/usr/local/bin/montage", "pkg-config": "/usr/local/bin/pkg-config", "pkg-config.bin": "/usr/local/bin/pkg-config.bin", "stream": "/usr/local/bin/stream", "compare": "/usr/local/bin/compare", "jpackage": "/usr/local/bin/jpackage", "hb-info": "/usr/local/bin/hb-info", "f2py3.11": "/usr/local/bin/f2py3.11", "dvipdf": "/usr/local/bin/dvipdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spatialomicsoverlay.
singularity registry hpc automated addition for bioconductor-spatialomicsoverlay
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialomicsoverlay
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialomicsoverlay:1.2.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spatialomicsoverlay/1.2.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spatialomicsoverlay/1.2.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spatialomicsoverlay-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialomicsoverlay-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialomicsoverlay-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spatialomicsoverlay-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spatialomicsoverlay-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spatialomicsoverlay-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dvipdf

```bash
$ singularity exec <container> /usr/local/bin/dvipdf
$ podman run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
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