---
layout: container
name:  "quay.io/biocontainers/bioconductor-procoil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-procoil/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-procoil/container.yaml"
updated_at: "2022-10-27 00:22:04.905186"
latest: "2.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-procoil"

versions:
 - "2.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-procoil"
config: {"url": "https://biocontainers.pro/tools/bioconductor-procoil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-procoil", "latest": {"2.8.0--r351_0": "sha256:c91e72c2c60c5dc76e41d7571da6fd0a5e7cc57dae3534f8ba5702bd23880379"}, "tags": {"2.8.0--r351_0": "sha256:c91e72c2c60c5dc76e41d7571da6fd0a5e7cc57dae3534f8ba5702bd23880379"}, "docker": "quay.io/biocontainers/bioconductor-procoil"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-procoil.
shpc-registry automated BioContainers addition for bioconductor-procoil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-procoil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-procoil:2.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-procoil/2.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-procoil/2.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-procoil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-procoil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-procoil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-procoil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-procoil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-procoil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-procoil

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