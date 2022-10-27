---
layout: container
name:  "quay.io/biocontainers/r-tigger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-tigger/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-tigger/container.yaml"
updated_at: "2022-10-27 00:54:14.231927"
latest: "0.4.0--r40h6115d3f_2"
container_url: "https://biocontainers.pro/tools/r-tigger"

versions:
 - "0.4.0--r40h6115d3f_2"
description: "shpc-registry automated BioContainers addition for r-tigger"
config: {"url": "https://biocontainers.pro/tools/r-tigger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-tigger", "latest": {"0.4.0--r40h6115d3f_2": "sha256:86b0a65ddbca4fb4ad173e9ffe5360e3921fad06b29bc5bcb8ba185e065adcdd"}, "tags": {"0.4.0--r40h6115d3f_2": "sha256:86b0a65ddbca4fb4ad173e9ffe5360e3921fad06b29bc5bcb8ba185e065adcdd"}, "docker": "quay.io/biocontainers/r-tigger"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-tigger.
shpc-registry automated BioContainers addition for r-tigger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-tigger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-tigger:0.4.0--r40h6115d3f_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-tigger/0.4.0--r40h6115d3f_2
$ module help quay.io/biocontainers/r-tigger/0.4.0--r40h6115d3f_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-tigger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-tigger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-tigger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-tigger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-tigger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-tigger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-tigger

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