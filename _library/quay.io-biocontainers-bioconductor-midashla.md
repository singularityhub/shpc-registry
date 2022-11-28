---
layout: container
name:  "quay.io/biocontainers/bioconductor-midashla"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-midashla/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-midashla/container.yaml"
updated_at: "2022-11-28 00:16:51.019206"
latest: "1.2.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-midashla"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-midashla"
config: {"url": "https://biocontainers.pro/tools/bioconductor-midashla", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-midashla", "latest": {"1.2.0--r41hdfd78af_0": "sha256:bb09bba92e2f7ff0d0f569626d6b9f4144c9fa26efa1e7a5216385606e61566a"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:bb09bba92e2f7ff0d0f569626d6b9f4144c9fa26efa1e7a5216385606e61566a"}, "docker": "quay.io/biocontainers/bioconductor-midashla", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-midashla.
shpc-registry automated BioContainers addition for bioconductor-midashla
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-midashla
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-midashla:1.2.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-midashla/1.2.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-midashla/1.2.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-midashla-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-midashla-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-midashla-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-midashla-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-midashla-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-midashla-inspect-deffile:

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