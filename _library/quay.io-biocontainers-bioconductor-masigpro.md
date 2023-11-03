---
layout: container
name:  "quay.io/biocontainers/bioconductor-masigpro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-masigpro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-masigpro/container.yaml"
updated_at: "2023-11-03 03:17:36.225144"
latest: "1.72.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-masigpro"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-masigpro"
config: {"url": "https://biocontainers.pro/tools/bioconductor-masigpro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-masigpro", "latest": {"1.72.0--r43hdfd78af_0": "sha256:46996cd42dc4a3c25066b9c8c73f66a98c1abb9e934e543a85d72edb5e6a42f0"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:9738ec5a2e05558a63af3e845d2b0acdcfbe863cb06edcb45383a631e1ed2eae", "1.70.0--r42hdfd78af_0": "sha256:4ec81afbc30f3c704f383ac7a7aef7cbc096ef21760eb7a04e97d30390fb2742", "1.72.0--r43hdfd78af_0": "sha256:46996cd42dc4a3c25066b9c8c73f66a98c1abb9e934e543a85d72edb5e6a42f0"}, "docker": "quay.io/biocontainers/bioconductor-masigpro"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-masigpro.
shpc-registry automated BioContainers addition for bioconductor-masigpro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-masigpro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-masigpro:1.72.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-masigpro/1.72.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-masigpro/1.72.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-masigpro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-masigpro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-masigpro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-masigpro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-masigpro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-masigpro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-masigpro

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