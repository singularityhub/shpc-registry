---
layout: container
name:  "quay.io/biocontainers/bioconductor-tidyspatialexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tidyspatialexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tidyspatialexperiment/container.yaml"
updated_at: "2025-09-06 03:33:51.587771"
latest: "1.2.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tidyspatialexperiment"
aliases:
 - "dec265"
 - "x265"
 - "rav1e"
 - "SvtAv1EncApp"
 - "dav1d"
 - "aomdec"
 - "aomenc"
 - "pandoc-lua"
 - "x86_64-conda-linux-gnu.cfg"
 - "pandoc-server"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "x86_64-conda-linux-gnu-pkg-config"
 - "Magick++-config"
 - "MagickCore-config"
 - "MagickWand-config"
 - "animate"
 - "composite"
 - "conjure"
 - "display"
 - "identify"
 - "import"
 - "magick"
 - "magick-script"
versions:
 - "1.2.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-tidyspatialexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tidyspatialexperiment", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-tidyspatialexperiment", "latest": {"1.2.0--r44hdfd78af_0": "sha256:26452e9d68b85393148f9e0a7c0aaf0dfe4834cba144ebd5ae2746a58ce59e91"}, "tags": {"1.2.0--r44hdfd78af_0": "sha256:26452e9d68b85393148f9e0a7c0aaf0dfe4834cba144ebd5ae2746a58ce59e91"}, "docker": "quay.io/biocontainers/bioconductor-tidyspatialexperiment", "aliases": {"dec265": "/usr/local/bin/dec265", "x265": "/usr/local/bin/x265", "rav1e": "/usr/local/bin/rav1e", "SvtAv1EncApp": "/usr/local/bin/SvtAv1EncApp", "dav1d": "/usr/local/bin/dav1d", "aomdec": "/usr/local/bin/aomdec", "aomenc": "/usr/local/bin/aomenc", "pandoc-lua": "/usr/local/bin/pandoc-lua", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "pandoc-server": "/usr/local/bin/pandoc-server", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config", "animate": "/usr/local/bin/animate", "composite": "/usr/local/bin/composite", "conjure": "/usr/local/bin/conjure", "display": "/usr/local/bin/display", "identify": "/usr/local/bin/identify", "import": "/usr/local/bin/import", "magick": "/usr/local/bin/magick", "magick-script": "/usr/local/bin/magick-script"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tidyspatialexperiment.
singularity registry hpc automated addition for bioconductor-tidyspatialexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tidyspatialexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tidyspatialexperiment:1.2.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tidyspatialexperiment/1.2.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tidyspatialexperiment/1.2.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tidyspatialexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidyspatialexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidyspatialexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tidyspatialexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tidyspatialexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tidyspatialexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dec265

```bash
$ singularity exec <container> /usr/local/bin/dec265
$ podman run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dec265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x265

```bash
$ singularity exec <container> /usr/local/bin/x265
$ podman run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rav1e

```bash
$ singularity exec <container> /usr/local/bin/rav1e
$ podman run --it --rm --entrypoint /usr/local/bin/rav1e   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rav1e   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SvtAv1EncApp

```bash
$ singularity exec <container> /usr/local/bin/SvtAv1EncApp
$ podman run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dav1d

```bash
$ singularity exec <container> /usr/local/bin/dav1d
$ podman run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomdec

```bash
$ singularity exec <container> /usr/local/bin/aomdec
$ podman run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomenc

```bash
$ singularity exec <container> /usr/local/bin/aomenc
$ podman run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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