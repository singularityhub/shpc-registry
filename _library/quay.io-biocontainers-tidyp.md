---
layout: container
name:  "quay.io/biocontainers/tidyp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tidyp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tidyp/container.yaml"
updated_at: "2024-01-12 02:35:35.474587"
latest: "1.04--hec16e2b_4"
container_url: "https://biocontainers.pro/tools/tidyp"
aliases:
 - "tidyp"
versions:
 - "1.04--hec16e2b_4"
description: "shpc-registry automated BioContainers addition for tidyp"
config: {"url": "https://biocontainers.pro/tools/tidyp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tidyp", "latest": {"1.04--hec16e2b_4": "sha256:9cf2a6488ddd11bab48e6554043b323b23f5221c0fbbfbf2e09f6cf436558e71"}, "tags": {"1.04--hec16e2b_4": "sha256:9cf2a6488ddd11bab48e6554043b323b23f5221c0fbbfbf2e09f6cf436558e71"}, "docker": "quay.io/biocontainers/tidyp", "aliases": {"tidyp": "/usr/local/bin/tidyp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tidyp.
shpc-registry automated BioContainers addition for tidyp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tidyp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tidyp:1.04--hec16e2b_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tidyp/1.04--hec16e2b_4
$ module help quay.io/biocontainers/tidyp/1.04--hec16e2b_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tidyp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tidyp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tidyp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tidyp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tidyp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tidyp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tidyp

```bash
$ singularity exec <container> /usr/local/bin/tidyp
$ podman run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
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