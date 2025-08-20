---
layout: container
name:  "quay.io/biocontainers/bioconductor-metacyto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metacyto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metacyto/container.yaml"
updated_at: "2025-08-20 03:26:34.860398"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metacyto"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metacyto"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metacyto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metacyto", "latest": {"1.28.0--r44hdfd78af_0": "sha256:aa45aa8619090cc5ee169b60f4ba046397f29c9b45554714e5b27a38ac6bc036"}, "tags": {"1.8.0--r36_0": "sha256:f13dba8f43fa8e2014515b0e00aed0703b528e180bb5fd49d7cd1aa15ea58dda", "1.16.0--r41hdfd78af_0": "sha256:268c59d125ce01e10f7f213a93be5d6935e15b5864453566fbed69eb99c5f6d2", "1.14.0--r41hdfd78af_0": "sha256:586aa89f9adc08b7bc86291481a734accdb6d59878dab7d5b9e8b22997c96079", "1.12.0--r40hdfd78af_1": "sha256:d6a4693b44292a1fbc409e497e9cd6874ae6490fc2d01007fc0326745fbffae3", "1.10.0--r40_0": "sha256:9916341d63c014b52217278e53299a22d4eb11ed51db37c17b3a541970e48d12", "1.20.0--r42hdfd78af_0": "sha256:82956e9ec8289b10083d1ba459259ea67bbd4c2f2d166753f19073e3c59ade41", "1.22.0--r43hdfd78af_0": "sha256:8478f71363918bc741c1a5a7ef46fd0784303ca48b3f91a5606b02f7660a1a1d", "1.24.0--r43hdfd78af_0": "sha256:2d4f9ab53be3b30277094d9a46d10fe7ad1e2e5e28ae80eb384bb82fb2faee3e", "1.28.0--r44hdfd78af_0": "sha256:aa45aa8619090cc5ee169b60f4ba046397f29c9b45554714e5b27a38ac6bc036"}, "docker": "quay.io/biocontainers/bioconductor-metacyto", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metacyto.
shpc-registry automated BioContainers addition for bioconductor-metacyto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metacyto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metacyto:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metacyto/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metacyto/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metacyto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metacyto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metacyto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metacyto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metacyto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metacyto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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