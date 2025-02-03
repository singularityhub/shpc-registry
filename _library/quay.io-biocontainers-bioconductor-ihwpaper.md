---
layout: container
name:  "quay.io/biocontainers/bioconductor-ihwpaper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ihwpaper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ihwpaper/container.yaml"
updated_at: "2025-02-03 04:06:34.178182"
latest: "1.34.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ihwpaper"

versions:
 - "1.22.0--r41hc247a5b_3"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
 - "1.34.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ihwpaper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ihwpaper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ihwpaper", "latest": {"1.34.0--r44he5774e6_0": "sha256:f8ea2b3da115421723e6014efd168382e3662c76e42edc94ca697ecd38022fb0"}, "tags": {"1.22.0--r41hc247a5b_3": "sha256:899941e3143bd2b9b80e43444383dd640d5df975e39e80087aceacc8cb0459de", "1.26.0--r42hc247a5b_0": "sha256:be22946a3a16ebf4f7f15f306fb5fe1a8fe82583e618d82bda8f5c0587611a01", "1.26.0--r42hf17093f_1": "sha256:1c6fac7eaab17bb26e2180fc5ffb70546b005f6d7b493d4da644336242244d7e", "1.28.0--r43hf17093f_0": "sha256:12bdfebf538d9f12dd61915fded94f517f295cdad943f295a5a1b433582ef6a7", "1.34.0--r44he5774e6_0": "sha256:f8ea2b3da115421723e6014efd168382e3662c76e42edc94ca697ecd38022fb0"}, "docker": "quay.io/biocontainers/bioconductor-ihwpaper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ihwpaper.
shpc-registry automated BioContainers addition for bioconductor-ihwpaper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ihwpaper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ihwpaper:1.34.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ihwpaper/1.34.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-ihwpaper/1.34.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ihwpaper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ihwpaper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ihwpaper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ihwpaper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ihwpaper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ihwpaper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ihwpaper

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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