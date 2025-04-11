---
layout: container
name:  "quay.io/biocontainers/bioconductor-htmg430pmcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htmg430pmcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htmg430pmcdf/container.yaml"
updated_at: "2025-04-11 03:05:54.834476"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-htmg430pmcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-htmg430pmcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htmg430pmcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htmg430pmcdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:2e676ab0c4feefdf092bd37ef37a6c4412cbe745dd66da8acbe38ab96743b739"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:12fef4e06e32ad33b8c5a09aa15b3e5b6bc5ef2a3ae585f057d3078b2e0dbc1e", "2.18.0--r42hdfd78af_10": "sha256:6f65609e9550efc1d2dc69ec4e6f5d7b5424a651b5a870f16c01f380215d9d13", "2.18.0--r43hdfd78af_11": "sha256:31a10ca5679f3849bde78e1551499cab592925c0df53ccba43152427c8da8111", "2.18.0--r43hdfd78af_12": "sha256:b446a9c721cc0d0f490ec13bc4e48a24d0e03dc36c73b2840c99ba8ccfb9aec8", "2.18.0--r44hdfd78af_13": "sha256:2e676ab0c4feefdf092bd37ef37a6c4412cbe745dd66da8acbe38ab96743b739"}, "docker": "quay.io/biocontainers/bioconductor-htmg430pmcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htmg430pmcdf.
shpc-registry automated BioContainers addition for bioconductor-htmg430pmcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430pmcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430pmcdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htmg430pmcdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-htmg430pmcdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htmg430pmcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430pmcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430pmcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htmg430pmcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htmg430pmcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htmg430pmcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htmg430pmcdf

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