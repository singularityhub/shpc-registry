---
layout: container
name:  "quay.io/biocontainers/gff3toembl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gff3toembl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gff3toembl/container.yaml"
updated_at: "2022-10-27 00:58:37.108950"
latest: "1.1.4--pyh864c0ab_2"
container_url: "https://biocontainers.pro/tools/gff3toembl"
aliases:
 - "gff3_to_embl"
versions:
 - "1.1.4--pyh864c0ab_2"
description: "shpc-registry automated BioContainers addition for gff3toembl"
config: {"url": "https://biocontainers.pro/tools/gff3toembl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gff3toembl", "latest": {"1.1.4--pyh864c0ab_2": "sha256:b5bac637f97f92531ef323a051406b71664338bb51fd5871307505dc1a9f4244"}, "tags": {"1.1.4--pyh864c0ab_2": "sha256:b5bac637f97f92531ef323a051406b71664338bb51fd5871307505dc1a9f4244"}, "docker": "quay.io/biocontainers/gff3toembl", "aliases": {"gff3_to_embl": "/usr/local/bin/gff3_to_embl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gff3toembl.
shpc-registry automated BioContainers addition for gff3toembl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gff3toembl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gff3toembl:1.1.4--pyh864c0ab_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gff3toembl/1.1.4--pyh864c0ab_2
$ module help quay.io/biocontainers/gff3toembl/1.1.4--pyh864c0ab_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gff3toembl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gff3toembl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gff3toembl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gff3toembl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gff3toembl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gff3toembl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gff3_to_embl

```bash
$ singularity exec <container> /usr/local/bin/gff3_to_embl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3_to_embl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3_to_embl   -v ${PWD} -w ${PWD} <container> -c " $@"
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