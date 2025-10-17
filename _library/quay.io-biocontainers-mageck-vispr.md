---
layout: container
name:  "quay.io/biocontainers/mageck-vispr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mageck-vispr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mageck-vispr/container.yaml"
updated_at: "2025-10-17 03:18:43.677761"
latest: "0.5.6--py_0"
container_url: "https://biocontainers.pro/tools/mageck-vispr"
aliases:
 - "RRA"
 - "mageck"
 - "mageck-vispr"
 - "mageckGSEA"
 - "vispr"
 - "cutadapt"
 - "fastqc"
 - "x86_64-conda-linux-gnu-pkg-config"
 - "flask"
 - "pulptest"
 - "igzip"
 - "Magick++-config"
 - "MagickCore-config"
 - "MagickWand-config"
 - "animate"
versions:
 - "0.5.6--py_0"
description: "shpc-registry automated BioContainers addition for mageck-vispr"
config: {"url": "https://biocontainers.pro/tools/mageck-vispr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mageck-vispr", "latest": {"0.5.6--py_0": "sha256:a934573b0aa1b48a5efaec6f764960a365443c614fa7f22cad94e0744b45a77b"}, "tags": {"0.5.6--py_0": "sha256:a934573b0aa1b48a5efaec6f764960a365443c614fa7f22cad94e0744b45a77b"}, "docker": "quay.io/biocontainers/mageck-vispr", "aliases": {"RRA": "/usr/local/bin/RRA", "mageck": "/usr/local/bin/mageck", "mageck-vispr": "/usr/local/bin/mageck-vispr", "mageckGSEA": "/usr/local/bin/mageckGSEA", "vispr": "/usr/local/bin/vispr", "cutadapt": "/usr/local/bin/cutadapt", "fastqc": "/usr/local/bin/fastqc", "x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "flask": "/usr/local/bin/flask", "pulptest": "/usr/local/bin/pulptest", "igzip": "/usr/local/bin/igzip", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config", "animate": "/usr/local/bin/animate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mageck-vispr.
shpc-registry automated BioContainers addition for mageck-vispr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mageck-vispr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mageck-vispr:0.5.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mageck-vispr/0.5.6--py_0
$ module help quay.io/biocontainers/mageck-vispr/0.5.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mageck-vispr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mageck-vispr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mageck-vispr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mageck-vispr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mageck-vispr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mageck-vispr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RRA

```bash
$ singularity exec <container> /usr/local/bin/RRA
$ podman run --it --rm --entrypoint /usr/local/bin/RRA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RRA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mageck

```bash
$ singularity exec <container> /usr/local/bin/mageck
$ podman run --it --rm --entrypoint /usr/local/bin/mageck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mageck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mageck-vispr

```bash
$ singularity exec <container> /usr/local/bin/mageck-vispr
$ podman run --it --rm --entrypoint /usr/local/bin/mageck-vispr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mageck-vispr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mageckGSEA

```bash
$ singularity exec <container> /usr/local/bin/mageckGSEA
$ podman run --it --rm --entrypoint /usr/local/bin/mageckGSEA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mageckGSEA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vispr

```bash
$ singularity exec <container> /usr/local/bin/vispr
$ podman run --it --rm --entrypoint /usr/local/bin/vispr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vispr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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