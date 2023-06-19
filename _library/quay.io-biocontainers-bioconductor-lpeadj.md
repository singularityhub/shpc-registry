---
layout: container
name:  "quay.io/biocontainers/bioconductor-lpeadj"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lpeadj/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lpeadj/container.yaml"
updated_at: "2023-06-19 03:21:15.173668"
latest: "1.58.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lpeadj"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lpeadj"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lpeadj", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lpeadj", "latest": {"1.58.0--r42hdfd78af_0": "sha256:a941f3207a4fd3cf5ea668493d3e510e4a3a36c8824ccb7704047a084949cb88"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:efb16b242790f5593493a6f5a857d1b2ed1c5f2284f72dcc372dd6a63a1a7477", "1.58.0--r42hdfd78af_0": "sha256:a941f3207a4fd3cf5ea668493d3e510e4a3a36c8824ccb7704047a084949cb88"}, "docker": "quay.io/biocontainers/bioconductor-lpeadj"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lpeadj.
shpc-registry automated BioContainers addition for bioconductor-lpeadj
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lpeadj
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lpeadj:1.58.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lpeadj/1.58.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lpeadj/1.58.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lpeadj-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpeadj-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpeadj-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lpeadj-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lpeadj-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lpeadj-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lpeadj

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