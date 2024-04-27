---
layout: container
name:  "quay.io/biocontainers/bioconductor-perfect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-perfect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-perfect/container.yaml"
updated_at: "2024-04-27 02:46:02.540552"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-perfect"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-perfect"
config: {"url": "https://biocontainers.pro/tools/bioconductor-perfect", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-perfect", "latest": {"1.14.0--r43hdfd78af_0": "sha256:80bc69662bcc89fb100ed698905e6947cbf2a1db7a7a0d5f85c869d409087652"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:026931eaa4e12388fabbd42f705aebec2ad859957291a42d17fbd9a92cf88e71", "1.12.0--r42hdfd78af_0": "sha256:e1c2e62b30151fac17803a3373530c2376f898da6b801e6c286bd96c5c64c699", "1.14.0--r43hdfd78af_0": "sha256:80bc69662bcc89fb100ed698905e6947cbf2a1db7a7a0d5f85c869d409087652"}, "docker": "quay.io/biocontainers/bioconductor-perfect"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-perfect.
shpc-registry automated BioContainers addition for bioconductor-perfect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-perfect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-perfect:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-perfect/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-perfect/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-perfect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-perfect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-perfect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-perfect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-perfect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-perfect-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-perfect

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