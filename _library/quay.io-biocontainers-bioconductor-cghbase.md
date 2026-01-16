---
layout: container
name:  "quay.io/biocontainers/bioconductor-cghbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cghbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cghbase/container.yaml"
updated_at: "2026-01-16 04:13:16.698618"
latest: "1.66.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cghbase"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.66.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cghbase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cghbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cghbase", "latest": {"1.66.0--r44hdfd78af_0": "sha256:70812717f52c9e3537d8ae08ab0df05bda4e56b23e81655bd63b47b0d50ba5c5"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:f8f498d1c4cfa56487091cde06abf6795e36345744307bf1ca72064f59ffa121", "1.58.0--r42hdfd78af_0": "sha256:68d164c9e74d19640a087ec68954b2c972aac74fc172fd36ceb98a789d37790f", "1.60.0--r43hdfd78af_0": "sha256:c343ad4d18532c202ece7bb7633b2f925749174aa101bec893ecfb8ec48daa3d", "1.62.0--r43hdfd78af_0": "sha256:7ba093935e958d891532d032c4525e8e4e9e93235e367fd380e48f87d1da4ef2", "1.66.0--r44hdfd78af_0": "sha256:70812717f52c9e3537d8ae08ab0df05bda4e56b23e81655bd63b47b0d50ba5c5"}, "docker": "quay.io/biocontainers/bioconductor-cghbase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cghbase.
shpc-registry automated BioContainers addition for bioconductor-cghbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cghbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cghbase:1.66.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cghbase/1.66.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cghbase/1.66.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cghbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cghbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cghbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cghbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cghbase

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