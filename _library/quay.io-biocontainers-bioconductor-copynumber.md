---
layout: container
name:  "quay.io/biocontainers/bioconductor-copynumber"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-copynumber/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-copynumber/container.yaml"
updated_at: "2025-11-21 15:46:58.335922"
latest: "1.38.0--r44hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-copynumber"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.38.0--r44hdfd78af_1"
 - "1.38.0--r44hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-copynumber"
config: {"url": "https://biocontainers.pro/tools/bioconductor-copynumber", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-copynumber", "latest": {"1.38.0--r44hdfd78af_2": "sha256:1bdfb40224cbb375831bf77e2c5328ef93b3ac9a2211244ce399e0b4483a9d49"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:90c45c1f7614ae1d90889193736f77f9e1d5db13d7937f7cedce8733ee1bd468", "1.38.0--r42hdfd78af_0": "sha256:7e7081948aeeb68a66236eebb606eeb1c78d39014bcd4c81da495d89b975abbe", "1.38.0--r44hdfd78af_1": "sha256:548e686ddca3cfc21a891a4d3cc039242104a2765821407ad52d859985e8ce7d", "1.38.0--r44hdfd78af_2": "sha256:1bdfb40224cbb375831bf77e2c5328ef93b3ac9a2211244ce399e0b4483a9d49"}, "docker": "quay.io/biocontainers/bioconductor-copynumber"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-copynumber.
shpc-registry automated BioContainers addition for bioconductor-copynumber
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-copynumber
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-copynumber:1.38.0--r44hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-copynumber/1.38.0--r44hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-copynumber/1.38.0--r44hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-copynumber-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copynumber-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copynumber-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-copynumber-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-copynumber-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-copynumber-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-copynumber

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