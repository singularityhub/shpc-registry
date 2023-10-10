---
layout: container
name:  "quay.io/biocontainers/bioconductor-crisprseek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-crisprseek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-crisprseek/container.yaml"
updated_at: "2023-10-10 02:47:38.051535"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-crisprseek"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-crisprseek"
config: {"url": "https://biocontainers.pro/tools/bioconductor-crisprseek", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-crisprseek", "latest": {"1.40.0--r43hdfd78af_0": "sha256:73258a522c223488230df00b2dff472e6c7d29fdd864878888e6aec16cbc2d59"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:f998f6ef4d2adfbe293367541e68989908da0c3315329cf1a2fdc4d4896b78c9", "1.38.0--r42hdfd78af_0": "sha256:bda7f4109fba5c9014107f680ff6998c4bededd5c2090a7bc6bc378646e0e2ef", "1.40.0--r43hdfd78af_0": "sha256:73258a522c223488230df00b2dff472e6c7d29fdd864878888e6aec16cbc2d59"}, "docker": "quay.io/biocontainers/bioconductor-crisprseek"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-crisprseek.
shpc-registry automated BioContainers addition for bioconductor-crisprseek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-crisprseek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-crisprseek:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-crisprseek/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-crisprseek/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-crisprseek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crisprseek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crisprseek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-crisprseek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-crisprseek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-crisprseek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-crisprseek

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