---
layout: container
name:  "quay.io/biocontainers/bioconductor-emdomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-emdomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-emdomics/container.yaml"
updated_at: "2024-10-17 03:38:44.260229"
latest: "2.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-emdomics"

versions:
 - "2.24.0--r41hdfd78af_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-emdomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-emdomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-emdomics", "latest": {"2.32.0--r43hdfd78af_0": "sha256:d984600dbf83eb07ee56d9b122818e0dc87b5ff6e37dc0330a2c5a431ad68f34"}, "tags": {"2.24.0--r41hdfd78af_0": "sha256:cee172f799878bc2035ef7fe70d3514d75db443a305db71b402d37fccbe409b6", "2.28.0--r42hdfd78af_0": "sha256:7ec38a428177cf19155cc0dacbf3aae8d32f0f75973d4d3979a5dbb64c24e1fc", "2.30.0--r43hdfd78af_0": "sha256:9c4b3584808e73a219c3bc6845c25d2188c396662c40725f5e6554e2a07d3894", "2.32.0--r43hdfd78af_0": "sha256:d984600dbf83eb07ee56d9b122818e0dc87b5ff6e37dc0330a2c5a431ad68f34"}, "docker": "quay.io/biocontainers/bioconductor-emdomics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-emdomics.
shpc-registry automated BioContainers addition for bioconductor-emdomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-emdomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-emdomics:2.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-emdomics/2.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-emdomics/2.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-emdomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-emdomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-emdomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-emdomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-emdomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-emdomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-emdomics

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