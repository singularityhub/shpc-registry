---
layout: container
name:  "quay.io/biocontainers/bioconductor-drugvsdisease"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drugvsdisease/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drugvsdisease/container.yaml"
updated_at: "2024-02-22 02:24:53.127670"
latest: "2.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-drugvsdisease"

versions:
 - "2.36.0--r41hdfd78af_0"
 - "2.40.0--r42hdfd78af_0"
 - "2.42.0--r43hdfd78af_0"
 - "2.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-drugvsdisease"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drugvsdisease", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drugvsdisease", "latest": {"2.44.0--r43hdfd78af_0": "sha256:ad0ea08a3ac8999cb43cc5487856c9b4cd8d0aeeb1dd9b4be8a3bba0fdf7538d"}, "tags": {"2.36.0--r41hdfd78af_0": "sha256:e2f2d6492d52cab14103a8d1bba4c20b8f94f43629dea04593f6e36a52fed91d", "2.40.0--r42hdfd78af_0": "sha256:873418becae84e7df68da39554c5d1ec68294731a269d93691e01d5277de1d99", "2.42.0--r43hdfd78af_0": "sha256:88e7fb3dd551358025bbdd2700b48245e3f323ef20be70b6a11efa7276c0222f", "2.44.0--r43hdfd78af_0": "sha256:ad0ea08a3ac8999cb43cc5487856c9b4cd8d0aeeb1dd9b4be8a3bba0fdf7538d"}, "docker": "quay.io/biocontainers/bioconductor-drugvsdisease"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drugvsdisease.
shpc-registry automated BioContainers addition for bioconductor-drugvsdisease
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drugvsdisease
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drugvsdisease:2.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drugvsdisease/2.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-drugvsdisease/2.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drugvsdisease-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drugvsdisease-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drugvsdisease-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drugvsdisease-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drugvsdisease-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drugvsdisease-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-drugvsdisease

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