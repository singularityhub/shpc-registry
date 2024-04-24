---
layout: container
name:  "quay.io/biocontainers/bioconductor-impulsede"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-impulsede/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-impulsede/container.yaml"
updated_at: "2024-04-24 02:55:40.434406"
latest: "1.13.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-impulsede"

versions:
 - "1.8.0--r351_0"
 - "1.13.0--r40_0"
 - "1.12.0--r36_0"
 - "1.10.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-impulsede"
config: {"url": "https://biocontainers.pro/tools/bioconductor-impulsede", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-impulsede", "latest": {"1.13.0--r40_0": "sha256:4991adb88d2ff921b76ea28334cb2b7fc2f3032230d32fc86f12eeee843aeb72"}, "tags": {"1.8.0--r351_0": "sha256:6c37a9925803ce608c9ac6571088b36a111822e4d1a1774f8d62e8f5e3a65630", "1.13.0--r40_0": "sha256:4991adb88d2ff921b76ea28334cb2b7fc2f3032230d32fc86f12eeee843aeb72", "1.12.0--r36_0": "sha256:4a2f5f06ec740fa49e832bacc459a54371826eced695ae08a8811c3bba2ffda3", "1.10.0--r36_1": "sha256:882359ecfedb593f41d27d1422df47e9e9523d9cc221fa1810c54b9da168a2de"}, "docker": "quay.io/biocontainers/bioconductor-impulsede"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-impulsede.
shpc-registry automated BioContainers addition for bioconductor-impulsede
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-impulsede
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-impulsede:1.13.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-impulsede/1.13.0--r40_0
$ module help quay.io/biocontainers/bioconductor-impulsede/1.13.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-impulsede-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-impulsede-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-impulsede-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-impulsede-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-impulsede-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-impulsede-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-impulsede

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