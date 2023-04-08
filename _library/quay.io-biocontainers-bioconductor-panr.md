---
layout: container
name:  "quay.io/biocontainers/bioconductor-panr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-panr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-panr/container.yaml"
updated_at: "2023-04-08 02:58:29.475318"
latest: "1.44.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-panr"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-panr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-panr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-panr", "latest": {"1.44.0--r42hdfd78af_0": "sha256:fce55ca657b6bad2f0fa4b7c40aea7cdb5ccd190e6e6dc378a7e5cac44bcb847"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:d8aa5b03e8203f1cb845a6b4c7e5c2a886231d4957333586d56ce60c391fca2a", "1.44.0--r42hdfd78af_0": "sha256:fce55ca657b6bad2f0fa4b7c40aea7cdb5ccd190e6e6dc378a7e5cac44bcb847"}, "docker": "quay.io/biocontainers/bioconductor-panr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-panr.
shpc-registry automated BioContainers addition for bioconductor-panr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-panr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-panr:1.44.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-panr/1.44.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-panr/1.44.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-panr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-panr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-panr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-panr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-panr

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