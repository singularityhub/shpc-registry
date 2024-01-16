---
layout: container
name:  "quay.io/biocontainers/bioconductor-sigsquared"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sigsquared/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sigsquared/container.yaml"
updated_at: "2024-01-16 02:42:01.630428"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sigsquared"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sigsquared"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sigsquared", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sigsquared", "latest": {"1.34.0--r43hdfd78af_0": "sha256:ca73281e91107189d8e7bfeac542bf9d5fa297177a8af3f97d0f5866a7c97415"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:fd1768860bd92854d5abca40a8d4bc1ca6ec16e05a891d0725efd993b012c8fa", "1.30.0--r42hdfd78af_0": "sha256:d6bbeae595e0666d4ae3451509ea30b1ab06607226eb2ef7a4cf8954cd895c75", "1.32.0--r43hdfd78af_0": "sha256:554ab90aa6dcdb1a607731f60042b894a66f46a2993c11fb805926bafad20c4b", "1.34.0--r43hdfd78af_0": "sha256:ca73281e91107189d8e7bfeac542bf9d5fa297177a8af3f97d0f5866a7c97415"}, "docker": "quay.io/biocontainers/bioconductor-sigsquared"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sigsquared.
shpc-registry automated BioContainers addition for bioconductor-sigsquared
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sigsquared
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sigsquared:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sigsquared/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sigsquared/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sigsquared-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigsquared-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigsquared-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sigsquared-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sigsquared-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sigsquared-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sigsquared

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