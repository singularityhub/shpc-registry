---
layout: container
name:  "quay.io/biocontainers/bioconductor-fmcsr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fmcsr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fmcsr/container.yaml"
updated_at: "2024-05-07 03:16:23.796913"
latest: "1.44.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fmcsr"
aliases:
 - "rsvg-convert"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
 - "gdk-pixbuf-pixdata"
 - "gdk-pixbuf-query-loaders"
versions:
 - "1.36.0--r41hc247a5b_2"
 - "1.40.0--r42hc247a5b_0"
 - "1.40.0--r42hf17093f_1"
 - "1.42.0--r43hf17093f_0"
 - "1.44.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fmcsr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fmcsr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fmcsr", "latest": {"1.44.0--r43hf17093f_0": "sha256:87a8945801baaaa62b84815e532cb6daf68e5d8a234facac5f8a153b585f2b2c"}, "tags": {"1.36.0--r41hc247a5b_2": "sha256:042cde91e3d0b262e80e0852d811d3d465c90417fe2a34329529ec214b212e12", "1.40.0--r42hc247a5b_0": "sha256:3ec1e4bfb931bf792aa5b853e75e9f63398c7de2795533c7f5a13f77069ea4ee", "1.40.0--r42hf17093f_1": "sha256:1b09eae278980efe67061cefd49a1b9c2ebb795b33ddbf026d5fa418973d4b45", "1.42.0--r43hf17093f_0": "sha256:3355e14679a335d2711e78be6ac6f7b30971e0259291ff6a13a031f8a593ed0f", "1.44.0--r43hf17093f_0": "sha256:87a8945801baaaa62b84815e532cb6daf68e5d8a234facac5f8a153b585f2b2c"}, "docker": "quay.io/biocontainers/bioconductor-fmcsr", "aliases": {"rsvg-convert": "/usr/local/bin/rsvg-convert", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource", "gdk-pixbuf-pixdata": "/usr/local/bin/gdk-pixbuf-pixdata", "gdk-pixbuf-query-loaders": "/usr/local/bin/gdk-pixbuf-query-loaders"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fmcsr.
shpc-registry automated BioContainers addition for bioconductor-fmcsr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fmcsr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fmcsr:1.44.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fmcsr/1.44.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-fmcsr/1.44.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fmcsr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fmcsr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fmcsr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fmcsr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fmcsr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fmcsr-inspect-deffile:

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