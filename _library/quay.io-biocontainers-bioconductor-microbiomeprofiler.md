---
layout: container
name:  "quay.io/biocontainers/bioconductor-microbiomeprofiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-microbiomeprofiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-microbiomeprofiler/container.yaml"
updated_at: "2023-03-26 02:48:03.836924"
latest: "1.4.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-microbiomeprofiler"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-microbiomeprofiler"
config: {"url": "https://biocontainers.pro/tools/bioconductor-microbiomeprofiler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-microbiomeprofiler", "latest": {"1.4.0--r42hdfd78af_0": "sha256:59cfd98454b8245317dfc8c61ad817259a2c8f75162ea3ac98b2f6a35e6226d9"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:b412a999ced08246bf028d0e5a12fa8290c50b533fd89fb28669456dc65ba7ed", "1.4.0--r42hdfd78af_0": "sha256:59cfd98454b8245317dfc8c61ad817259a2c8f75162ea3ac98b2f6a35e6226d9"}, "docker": "quay.io/biocontainers/bioconductor-microbiomeprofiler"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-microbiomeprofiler.
shpc-registry automated BioContainers addition for bioconductor-microbiomeprofiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-microbiomeprofiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-microbiomeprofiler:1.4.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-microbiomeprofiler/1.4.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-microbiomeprofiler/1.4.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-microbiomeprofiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-microbiomeprofiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-microbiomeprofiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-microbiomeprofiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-microbiomeprofiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-microbiomeprofiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-microbiomeprofiler

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