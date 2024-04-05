---
layout: container
name:  "quay.io/biocontainers/bioconductor-dino"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dino/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dino/container.yaml"
updated_at: "2024-04-05 02:25:19.152942"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dino"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dino"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dino", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dino", "latest": {"1.8.0--r43hdfd78af_0": "sha256:e86fc4931d4ce7a72a0e1f179652344cbceae8551d65b95dca5d5f6e9b93b884"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:7a5c2e4bcb55a177301692a9381fe5779cce64f04f2b70dd6a0def341b5c443f", "1.4.0--r42hdfd78af_0": "sha256:99d8e4a25c15b418dfe302216928c730917a397e176f068e69fa93c1bdf6e236", "1.6.0--r43hdfd78af_0": "sha256:82217e3f297aad2240d880d7e66827cf725a292e570146739f7470a783092dfd", "1.8.0--r43hdfd78af_0": "sha256:e86fc4931d4ce7a72a0e1f179652344cbceae8551d65b95dca5d5f6e9b93b884"}, "docker": "quay.io/biocontainers/bioconductor-dino"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dino.
shpc-registry automated BioContainers addition for bioconductor-dino
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dino
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dino:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dino/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dino/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dino-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dino-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dino-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dino-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dino-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dino-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dino

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