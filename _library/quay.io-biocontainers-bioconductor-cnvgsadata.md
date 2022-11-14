---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvgsadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvgsadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvgsadata/container.yaml"
updated_at: "2022-11-14 00:57:52.189441"
latest: "1.30.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvgsadata"
aliases:
 - ".bioconductor-cnvgsadata-post-link.sh"
 - ".bioconductor-cnvgsadata-pre-unlink.sh"
versions:
 - "1.30.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvgsadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvgsadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvgsadata", "latest": {"1.30.0--r41hdfd78af_1": "sha256:fd0f302278ff545554699523bca6abaf77724fa9db52a3f813452ac7083b7644"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:fd0f302278ff545554699523bca6abaf77724fa9db52a3f813452ac7083b7644"}, "docker": "quay.io/biocontainers/bioconductor-cnvgsadata", "aliases": {".bioconductor-cnvgsadata-post-link.sh": "/usr/local/bin/.bioconductor-cnvgsadata-post-link.sh", ".bioconductor-cnvgsadata-pre-unlink.sh": "/usr/local/bin/.bioconductor-cnvgsadata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvgsadata.
shpc-registry automated BioContainers addition for bioconductor-cnvgsadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgsadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgsadata:1.30.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvgsadata/1.30.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-cnvgsadata/1.30.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnvgsadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvgsadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvgsadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnvgsadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnvgsadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnvgsadata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-cnvgsadata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-cnvgsadata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-cnvgsadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-cnvgsadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-cnvgsadata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-cnvgsadata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-cnvgsadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-cnvgsadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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