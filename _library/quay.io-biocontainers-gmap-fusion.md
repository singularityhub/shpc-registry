---
layout: container
name:  "quay.io/biocontainers/gmap-fusion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmap-fusion/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gmap-fusion/container.yaml"
updated_at: "2022-10-29 05:30:18.166362"
latest: "0.4.0--2"
container_url: "https://biocontainers.pro/tools/gmap-fusion"
aliases:
 - "GMAP-fusion"
 - "gmap_compress"
 - "gmap_reassemble"
 - "gmap_uncompress"
 - "2to3-3.7"
 - "ace2sam"
 - "atoiindex"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
versions:
 - "0.4.0--2"
description: "shpc-registry automated BioContainers addition for gmap-fusion"
config: {"url": "https://biocontainers.pro/tools/gmap-fusion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gmap-fusion", "latest": {"0.4.0--2": "sha256:40465100fd9563473496cc6d56e303b77cc691079a934db0e1b65b4a3f677e4f"}, "tags": {"0.4.0--2": "sha256:40465100fd9563473496cc6d56e303b77cc691079a934db0e1b65b4a3f677e4f"}, "docker": "quay.io/biocontainers/gmap-fusion", "aliases": {"GMAP-fusion": "/usr/local/bin/GMAP-fusion", "gmap_compress": "/usr/local/bin/gmap_compress", "gmap_reassemble": "/usr/local/bin/gmap_reassemble", "gmap_uncompress": "/usr/local/bin/gmap_uncompress", "2to3-3.7": "/usr/local/bin/2to3-3.7", "ace2sam": "/usr/local/bin/ace2sam", "atoiindex": "/usr/local/bin/atoiindex", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmap-fusion.
shpc-registry automated BioContainers addition for gmap-fusion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmap-fusion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmap-fusion:0.4.0--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmap-fusion/0.4.0--2
$ module help quay.io/biocontainers/gmap-fusion/0.4.0--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmap-fusion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmap-fusion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmap-fusion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmap-fusion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmap-fusion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmap-fusion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GMAP-fusion

```bash
$ singularity exec <container> /usr/local/bin/GMAP-fusion
$ podman run --it --rm --entrypoint /usr/local/bin/GMAP-fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMAP-fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_compress

```bash
$ singularity exec <container> /usr/local/bin/gmap_compress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_reassemble

```bash
$ singularity exec <container> /usr/local/bin/gmap_reassemble
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_uncompress

```bash
$ singularity exec <container> /usr/local/bin/gmap_uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### atoiindex

```bash
$ singularity exec <container> /usr/local/bin/atoiindex
$ podman run --it --rm --entrypoint /usr/local/bin/atoiindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atoiindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
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