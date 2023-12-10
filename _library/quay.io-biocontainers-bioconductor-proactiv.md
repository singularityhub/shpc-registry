---
layout: container
name:  "quay.io/biocontainers/bioconductor-proactiv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-proactiv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-proactiv/container.yaml"
updated_at: "2023-12-10 02:40:49.154101"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-proactiv"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-proactiv"
config: {"url": "https://biocontainers.pro/tools/bioconductor-proactiv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-proactiv", "latest": {"1.10.0--r43hdfd78af_0": "sha256:850c3fab27e429e50cda659af10021856e0a22acd21f221aa3b4f2df114fc581"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:2ad73e39127cda2f8b81079500f3484986edece8ff8cc883feff6125ae7e82df", "1.8.0--r42hdfd78af_0": "sha256:aa570d97ceab57d1159399ce8404c5280f8628736ee7da9647ee7d0601fd1599", "1.10.0--r43hdfd78af_0": "sha256:850c3fab27e429e50cda659af10021856e0a22acd21f221aa3b4f2df114fc581"}, "docker": "quay.io/biocontainers/bioconductor-proactiv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-proactiv.
shpc-registry automated BioContainers addition for bioconductor-proactiv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-proactiv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-proactiv:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-proactiv/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-proactiv/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-proactiv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proactiv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proactiv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-proactiv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-proactiv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-proactiv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-proactiv

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