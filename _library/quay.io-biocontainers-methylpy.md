---
layout: container
name:  "quay.io/biocontainers/methylpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/methylpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/methylpy/container.yaml"
updated_at: "2025-05-24 11:28:56.381341"
latest: "1.4.7--py310h2401223_0"
container_url: "https://biocontainers.pro/tools/methylpy"
aliases:
 - "methylpy"
 - "wigToBigWig"
 - "picard"
 - "cutadapt"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
versions:
 - "1.4.3--py27h41a55b7_0"
 - "1.4.7--py310h2401223_0"
 - "1.4.7--py39h0ae133c_0"
description: "shpc-registry automated BioContainers addition for methylpy"
config: {"url": "https://biocontainers.pro/tools/methylpy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for methylpy", "latest": {"1.4.7--py310h2401223_0": "sha256:f78225877896bb8fe3a7099463952fcebb40205637f1a4d3de4b364e40e82aa1"}, "tags": {"1.4.3--py27h41a55b7_0": "sha256:c4b8fa9f4e0743dd78d19f9848ebf006a19cac5f0fd760843e75913eb0abab3e", "1.4.7--py310h2401223_0": "sha256:f78225877896bb8fe3a7099463952fcebb40205637f1a4d3de4b364e40e82aa1", "1.4.7--py39h0ae133c_0": "sha256:51c17eafe1de735415b1d1a878af025b64a17d4e4de0775117b5bdec857adfb6"}, "docker": "quay.io/biocontainers/methylpy", "aliases": {"methylpy": "/usr/local/bin/methylpy", "wigToBigWig": "/usr/local/bin/wigToBigWig", "picard": "/usr/local/bin/picard", "cutadapt": "/usr/local/bin/cutadapt", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/methylpy.
shpc-registry automated BioContainers addition for methylpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/methylpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/methylpy:1.4.7--py310h2401223_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/methylpy/1.4.7--py310h2401223_0
$ module help quay.io/biocontainers/methylpy/1.4.7--py310h2401223_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### methylpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### methylpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### methylpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### methylpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### methylpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### methylpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### methylpy

```bash
$ singularity exec <container> /usr/local/bin/methylpy
$ podman run --it --rm --entrypoint /usr/local/bin/methylpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methylpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
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