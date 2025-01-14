---
layout: container
name:  "quay.io/biocontainers/bioconductor-frenchfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-frenchfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-frenchfish/container.yaml"
updated_at: "2025-01-14 03:20:46.361198"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-frenchfish"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-frenchfish"
config: {"url": "https://biocontainers.pro/tools/bioconductor-frenchfish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-frenchfish", "latest": {"1.18.0--r44hdfd78af_0": "sha256:8bd8b5a7ee873d4f913dede606069830f185bf35e194ae6d1f8c1964885bff53"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:cb888657c3371e8a23a076c5297a9fcf39f6d0995e8657f021dd3a445c4557f3", "1.10.0--r42hdfd78af_0": "sha256:96c3073f111619f6df0bde6c637308e5ac12ed7d172d476b9adf02381cd97f07", "1.12.0--r43hdfd78af_0": "sha256:af1bc24fb99115d8b9df3299bc8bafae67ab6a073be1bb4b156008ca811fe480", "1.14.0--r43hdfd78af_0": "sha256:c3ce76b3d07e6e965897e0f4cd8fd9d17b766bf1004c02953fb4f88de0607374", "1.18.0--r44hdfd78af_0": "sha256:8bd8b5a7ee873d4f913dede606069830f185bf35e194ae6d1f8c1964885bff53"}, "docker": "quay.io/biocontainers/bioconductor-frenchfish"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-frenchfish.
shpc-registry automated BioContainers addition for bioconductor-frenchfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-frenchfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-frenchfish:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-frenchfish/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-frenchfish/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-frenchfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frenchfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frenchfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-frenchfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-frenchfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-frenchfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-frenchfish

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