---
layout: container
name:  "quay.io/biocontainers/bioconductor-zlibbioc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-zlibbioc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-zlibbioc/container.yaml"
updated_at: "2023-02-12 02:55:43.489309"
latest: "1.44.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-zlibbioc"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-zlibbioc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-zlibbioc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-zlibbioc", "latest": {"1.44.0--r42hc0cfd56_0": "sha256:d58082e0fd0249bbabc21cd16f2fa9d147052d6b830a8c7220c4ba37a32c7499"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:c799784bee1f74f9b18e645f0b2d5f308a1379d5387a4fd6c49816b40d9f93f6", "1.44.0--r42hc0cfd56_0": "sha256:d58082e0fd0249bbabc21cd16f2fa9d147052d6b830a8c7220c4ba37a32c7499"}, "docker": "quay.io/biocontainers/bioconductor-zlibbioc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-zlibbioc.
shpc-registry automated BioContainers addition for bioconductor-zlibbioc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-zlibbioc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-zlibbioc:1.44.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-zlibbioc/1.44.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-zlibbioc/1.44.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-zlibbioc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zlibbioc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zlibbioc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-zlibbioc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-zlibbioc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-zlibbioc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-zlibbioc

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