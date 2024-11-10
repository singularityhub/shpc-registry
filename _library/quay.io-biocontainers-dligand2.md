---
layout: container
name:  "quay.io/biocontainers/dligand2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dligand2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dligand2/container.yaml"
updated_at: "2024-11-10 03:20:22.491285"
latest: "0.1.0--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/dligand2"
aliases:
 - "dligand2"
versions:
 - "0.1.0--h9f5acd7_2"
 - "0.1.0--h9f5acd7_3"
 - "0.1.0--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for dligand2"
config: {"url": "https://biocontainers.pro/tools/dligand2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dligand2", "latest": {"0.1.0--h4ac6f70_4": "sha256:acd149318a1d1268e5197fb4a016bb54804b3075f048eec7d8f974d5f557b5b1"}, "tags": {"0.1.0--h9f5acd7_2": "sha256:dba2c50c7bc8e1a143921ac2c675c486f9c2b8a6b205058e584cf89dff1dfd28", "0.1.0--h9f5acd7_3": "sha256:32a00862a2c8532521814be12271219169b5afa6bf9b0035a686d954a97c7f51", "0.1.0--h4ac6f70_4": "sha256:acd149318a1d1268e5197fb4a016bb54804b3075f048eec7d8f974d5f557b5b1"}, "docker": "quay.io/biocontainers/dligand2", "aliases": {"dligand2": "/usr/local/bin/dligand2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dligand2.
shpc-registry automated BioContainers addition for dligand2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dligand2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dligand2:0.1.0--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dligand2/0.1.0--h4ac6f70_4
$ module help quay.io/biocontainers/dligand2/0.1.0--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dligand2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dligand2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dligand2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dligand2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dligand2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dligand2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dligand2

```bash
$ singularity exec <container> /usr/local/bin/dligand2
$ podman run --it --rm --entrypoint /usr/local/bin/dligand2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dligand2   -v ${PWD} -w ${PWD} <container> -c " $@"
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