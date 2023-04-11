---
layout: container
name:  "quay.io/biocontainers/bioconductor-scshapes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scshapes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scshapes/container.yaml"
updated_at: "2023-04-11 03:04:53.098919"
latest: "1.4.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scshapes"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scshapes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scshapes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scshapes", "latest": {"1.4.0--r42hdfd78af_0": "sha256:a30bd817bf8a773f555fecd595ef0baf6abf74d50358acff640c27a96c562b88"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:f7be7ced7ebdec3ff1e62e3e095a0c6acffd875108485f0456028cb16723c210", "1.4.0--r42hdfd78af_0": "sha256:a30bd817bf8a773f555fecd595ef0baf6abf74d50358acff640c27a96c562b88"}, "docker": "quay.io/biocontainers/bioconductor-scshapes"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scshapes.
shpc-registry automated BioContainers addition for bioconductor-scshapes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scshapes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scshapes:1.4.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scshapes/1.4.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scshapes/1.4.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scshapes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scshapes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scshapes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scshapes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scshapes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scshapes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scshapes

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