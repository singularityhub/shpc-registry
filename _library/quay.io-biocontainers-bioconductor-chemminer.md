---
layout: container
name:  "quay.io/biocontainers/bioconductor-chemminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chemminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chemminer/container.yaml"
updated_at: "2025-09-11 05:05:58.260776"
latest: "3.58.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chemminer"
aliases:
 - "rsvg-convert"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
 - "gdk-pixbuf-pixdata"
 - "gdk-pixbuf-query-loaders"
versions:
 - "3.46.0--r41hc247a5b_2"
 - "3.50.0--r42hc247a5b_0"
 - "3.50.0--r42hf17093f_1"
 - "3.52.0--r43hf17093f_0"
 - "3.54.0--r43hf17093f_0"
 - "3.58.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chemminer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chemminer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chemminer", "latest": {"3.58.0--r44he5774e6_0": "sha256:5b154b0d777e655d57813e3ceb6c436c567521053dd0986e49a072ff21992bf5"}, "tags": {"3.46.0--r41hc247a5b_2": "sha256:d78371c0f7c155ca817fa8f0c7f0b7a01f433f57bb68b32a137b536934c532c1", "3.50.0--r42hc247a5b_0": "sha256:67531a786f200a2233f79173bbb09f7d5939293852b61d6447fc0cdc390fe03f", "3.50.0--r42hf17093f_1": "sha256:5eb82204d243f57071ebea7405fef67594781bc0b0f22632db6e6f41c37b9986", "3.52.0--r43hf17093f_0": "sha256:108ea1c77c615f5beea8138373ce22f1c19f8a782df71f42c73425bbca4b3fe0", "3.54.0--r43hf17093f_0": "sha256:083c63ee49aa9530a2dbd6c6cbd36bcf49482c2d70775ab2e43c47e681e419f6", "3.58.0--r44he5774e6_0": "sha256:5b154b0d777e655d57813e3ceb6c436c567521053dd0986e49a072ff21992bf5"}, "docker": "quay.io/biocontainers/bioconductor-chemminer", "aliases": {"rsvg-convert": "/usr/local/bin/rsvg-convert", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource", "gdk-pixbuf-pixdata": "/usr/local/bin/gdk-pixbuf-pixdata", "gdk-pixbuf-query-loaders": "/usr/local/bin/gdk-pixbuf-query-loaders"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chemminer.
shpc-registry automated BioContainers addition for bioconductor-chemminer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chemminer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chemminer:3.58.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chemminer/3.58.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-chemminer/3.58.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chemminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chemminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chemminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chemminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chemminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chemminer-inspect-deffile:

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