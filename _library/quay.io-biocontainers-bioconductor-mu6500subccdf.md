---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu6500subccdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu6500subccdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu6500subccdf/container.yaml"
updated_at: "2026-01-06 03:57:39.972622"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mu6500subccdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mu6500subccdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu6500subccdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu6500subccdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:6a6edd920d826c2e01e7a647729296b7d97a7c1637a86234043a94dce96d2a18"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:4b12f4eb2f1f13bc3c40c12469c6869f1fba87cee6b83c40b108929c4740031a", "2.18.0--r42hdfd78af_10": "sha256:eb280c7d24a2a4f8735985ee01dc1f26a88f49d81b291cc182d14e82818bf2ed", "2.18.0--r43hdfd78af_11": "sha256:747a07f9e25a82f6748dc33a5f7584d4d272786475d000193ed7eacb0b42d107", "2.18.0--r43hdfd78af_12": "sha256:1bd899a3dd60700e8a1fc1025c0a70937ef1c21a154eb00aca716a4e7b8e7d69", "2.18.0--r44hdfd78af_13": "sha256:6a6edd920d826c2e01e7a647729296b7d97a7c1637a86234043a94dce96d2a18"}, "docker": "quay.io/biocontainers/bioconductor-mu6500subccdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu6500subccdf.
shpc-registry automated BioContainers addition for bioconductor-mu6500subccdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu6500subccdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu6500subccdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu6500subccdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mu6500subccdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu6500subccdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu6500subccdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu6500subccdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu6500subccdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu6500subccdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu6500subccdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu6500subccdf

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