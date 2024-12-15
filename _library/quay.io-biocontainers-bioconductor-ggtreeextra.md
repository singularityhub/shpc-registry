---
layout: container
name:  "quay.io/biocontainers/bioconductor-ggtreeextra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ggtreeextra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ggtreeextra/container.yaml"
updated_at: "2024-12-15 04:07:35.902596"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ggtreeextra"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ggtreeextra"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ggtreeextra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ggtreeextra", "latest": {"1.12.0--r43hdfd78af_0": "sha256:5a1016941443e389a3fe73db328f654df348cf6b06f7393c27c27dfe140b9f0c"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:94584baab40dd22e1c17a57ad91273905b8589044c17127f392415e9a8d85370", "1.8.0--r42hdfd78af_0": "sha256:25d0f62d26858e1565a630f40d754f9738556f9e901e7112fe67d46a0447a361", "1.10.0--r43hdfd78af_0": "sha256:68a87efbac8ae6e68562275ed275984fea080035d8d2d02268aaeab6c12ee7a4", "1.12.0--r43hdfd78af_0": "sha256:5a1016941443e389a3fe73db328f654df348cf6b06f7393c27c27dfe140b9f0c"}, "docker": "quay.io/biocontainers/bioconductor-ggtreeextra"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ggtreeextra.
shpc-registry automated BioContainers addition for bioconductor-ggtreeextra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ggtreeextra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ggtreeextra:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ggtreeextra/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ggtreeextra/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ggtreeextra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggtreeextra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggtreeextra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ggtreeextra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ggtreeextra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ggtreeextra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ggtreeextra

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