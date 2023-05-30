---
layout: container
name:  "quay.io/biocontainers/bioconductor-alpsnmr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-alpsnmr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-alpsnmr/container.yaml"
updated_at: "2023-05-30 02:50:35.445755"
latest: "4.0.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-alpsnmr"
aliases:
 - "pandoc"
versions:
 - "3.4.0--r41hdfd78af_0"
 - "4.0.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-alpsnmr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-alpsnmr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-alpsnmr", "latest": {"4.0.0--r42hdfd78af_0": "sha256:ec297679c09d6b5613cc31b061f52c6ed615faa86ee8a4cd9788e57f6727002c"}, "tags": {"3.4.0--r41hdfd78af_0": "sha256:9f18bd9328cba49d419393af3b9026f436610054a5b9043075ad070dabd13585", "4.0.0--r42hdfd78af_0": "sha256:ec297679c09d6b5613cc31b061f52c6ed615faa86ee8a4cd9788e57f6727002c"}, "docker": "quay.io/biocontainers/bioconductor-alpsnmr", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-alpsnmr.
shpc-registry automated BioContainers addition for bioconductor-alpsnmr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-alpsnmr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-alpsnmr:4.0.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-alpsnmr/4.0.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-alpsnmr/4.0.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-alpsnmr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alpsnmr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alpsnmr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-alpsnmr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-alpsnmr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-alpsnmr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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