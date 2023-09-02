---
layout: container
name:  "quay.io/biocontainers/bioconductor-biseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biseq/container.yaml"
updated_at: "2023-09-02 02:46:22.054281"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biseq"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biseq", "latest": {"1.40.0--r43hdfd78af_0": "sha256:f0f6e91c63157bb14dfdabc897f9be507cf0e4ab027eb6d60cf5c4a7687d0b74"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:a014ec0df02513d84afadfe16f7f3b54a0754d648ce28b3705a38e752c290ac7", "1.38.0--r42hdfd78af_0": "sha256:7e59f3472781e4173a1eeb6fd8a7de21a8ed653ade52aa5f1f86f7c482cc2975", "1.40.0--r43hdfd78af_0": "sha256:f0f6e91c63157bb14dfdabc897f9be507cf0e4ab027eb6d60cf5c4a7687d0b74"}, "docker": "quay.io/biocontainers/bioconductor-biseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biseq.
shpc-registry automated BioContainers addition for bioconductor-biseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biseq:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biseq/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biseq/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biseq

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