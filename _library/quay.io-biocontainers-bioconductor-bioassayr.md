---
layout: container
name:  "quay.io/biocontainers/bioconductor-bioassayr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bioassayr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bioassayr/container.yaml"
updated_at: "2025-04-06 03:45:46.664138"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bioassayr"
aliases:
 - "rsvg-convert"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
 - "gdk-pixbuf-pixdata"
 - "gdk-pixbuf-query-loaders"
versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bioassayr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bioassayr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bioassayr", "latest": {"1.44.0--r44hdfd78af_0": "sha256:16a3d3fc6fa67196e4858af740634c4f2bf15d6cc0458f68ef80b5dd237ac496"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:880e1f15a46896dee9b3620134dfc45d66af334170f7472b81957bb8995a8b0c", "1.36.0--r42hdfd78af_0": "sha256:10230fa3f9d49ffe443345fba069d585bf4862ea924d4adabbf74af972da3aa0", "1.38.0--r43hdfd78af_0": "sha256:9f4412593808c6eb4bbf9d0a79912589a0e186df6a0890a3041c29ad56764867", "1.40.0--r43hdfd78af_0": "sha256:449aaa41ef19ba14bb1961733a89ddb20fb9d43acd0921346c303903010ff63a", "1.44.0--r44hdfd78af_0": "sha256:16a3d3fc6fa67196e4858af740634c4f2bf15d6cc0458f68ef80b5dd237ac496"}, "docker": "quay.io/biocontainers/bioconductor-bioassayr", "aliases": {"rsvg-convert": "/usr/local/bin/rsvg-convert", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource", "gdk-pixbuf-pixdata": "/usr/local/bin/gdk-pixbuf-pixdata", "gdk-pixbuf-query-loaders": "/usr/local/bin/gdk-pixbuf-query-loaders"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bioassayr.
shpc-registry automated BioContainers addition for bioconductor-bioassayr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bioassayr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bioassayr:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bioassayr/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bioassayr/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bioassayr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioassayr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioassayr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bioassayr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bioassayr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bioassayr-inspect-deffile:

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