---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvgsadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvgsadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvgsadata/container.yaml"
updated_at: "2024-07-16 02:59:31.608949"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvgsadata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvgsadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvgsadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvgsadata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:b7edc230c676cabc80dea2ee3a6631a337f487f1a73c2c6d552573d06f13edb5"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:fd0f302278ff545554699523bca6abaf77724fa9db52a3f813452ac7083b7644", "1.34.0--r42hdfd78af_0": "sha256:b77d0da7084bf4527a5a6ef17de592a4c2e9c84f7f282cc3fb6882bced285dd2", "1.36.0--r43hdfd78af_0": "sha256:1fe28f815e4ae6cf2e1fba0a48719a25b57d779d8272781bff5cc3900dfa9fe3", "1.38.0--r43hdfd78af_0": "sha256:b7edc230c676cabc80dea2ee3a6631a337f487f1a73c2c6d552573d06f13edb5"}, "docker": "quay.io/biocontainers/bioconductor-cnvgsadata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvgsadata.
shpc-registry automated BioContainers addition for bioconductor-cnvgsadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgsadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgsadata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvgsadata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnvgsadata/1.38.0--r43hdfd78af_0
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



#### bioconductor-cnvgsadata

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