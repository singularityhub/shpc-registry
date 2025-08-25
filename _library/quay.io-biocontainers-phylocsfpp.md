---
layout: container
name:  "quay.io/biocontainers/phylocsfpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylocsfpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylocsfpp/container.yaml"
updated_at: "2025-08-25 03:21:35.135793"
latest: "1.2.0_9643238d--heaafb18_7"
container_url: "https://biocontainers.pro/tools/phylocsfpp"
aliases:
 - "phylocsf++"
versions:
 - "1.2.0_9643238d--h54ed327_5"
 - "1.2.0_9643238d--ha666654_6"
 - "1.2.0_9643238d--heaafb18_7"
description: "shpc-registry automated BioContainers addition for phylocsfpp"
config: {"url": "https://biocontainers.pro/tools/phylocsfpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylocsfpp", "latest": {"1.2.0_9643238d--heaafb18_7": "sha256:99494dd80a6d87ee97d12c70281f88d49abd739da181ba78ecf0b0cc87ae79c4"}, "tags": {"1.2.0_9643238d--h54ed327_5": "sha256:487185b710260ed70141d67f804375985114a58e66b93316df6015b5f8e2db45", "1.2.0_9643238d--ha666654_6": "sha256:41ab92c49619218fa1f148d33fcbffd825e1863018225bc25658979765d83bc2", "1.2.0_9643238d--heaafb18_7": "sha256:99494dd80a6d87ee97d12c70281f88d49abd739da181ba78ecf0b0cc87ae79c4"}, "docker": "quay.io/biocontainers/phylocsfpp", "aliases": {"phylocsf++": "/usr/local/bin/phylocsf++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylocsfpp.
shpc-registry automated BioContainers addition for phylocsfpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylocsfpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylocsfpp:1.2.0_9643238d--heaafb18_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylocsfpp/1.2.0_9643238d--heaafb18_7
$ module help quay.io/biocontainers/phylocsfpp/1.2.0_9643238d--heaafb18_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylocsfpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylocsfpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylocsfpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylocsfpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylocsfpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylocsfpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### phylocsf++

```bash
$ singularity exec <container> /usr/local/bin/phylocsf++
$ podman run --it --rm --entrypoint /usr/local/bin/phylocsf++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phylocsf++   -v ${PWD} -w ${PWD} <container> -c " $@"
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