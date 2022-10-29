---
layout: container
name:  "quay.io/biocontainers/vsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vsearch/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vsearch/container.yaml"
updated_at: "2022-10-29 08:17:35.801589"
latest: "2.9.1--h96824bc_0"
container_url: "https://biocontainers.pro/tools/vsearch"
aliases:
 - "vsearch"
versions:
 - "2.9.1--h96824bc_0"
description: "shpc-registry automated BioContainers addition for vsearch"
config: {"url": "https://biocontainers.pro/tools/vsearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vsearch", "latest": {"2.9.1--h96824bc_0": "sha256:f6737ca83d95ff84710b2e99840b549bcb708022c3f328a919193f31c537b5cd"}, "tags": {"2.9.1--h96824bc_0": "sha256:f6737ca83d95ff84710b2e99840b549bcb708022c3f328a919193f31c537b5cd"}, "docker": "quay.io/biocontainers/vsearch", "aliases": {"vsearch": "/usr/local/bin/vsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vsearch.
shpc-registry automated BioContainers addition for vsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vsearch:2.9.1--h96824bc_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vsearch/2.9.1--h96824bc_0
$ module help quay.io/biocontainers/vsearch/2.9.1--h96824bc_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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