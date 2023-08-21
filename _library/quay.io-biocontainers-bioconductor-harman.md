---
layout: container
name:  "quay.io/biocontainers/bioconductor-harman"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-harman/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-harman/container.yaml"
updated_at: "2023-08-21 02:46:34.555615"
latest: "1.28.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-harman"

versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.16.0--r40h5f743cb_0"
 - "1.14.0--r36he1b5a44_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-harman"
config: {"url": "https://biocontainers.pro/tools/bioconductor-harman", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-harman", "latest": {"1.28.0--r43hf17093f_0": "sha256:09643af42ab77a1a09b14bb5ab17dc011dba9407f1bbd133eabd514777e79a7e"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:f991fcbfe53b063c3c8c6ed799e43aa5eb6483a15aea768d7c2c2a9e0bab394a", "1.22.0--r41hc247a5b_2": "sha256:e5e641269bf7af27455ee10e9161519ad3f70de228de1ce9e06aca7257a64142", "1.20.0--r41h399db7b_0": "sha256:d193ffb7fa59965e752408632e16ad753cc2b028b2956c7eab67f88238cce09a", "1.18.0--r40h399db7b_1": "sha256:4be3fe0af552386f7319da63411731cf70383cd1722390f336adf56019146b76", "1.16.0--r40h5f743cb_0": "sha256:aa6bc75366be03ecd18d037263c30d59bbc54d3650018a8e7e9fc4d2cc7836f1", "1.14.0--r36he1b5a44_0": "sha256:571cd659d01dddbaad2aeb8abe84bbd3b3db6fcfc42e2e4f9da32ee3f642c9dc", "1.26.0--r42hc247a5b_0": "sha256:8889a1695f6ffcfbdb4fbf200d912419b07e1e6a9add6244ae959947d55cd356", "1.26.0--r42hf17093f_1": "sha256:ab0a1f5eef2e4c4a6677fb639d6ecb822e20777b44352ac15db66d5e16f5cd30", "1.28.0--r43hf17093f_0": "sha256:09643af42ab77a1a09b14bb5ab17dc011dba9407f1bbd133eabd514777e79a7e"}, "docker": "quay.io/biocontainers/bioconductor-harman"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-harman.
shpc-registry automated BioContainers addition for bioconductor-harman
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-harman
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-harman:1.28.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-harman/1.28.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-harman/1.28.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-harman-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harman-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harman-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-harman-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-harman-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-harman-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-harman

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