---
layout: container
name:  "quay.io/biocontainers/bioconductor-hpastainr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hpastainr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hpastainr/container.yaml"
updated_at: "2024-07-15 03:25:07.121020"
latest: "1.9.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hpastainr"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.9.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hpastainr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hpastainr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hpastainr", "latest": {"1.9.0--r43hdfd78af_0": "sha256:c7aabcb6bfecc312bc4212789321d37a3fb384322cfd196b5b020a6a5267aa45"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:6c08152b5125ab93259a15fca229c245e48ebbf0b0bd75213986e8675c702bec", "1.8.0--r42hdfd78af_0": "sha256:965a0ef73f354cf0a5926cbf9a3fd648b0c133960efdad7d67707447e9e641e4", "1.9.0--r43hdfd78af_0": "sha256:c7aabcb6bfecc312bc4212789321d37a3fb384322cfd196b5b020a6a5267aa45"}, "docker": "quay.io/biocontainers/bioconductor-hpastainr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hpastainr.
shpc-registry automated BioContainers addition for bioconductor-hpastainr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hpastainr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hpastainr:1.9.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hpastainr/1.9.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hpastainr/1.9.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hpastainr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpastainr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hpastainr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hpastainr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hpastainr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hpastainr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hpastainr

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