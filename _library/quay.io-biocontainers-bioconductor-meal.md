---
layout: container
name:  "quay.io/biocontainers/bioconductor-meal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-meal/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-meal/container.yaml"
updated_at: "2022-10-27 01:04:35.143845"
latest: "1.22.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-meal"
aliases:
 - ".bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-post-link.sh"
 - ".bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-pre-unlink.sh"
 - ".bioconductor-illuminahumanmethylationepicmanifest-post-link.sh"
 - ".bioconductor-illuminahumanmethylationepicmanifest-pre-unlink.sh"
versions:
 - "1.22.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-meal"
config: {"url": "https://biocontainers.pro/tools/bioconductor-meal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-meal", "latest": {"1.22.0--r41hdfd78af_0": "sha256:ad758e9b629f507571ffc0460256d19ac2faf5193395dacbebba2874b12c777a"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:ad758e9b629f507571ffc0460256d19ac2faf5193395dacbebba2874b12c777a"}, "docker": "quay.io/biocontainers/bioconductor-meal", "aliases": {".bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-post-link.sh": "/usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-post-link.sh", ".bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-pre-unlink.sh": "/usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-pre-unlink.sh", ".bioconductor-illuminahumanmethylationepicmanifest-post-link.sh": "/usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-post-link.sh", ".bioconductor-illuminahumanmethylationepicmanifest-pre-unlink.sh": "/usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-meal.
shpc-registry automated BioContainers addition for bioconductor-meal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-meal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-meal:1.22.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-meal/1.22.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-meal/1.22.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-meal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-meal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-meal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-meal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicanno.ilm10b4.hg19-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-illuminahumanmethylationepicmanifest-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-illuminahumanmethylationepicmanifest-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-illuminahumanmethylationepicmanifest-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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