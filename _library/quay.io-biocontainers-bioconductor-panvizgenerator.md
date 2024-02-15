---
layout: container
name:  "quay.io/biocontainers/bioconductor-panvizgenerator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-panvizgenerator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-panvizgenerator/container.yaml"
updated_at: "2024-02-15 03:43:13.336373"
latest: "1.22.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-panvizgenerator"

versions:
 - "1.22.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-panvizgenerator"
config: {"url": "https://biocontainers.pro/tools/bioconductor-panvizgenerator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-panvizgenerator", "latest": {"1.22.0--r41hdfd78af_0": "sha256:0ec433cc0d04f2e700c5d1fb0ac3aa34fa8ae12924eb4c54f44a72042378c41c"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:0ec433cc0d04f2e700c5d1fb0ac3aa34fa8ae12924eb4c54f44a72042378c41c"}, "docker": "quay.io/biocontainers/bioconductor-panvizgenerator"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-panvizgenerator.
shpc-registry automated BioContainers addition for bioconductor-panvizgenerator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-panvizgenerator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-panvizgenerator:1.22.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-panvizgenerator/1.22.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-panvizgenerator/1.22.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-panvizgenerator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panvizgenerator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panvizgenerator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-panvizgenerator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-panvizgenerator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-panvizgenerator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-panvizgenerator

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