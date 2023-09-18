---
layout: container
name:  "quay.io/biocontainers/bioconductor-messina"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-messina/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-messina/container.yaml"
updated_at: "2023-09-18 02:34:44.329111"
latest: "1.34.0--r42hf17093f_2"
container_url: "https://biocontainers.pro/tools/bioconductor-messina"

versions:
 - "1.30.0--r41hc247a5b_2"
 - "1.34.0--r42hc247a5b_0"
 - "1.34.0--r42hf17093f_2"
description: "shpc-registry automated BioContainers addition for bioconductor-messina"
config: {"url": "https://biocontainers.pro/tools/bioconductor-messina", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-messina", "latest": {"1.34.0--r42hf17093f_2": "sha256:da11542f1d2109450e57612df52d43c35ebecd15902d71e6b009d89f8dda306e"}, "tags": {"1.30.0--r41hc247a5b_2": "sha256:e1a4f18eb7a8b4e9dd6057f1753b6da2b05bd8318bc83432852696185a2b7848", "1.34.0--r42hc247a5b_0": "sha256:4a0b47131fa83c803b03fd3c652fe81d5c6c961b08564c927d9759ee5541b615", "1.34.0--r42hf17093f_2": "sha256:da11542f1d2109450e57612df52d43c35ebecd15902d71e6b009d89f8dda306e"}, "docker": "quay.io/biocontainers/bioconductor-messina"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-messina.
shpc-registry automated BioContainers addition for bioconductor-messina
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-messina
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-messina:1.34.0--r42hf17093f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-messina/1.34.0--r42hf17093f_2
$ module help quay.io/biocontainers/bioconductor-messina/1.34.0--r42hf17093f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-messina-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-messina-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-messina-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-messina-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-messina-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-messina-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-messina

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