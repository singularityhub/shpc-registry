---
layout: container
name:  "quay.io/biocontainers/bioconductor-eir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eir/container.yaml"
updated_at: "2024-10-31 03:48:21.058505"
latest: "1.42.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-eir"
aliases:
 - "rsvg-convert"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
 - "gdk-pixbuf-pixdata"
 - "gdk-pixbuf-query-loaders"
versions:
 - "1.34.0--r41hc247a5b_2"
 - "1.38.0--r42hc247a5b_0"
 - "1.38.0--r42hf17093f_1"
 - "1.40.0--r43hf17093f_0"
 - "1.42.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-eir"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-eir", "latest": {"1.42.0--r43hf17093f_0": "sha256:4b248dbc8e8759eca50220bb9ee234990367ef84493daa7ea71da6bc6ad72af0"}, "tags": {"1.34.0--r41hc247a5b_2": "sha256:2fbb2bc95428289a24ddce95824f0dbde014016fcbf66d18a78411c7501f1e64", "1.38.0--r42hc247a5b_0": "sha256:7b1c86afdea6e0cd60ab278ff18da230f439a3dfb493623eca205876cc7af2b7", "1.38.0--r42hf17093f_1": "sha256:e9a7d64cfafbc68d9c108d0aad21858b7f87c4d4c909b6acaeb07edac32fdd3a", "1.40.0--r43hf17093f_0": "sha256:b60efadd200bef6dd8263704ddc5c348e49bae5bf6ef2be73d9744f2ade81b65", "1.42.0--r43hf17093f_0": "sha256:4b248dbc8e8759eca50220bb9ee234990367ef84493daa7ea71da6bc6ad72af0"}, "docker": "quay.io/biocontainers/bioconductor-eir", "aliases": {"rsvg-convert": "/usr/local/bin/rsvg-convert", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource", "gdk-pixbuf-pixdata": "/usr/local/bin/gdk-pixbuf-pixdata", "gdk-pixbuf-query-loaders": "/usr/local/bin/gdk-pixbuf-query-loaders"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eir.
shpc-registry automated BioContainers addition for bioconductor-eir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eir:1.42.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eir/1.42.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-eir/1.42.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rsvg-convert

```bash
$ singularity exec <container> /usr/local/bin/rsvg-convert
$ podman run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
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