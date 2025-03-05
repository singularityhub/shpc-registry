---
layout: container
name:  "quay.io/biocontainers/ea-utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ea-utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ea-utils/container.yaml"
updated_at: "2025-03-05 03:36:30.454812"
latest: "1.1.2.779--h543ed2d_2"
container_url: "https://biocontainers.pro/tools/ea-utils"
aliases:
 - "alc"
 - "determine-phred"
 - "fastq-clipper"
 - "fastq-join"
 - "fastq-mcf"
 - "fastq-multx"
 - "fastq-stats"
 - "fastx-graph"
 - "randomFQ"
 - "sam-stats"
 - "varcall"
versions:
 - "1.1.2.779--h543ed2d_2"
description: "shpc-registry automated BioContainers addition for ea-utils"
config: {"url": "https://biocontainers.pro/tools/ea-utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ea-utils", "latest": {"1.1.2.779--h543ed2d_2": "sha256:35e5bcaaf423f9f49e6ebeff426687974b8ab51d46befd189b82bb2d6dd08496"}, "tags": {"1.1.2.779--h543ed2d_2": "sha256:35e5bcaaf423f9f49e6ebeff426687974b8ab51d46befd189b82bb2d6dd08496"}, "docker": "quay.io/biocontainers/ea-utils", "aliases": {"alc": "/usr/local/bin/alc", "determine-phred": "/usr/local/bin/determine-phred", "fastq-clipper": "/usr/local/bin/fastq-clipper", "fastq-join": "/usr/local/bin/fastq-join", "fastq-mcf": "/usr/local/bin/fastq-mcf", "fastq-multx": "/usr/local/bin/fastq-multx", "fastq-stats": "/usr/local/bin/fastq-stats", "fastx-graph": "/usr/local/bin/fastx-graph", "randomFQ": "/usr/local/bin/randomFQ", "sam-stats": "/usr/local/bin/sam-stats", "varcall": "/usr/local/bin/varcall"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ea-utils.
shpc-registry automated BioContainers addition for ea-utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ea-utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ea-utils:1.1.2.779--h543ed2d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ea-utils/1.1.2.779--h543ed2d_2
$ module help quay.io/biocontainers/ea-utils/1.1.2.779--h543ed2d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ea-utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ea-utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ea-utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ea-utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ea-utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ea-utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alc

```bash
$ singularity exec <container> /usr/local/bin/alc
$ podman run --it --rm --entrypoint /usr/local/bin/alc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### determine-phred

```bash
$ singularity exec <container> /usr/local/bin/determine-phred
$ podman run --it --rm --entrypoint /usr/local/bin/determine-phred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/determine-phred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-clipper

```bash
$ singularity exec <container> /usr/local/bin/fastq-clipper
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-clipper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-clipper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-join

```bash
$ singularity exec <container> /usr/local/bin/fastq-join
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-mcf

```bash
$ singularity exec <container> /usr/local/bin/fastq-mcf
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-mcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-mcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-multx

```bash
$ singularity exec <container> /usr/local/bin/fastq-multx
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-multx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-multx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-stats

```bash
$ singularity exec <container> /usr/local/bin/fastq-stats
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastx-graph

```bash
$ singularity exec <container> /usr/local/bin/fastx-graph
$ podman run --it --rm --entrypoint /usr/local/bin/fastx-graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastx-graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randomFQ

```bash
$ singularity exec <container> /usr/local/bin/randomFQ
$ podman run --it --rm --entrypoint /usr/local/bin/randomFQ   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randomFQ   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam-stats

```bash
$ singularity exec <container> /usr/local/bin/sam-stats
$ podman run --it --rm --entrypoint /usr/local/bin/sam-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varcall

```bash
$ singularity exec <container> /usr/local/bin/varcall
$ podman run --it --rm --entrypoint /usr/local/bin/varcall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varcall   -v ${PWD} -w ${PWD} <container> -c " $@"
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