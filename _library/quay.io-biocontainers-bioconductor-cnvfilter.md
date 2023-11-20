---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvfilter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvfilter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvfilter/container.yaml"
updated_at: "2023-11-20 03:06:02.386290"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvfilter"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvfilter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvfilter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvfilter", "latest": {"1.14.0--r43hdfd78af_0": "sha256:bc5ef191805e47ed67ef03df469b5e7ff3428ba772184ecb8856d0ce4662398a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:87e1b922d36ac7add00aac9a152db5a98b688ef2b8757c843f9436c3c425a47a", "1.12.0--r42hdfd78af_0": "sha256:c0ab27d89a89044968d6242afb31747b1b376338e5b79b6b4f73bded6dd5175b", "1.14.0--r43hdfd78af_0": "sha256:bc5ef191805e47ed67ef03df469b5e7ff3428ba772184ecb8856d0ce4662398a"}, "docker": "quay.io/biocontainers/bioconductor-cnvfilter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvfilter.
shpc-registry automated BioContainers addition for bioconductor-cnvfilter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvfilter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvfilter:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvfilter/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnvfilter/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnvfilter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvfilter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvfilter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnvfilter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnvfilter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnvfilter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cnvfilter

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