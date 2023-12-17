---
layout: container
name:  "quay.io/biocontainers/bioconductor-timeomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-timeomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-timeomics/container.yaml"
updated_at: "2023-12-17 03:05:58.393749"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-timeomics"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-timeomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-timeomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-timeomics", "latest": {"1.14.0--r43hdfd78af_0": "sha256:63387ff9347f4262bfc112ccc9a45d89f37ae3bd202c805c10a057e69ad56114"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:6eddbef4d68b6b52a33e9fcfb83eeff49f53a5cc1ea70bcd86c238807f767290", "1.10.0--r42hdfd78af_0": "sha256:07bdbe60ed7a165faae5cfcdbdebf7f3944bdf76c32d0b6c6cfc7e943239065e", "1.12.0--r43hdfd78af_0": "sha256:7e7bb43eefdd4b290f926a66a265d5cf8baf31f113fb3ec0b43eb2e7da9071ba", "1.14.0--r43hdfd78af_0": "sha256:63387ff9347f4262bfc112ccc9a45d89f37ae3bd202c805c10a057e69ad56114"}, "docker": "quay.io/biocontainers/bioconductor-timeomics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-timeomics.
shpc-registry automated BioContainers addition for bioconductor-timeomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-timeomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-timeomics:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-timeomics/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-timeomics/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-timeomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timeomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timeomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-timeomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-timeomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-timeomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-timeomics

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