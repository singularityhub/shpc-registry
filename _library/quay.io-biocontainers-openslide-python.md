---
layout: container
name:  "quay.io/biocontainers/openslide-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/openslide-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/openslide-python/container.yaml"
updated_at: "2024-01-28 03:44:20.809591"
latest: "1.1.1--py36h470a237_0"
container_url: "https://biocontainers.pro/tools/openslide-python"
aliases:
 - "aclocal.bak"
 - "autoheader.bak"
 - "autom4te.bak"
 - "automake.bak"
 - "autoreconf.bak"
 - "autoscan.bak"
 - "autoupdate.bak"
 - "ifnames.bak"
 - "openslide-quickhash1sum"
 - "openslide-show-properties"
 - "openslide-write-png"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
 - "gdk-pixbuf-pixdata"
 - "gdk-pixbuf-query-loaders"
 - "2to3-3.6"
versions:
 - "1.1.1--py36h470a237_0"
description: "shpc-registry automated BioContainers addition for openslide-python"
config: {"url": "https://biocontainers.pro/tools/openslide-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for openslide-python", "latest": {"1.1.1--py36h470a237_0": "sha256:8e07e05e15b3d41e524af0a43121a98523c351b27c822e20dcfc106301f397a3"}, "tags": {"1.1.1--py36h470a237_0": "sha256:8e07e05e15b3d41e524af0a43121a98523c351b27c822e20dcfc106301f397a3"}, "docker": "quay.io/biocontainers/openslide-python", "aliases": {"aclocal.bak": "/usr/local/bin/aclocal.bak", "autoheader.bak": "/usr/local/bin/autoheader.bak", "autom4te.bak": "/usr/local/bin/autom4te.bak", "automake.bak": "/usr/local/bin/automake.bak", "autoreconf.bak": "/usr/local/bin/autoreconf.bak", "autoscan.bak": "/usr/local/bin/autoscan.bak", "autoupdate.bak": "/usr/local/bin/autoupdate.bak", "ifnames.bak": "/usr/local/bin/ifnames.bak", "openslide-quickhash1sum": "/usr/local/bin/openslide-quickhash1sum", "openslide-show-properties": "/usr/local/bin/openslide-show-properties", "openslide-write-png": "/usr/local/bin/openslide-write-png", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource", "gdk-pixbuf-pixdata": "/usr/local/bin/gdk-pixbuf-pixdata", "gdk-pixbuf-query-loaders": "/usr/local/bin/gdk-pixbuf-query-loaders", "2to3-3.6": "/usr/local/bin/2to3-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/openslide-python.
shpc-registry automated BioContainers addition for openslide-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/openslide-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/openslide-python:1.1.1--py36h470a237_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/openslide-python/1.1.1--py36h470a237_0
$ module help quay.io/biocontainers/openslide-python/1.1.1--py36h470a237_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openslide-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openslide-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openslide-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openslide-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openslide-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openslide-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aclocal.bak

```bash
$ singularity exec <container> /usr/local/bin/aclocal.bak
$ podman run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoheader.bak

```bash
$ singularity exec <container> /usr/local/bin/autoheader.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autom4te.bak

```bash
$ singularity exec <container> /usr/local/bin/autom4te.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### automake.bak

```bash
$ singularity exec <container> /usr/local/bin/automake.bak
$ podman run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoreconf.bak

```bash
$ singularity exec <container> /usr/local/bin/autoreconf.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoscan.bak

```bash
$ singularity exec <container> /usr/local/bin/autoscan.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoupdate.bak

```bash
$ singularity exec <container> /usr/local/bin/autoupdate.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifnames.bak

```bash
$ singularity exec <container> /usr/local/bin/ifnames.bak
$ podman run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### openslide-quickhash1sum

```bash
$ singularity exec <container> /usr/local/bin/openslide-quickhash1sum
$ podman run --it --rm --entrypoint /usr/local/bin/openslide-quickhash1sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/openslide-quickhash1sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### openslide-show-properties

```bash
$ singularity exec <container> /usr/local/bin/openslide-show-properties
$ podman run --it --rm --entrypoint /usr/local/bin/openslide-show-properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/openslide-show-properties   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### openslide-write-png

```bash
$ singularity exec <container> /usr/local/bin/openslide-write-png
$ podman run --it --rm --entrypoint /usr/local/bin/openslide-write-png   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/openslide-write-png   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gdk-pixbuf-thumbnailer

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-thumbnailer
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-csource

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-csource
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-pixdata

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-pixdata
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-pixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-pixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-query-loaders

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-query-loaders
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-query-loaders   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-query-loaders   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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