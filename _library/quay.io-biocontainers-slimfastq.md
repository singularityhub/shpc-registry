---
layout: container
name:  "quay.io/biocontainers/slimfastq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slimfastq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slimfastq/container.yaml"
updated_at: "2023-03-23 03:41:32.153807"
latest: "2.04--h87f3376_2"
container_url: "https://biocontainers.pro/tools/slimfastq"
aliases:
 - "slimfastq"
 - "slimfastq.multi"
versions:
 - "2.04--h87f3376_2"
description: "shpc-registry automated BioContainers addition for slimfastq"
config: {"url": "https://biocontainers.pro/tools/slimfastq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slimfastq", "latest": {"2.04--h87f3376_2": "sha256:6948357675511a0e48eb20262b37bb3a230843833734de09f183c85563302aef"}, "tags": {"2.04--h87f3376_2": "sha256:6948357675511a0e48eb20262b37bb3a230843833734de09f183c85563302aef"}, "docker": "quay.io/biocontainers/slimfastq", "aliases": {"slimfastq": "/usr/local/bin/slimfastq", "slimfastq.multi": "/usr/local/bin/slimfastq.multi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slimfastq.
shpc-registry automated BioContainers addition for slimfastq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slimfastq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slimfastq:2.04--h87f3376_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slimfastq/2.04--h87f3376_2
$ module help quay.io/biocontainers/slimfastq/2.04--h87f3376_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slimfastq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slimfastq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slimfastq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slimfastq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slimfastq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slimfastq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### slimfastq

```bash
$ singularity exec <container> /usr/local/bin/slimfastq
$ podman run --it --rm --entrypoint /usr/local/bin/slimfastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slimfastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slimfastq.multi

```bash
$ singularity exec <container> /usr/local/bin/slimfastq.multi
$ podman run --it --rm --entrypoint /usr/local/bin/slimfastq.multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slimfastq.multi   -v ${PWD} -w ${PWD} <container> -c " $@"
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