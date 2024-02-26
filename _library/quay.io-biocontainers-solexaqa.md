---
layout: container
name:  "quay.io/biocontainers/solexaqa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/solexaqa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/solexaqa/container.yaml"
updated_at: "2024-02-26 03:57:11.618458"
latest: "3.1.7.1--h69fb01c_5"
container_url: "https://biocontainers.pro/tools/solexaqa"
aliases:
 - "SolexaQA++"
versions:
 - "3.1.7.1--h36ad0af_3"
 - "3.1.7.1--h69fb01c_5"
description: "shpc-registry automated BioContainers addition for solexaqa"
config: {"url": "https://biocontainers.pro/tools/solexaqa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for solexaqa", "latest": {"3.1.7.1--h69fb01c_5": "sha256:305d7af6bee54aba343ebceef101981ef343bd53112d4f64f83e964d3c51a5f0"}, "tags": {"3.1.7.1--h36ad0af_3": "sha256:88488a2fb8fec3bff0bfa2570abb52c303a849d63e56863ba2f6c1ad05a08c8c", "3.1.7.1--h69fb01c_5": "sha256:305d7af6bee54aba343ebceef101981ef343bd53112d4f64f83e964d3c51a5f0"}, "docker": "quay.io/biocontainers/solexaqa", "aliases": {"SolexaQA++": "/usr/local/bin/SolexaQA++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/solexaqa.
shpc-registry automated BioContainers addition for solexaqa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/solexaqa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/solexaqa:3.1.7.1--h69fb01c_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/solexaqa/3.1.7.1--h69fb01c_5
$ module help quay.io/biocontainers/solexaqa/3.1.7.1--h69fb01c_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### solexaqa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### solexaqa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### solexaqa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### solexaqa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### solexaqa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### solexaqa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SolexaQA++

```bash
$ singularity exec <container> /usr/local/bin/SolexaQA++
$ podman run --it --rm --entrypoint /usr/local/bin/SolexaQA++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SolexaQA++   -v ${PWD} -w ${PWD} <container> -c " $@"
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