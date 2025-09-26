---
layout: container
name:  "quay.io/biocontainers/graphicsmagick"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphicsmagick/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/graphicsmagick/container.yaml"
updated_at: "2025-09-26 03:28:26.250793"
latest: "1.3.45"
container_url: "https://biocontainers.pro/tools/graphicsmagick"
aliases:
 - "GraphicsMagick++-config"
 - "GraphicsMagick-config"
 - "GraphicsMagickWand-config"
 - "gm"
 - "chrpath"
 - "g-ir-doc-tool"
 - "gnuplot"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "compile-et.pl"
 - "gdlib-config"
versions:
 - "1.3.31"
 - "1.3.42"
 - "1.3.43"
 - "1.3.44"
 - "1.3.45"
description: "shpc-registry automated BioContainers addition for graphicsmagick"
config: {"url": "https://biocontainers.pro/tools/graphicsmagick", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphicsmagick", "latest": {"1.3.45": "sha256:650a5cc5cc320628bf9f7c03eaebd3ade303efc0633ebeeadffc9e7106e6a4d6"}, "tags": {"1.3.31": "sha256:35d1a1cf270b5968e7adc8dd2c42324917729004784f740a39139b74543cf124", "1.3.42": "sha256:45989dbbf99e793a5a8702543a8a9c7f0a58693f01884ff302e84c0ea83d2a45", "1.3.43": "sha256:f052a92264afa84157f28832cbac6216d51c3dcd7477104af99f041396d68dc7", "1.3.44": "sha256:96befa22774a532ef2ddb6a6fd902c5c10d16aada7887103791976c6b9fabc47", "1.3.45": "sha256:650a5cc5cc320628bf9f7c03eaebd3ade303efc0633ebeeadffc9e7106e6a4d6"}, "docker": "quay.io/biocontainers/graphicsmagick", "aliases": {"GraphicsMagick++-config": "/usr/local/bin/GraphicsMagick++-config", "GraphicsMagick-config": "/usr/local/bin/GraphicsMagick-config", "GraphicsMagickWand-config": "/usr/local/bin/GraphicsMagickWand-config", "gm": "/usr/local/bin/gm", "chrpath": "/usr/local/bin/chrpath", "g-ir-doc-tool": "/usr/local/bin/g-ir-doc-tool", "gnuplot": "/usr/local/bin/gnuplot", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "compile-et.pl": "/usr/local/bin/compile-et.pl", "gdlib-config": "/usr/local/bin/gdlib-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphicsmagick.
shpc-registry automated BioContainers addition for graphicsmagick
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphicsmagick
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphicsmagick:1.3.45
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphicsmagick/1.3.45
$ module help quay.io/biocontainers/graphicsmagick/1.3.45
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphicsmagick-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphicsmagick-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphicsmagick-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphicsmagick-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphicsmagick-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphicsmagick-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GraphicsMagick++-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GraphicsMagick-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagick-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagick-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagick-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GraphicsMagickWand-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagickWand-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gm

```bash
$ singularity exec <container> /usr/local/bin/gm
$ podman run --it --rm --entrypoint /usr/local/bin/gm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrpath

```bash
$ singularity exec <container> /usr/local/bin/chrpath
$ podman run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-doc-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-doc-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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