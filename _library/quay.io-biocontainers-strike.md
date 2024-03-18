---
layout: container
name:  "quay.io/biocontainers/strike"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strike/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strike/container.yaml"
updated_at: "2024-03-18 02:29:10.883948"
latest: "1.2--h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/strike"
aliases:
 - "strike"
versions:
 - "1.2--h9f5acd7_3"
 - "1.2--h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for strike"
config: {"url": "https://biocontainers.pro/tools/strike", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strike", "latest": {"1.2--h4ac6f70_5": "sha256:d708f6e5115c786cd0fddbd815e2a15cd8529caa9edbdce73163a31fec45ae82"}, "tags": {"1.2--h9f5acd7_3": "sha256:b42019e9f07ce957f57bc89a2942682bc50332d0f1bf7277c0ec1ee4d16e8ec1", "1.2--h4ac6f70_5": "sha256:d708f6e5115c786cd0fddbd815e2a15cd8529caa9edbdce73163a31fec45ae82"}, "docker": "quay.io/biocontainers/strike", "aliases": {"strike": "/usr/local/bin/strike"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strike.
shpc-registry automated BioContainers addition for strike
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strike
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strike:1.2--h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strike/1.2--h4ac6f70_5
$ module help quay.io/biocontainers/strike/1.2--h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strike-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strike-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strike-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strike-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strike-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strike-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### strike

```bash
$ singularity exec <container> /usr/local/bin/strike
$ podman run --it --rm --entrypoint /usr/local/bin/strike   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strike   -v ${PWD} -w ${PWD} <container> -c " $@"
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