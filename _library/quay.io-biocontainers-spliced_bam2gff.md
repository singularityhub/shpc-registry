---
layout: container
name:  "quay.io/biocontainers/spliced_bam2gff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spliced_bam2gff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spliced_bam2gff/container.yaml"
updated_at: "2024-12-22 03:42:02.199647"
latest: "1.3--he881be0_1"
container_url: "https://biocontainers.pro/tools/spliced_bam2gff"
aliases:
 - "spliced_bam2gff"
versions:
 - "1.3--he881be0_1"
description: "shpc-registry automated BioContainers addition for spliced_bam2gff"
config: {"url": "https://biocontainers.pro/tools/spliced_bam2gff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spliced_bam2gff", "latest": {"1.3--he881be0_1": "sha256:d7e58276fc432139fe6ffa4d35971a6fd5d9c471e7741487428ef54c3ce9479c"}, "tags": {"1.3--he881be0_1": "sha256:d7e58276fc432139fe6ffa4d35971a6fd5d9c471e7741487428ef54c3ce9479c"}, "docker": "quay.io/biocontainers/spliced_bam2gff", "aliases": {"spliced_bam2gff": "/usr/local/bin/spliced_bam2gff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spliced_bam2gff.
shpc-registry automated BioContainers addition for spliced_bam2gff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spliced_bam2gff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spliced_bam2gff:1.3--he881be0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spliced_bam2gff/1.3--he881be0_1
$ module help quay.io/biocontainers/spliced_bam2gff/1.3--he881be0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spliced_bam2gff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spliced_bam2gff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spliced_bam2gff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spliced_bam2gff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spliced_bam2gff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spliced_bam2gff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spliced_bam2gff

```bash
$ singularity exec <container> /usr/local/bin/spliced_bam2gff
$ podman run --it --rm --entrypoint /usr/local/bin/spliced_bam2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spliced_bam2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
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