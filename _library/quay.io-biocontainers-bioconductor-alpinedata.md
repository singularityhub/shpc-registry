---
layout: container
name:  "quay.io/biocontainers/bioconductor-alpinedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-alpinedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-alpinedata/container.yaml"
updated_at: "2024-11-10 03:36:20.094679"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-alpinedata"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-alpinedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-alpinedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-alpinedata", "latest": {"1.26.0--r43hdfd78af_0": "sha256:c0e167ebe96d73034bba182134e83851fcf68558d33f33951148c9fb5ec8851d"}, "tags": {"1.8.0--r351_0": "sha256:b6b39e16b6cb0ed1f46b051eb281bce9146ebba308dbd3de2f4ffbb9fcfa69d5", "1.24.0--r42hdfd78af_0": "sha256:5c0c8da6dc15dc7fb836b725f34e4d59af3a7033618abb362a14ee34f5b5ec1f", "1.20.0--r41hdfd78af_1": "sha256:2bf864bd89fa69200b99dd5ac05417a27bcc2da0e8ee7c829c39c3b2247834be", "1.18.0--r41hdfd78af_0": "sha256:17918454d1eea13c4cee84c0ed55a234b70010555b5f3ebb3a70c279ce58b5a5", "1.16.0--r40hdfd78af_1": "sha256:0a6d329161b5030b62783bd5ab291d2cf2f83874173a455dde4bf26586983e13", "1.14.0--r40_0": "sha256:9a6459775bbe4353346208e0ed5516b72d4bf2670fa826b19b1ac4ec99bce068", "1.26.0--r43hdfd78af_0": "sha256:c0e167ebe96d73034bba182134e83851fcf68558d33f33951148c9fb5ec8851d"}, "docker": "quay.io/biocontainers/bioconductor-alpinedata", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-alpinedata.
shpc-registry automated BioContainers addition for bioconductor-alpinedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-alpinedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-alpinedata:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-alpinedata/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-alpinedata/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-alpinedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alpinedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alpinedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-alpinedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-alpinedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-alpinedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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