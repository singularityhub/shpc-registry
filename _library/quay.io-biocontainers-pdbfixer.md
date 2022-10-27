---
layout: container
name:  "quay.io/biocontainers/pdbfixer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pdbfixer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pdbfixer/container.yaml"
updated_at: "2022-10-27 00:29:10.956507"
latest: "1.8.1"
container_url: "https://biocontainers.pro/tools/pdbfixer"
aliases:
 - ".ocl-icd-system-post-link.sh"
 - ".ocl-icd-system-pre-unlink.sh"
 - "pdbfixer"
versions:
 - "1.8.1"
description: "shpc-registry automated BioContainers addition for pdbfixer"
config: {"url": "https://biocontainers.pro/tools/pdbfixer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pdbfixer", "latest": {"1.8.1": "sha256:2ef51fa5f45cf68b64b3a5eb9a1e03ba70b4f9d3972c31ecb755cf55c5c74ba1"}, "tags": {"1.8.1": "sha256:2ef51fa5f45cf68b64b3a5eb9a1e03ba70b4f9d3972c31ecb755cf55c5c74ba1"}, "docker": "quay.io/biocontainers/pdbfixer", "aliases": {".ocl-icd-system-post-link.sh": "/usr/local/bin/.ocl-icd-system-post-link.sh", ".ocl-icd-system-pre-unlink.sh": "/usr/local/bin/.ocl-icd-system-pre-unlink.sh", "pdbfixer": "/usr/local/bin/pdbfixer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pdbfixer.
shpc-registry automated BioContainers addition for pdbfixer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pdbfixer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pdbfixer:1.8.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pdbfixer/1.8.1
$ module help quay.io/biocontainers/pdbfixer/1.8.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pdbfixer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pdbfixer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pdbfixer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pdbfixer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pdbfixer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pdbfixer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .ocl-icd-system-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.ocl-icd-system-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.ocl-icd-system-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.ocl-icd-system-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .ocl-icd-system-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.ocl-icd-system-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.ocl-icd-system-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.ocl-icd-system-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdbfixer

```bash
$ singularity exec <container> /usr/local/bin/pdbfixer
$ podman run --it --rm --entrypoint /usr/local/bin/pdbfixer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdbfixer   -v ${PWD} -w ${PWD} <container> -c " $@"
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