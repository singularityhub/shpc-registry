---
layout: container
name:  "quay.io/biocontainers/bioconductor-lrcelltypemarkers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lrcelltypemarkers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lrcelltypemarkers/container.yaml"
updated_at: "2026-01-29 04:57:20.904951"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lrcelltypemarkers"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lrcelltypemarkers"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lrcelltypemarkers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lrcelltypemarkers", "latest": {"1.14.0--r44hdfd78af_0": "sha256:e729c6d8c83b2bb088262b0869b96636f44249699143b79b2f6a3928dc87f09d"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:35101b6826f23ec1b256dc6e17e13919fb123b21cab982ec449371f488582707", "1.6.0--r42hdfd78af_0": "sha256:d8554cb695cfe868d350a87637851a34079eb475f84287cd19b9835f4b563536", "1.8.0--r43hdfd78af_0": "sha256:83026ad178a6e3c92c38b1b0c71cbbb68a6830ec58cbdd197818a72fa46571b2", "1.10.0--r43hdfd78af_0": "sha256:f3c91415be5a533ce5d8668764bebd3ee6d101e28a618bae96e07ee14cb81596", "1.14.0--r44hdfd78af_0": "sha256:e729c6d8c83b2bb088262b0869b96636f44249699143b79b2f6a3928dc87f09d"}, "docker": "quay.io/biocontainers/bioconductor-lrcelltypemarkers"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lrcelltypemarkers.
shpc-registry automated BioContainers addition for bioconductor-lrcelltypemarkers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lrcelltypemarkers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lrcelltypemarkers:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lrcelltypemarkers/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lrcelltypemarkers/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lrcelltypemarkers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrcelltypemarkers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrcelltypemarkers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lrcelltypemarkers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lrcelltypemarkers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lrcelltypemarkers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lrcelltypemarkers

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