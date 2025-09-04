---
layout: container
name:  "quay.io/biocontainers/pbccs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbccs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbccs/container.yaml"
updated_at: "2025-09-04 03:09:49.684461"
latest: "6.4.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/pbccs"
aliases:
 - "ccs"
 - "ccs-alt"
versions:
 - "6.4.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for pbccs"
config: {"url": "https://biocontainers.pro/tools/pbccs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbccs", "latest": {"6.4.0--h9ee0642_0": "sha256:6876708af8f1bd3af45740d86fa2f0479bea48e72bc97118240cb9f4fbd5e13b"}, "tags": {"6.4.0--h9ee0642_0": "sha256:6876708af8f1bd3af45740d86fa2f0479bea48e72bc97118240cb9f4fbd5e13b"}, "docker": "quay.io/biocontainers/pbccs", "aliases": {"ccs": "/usr/local/bin/ccs", "ccs-alt": "/usr/local/bin/ccs-alt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbccs.
shpc-registry automated BioContainers addition for pbccs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbccs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbccs:6.4.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbccs/6.4.0--h9ee0642_0
$ module help quay.io/biocontainers/pbccs/6.4.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbccs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbccs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbccs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbccs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbccs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbccs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccs

```bash
$ singularity exec <container> /usr/local/bin/ccs
$ podman run --it --rm --entrypoint /usr/local/bin/ccs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccs-alt

```bash
$ singularity exec <container> /usr/local/bin/ccs-alt
$ podman run --it --rm --entrypoint /usr/local/bin/ccs-alt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs-alt   -v ${PWD} -w ${PWD} <container> -c " $@"
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