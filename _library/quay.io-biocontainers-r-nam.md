---
layout: container
name:  "quay.io/biocontainers/r-nam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-nam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-nam/container.yaml"
updated_at: "2023-08-10 03:00:19.851098"
latest: "1.6.4--r351h9d2a408_0"
container_url: "https://biocontainers.pro/tools/r-nam"

versions:
 - "1.6.4--r351h9d2a408_0"
description: "shpc-registry automated BioContainers addition for r-nam"
config: {"url": "https://biocontainers.pro/tools/r-nam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-nam", "latest": {"1.6.4--r351h9d2a408_0": "sha256:b73c399a3cce876dc299e0faf44b571b38a88929edbc8ff5fdbcd983991be20f"}, "tags": {"1.6.4--r351h9d2a408_0": "sha256:b73c399a3cce876dc299e0faf44b571b38a88929edbc8ff5fdbcd983991be20f"}, "docker": "quay.io/biocontainers/r-nam"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-nam.
shpc-registry automated BioContainers addition for r-nam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-nam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-nam:1.6.4--r351h9d2a408_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-nam/1.6.4--r351h9d2a408_0
$ module help quay.io/biocontainers/r-nam/1.6.4--r351h9d2a408_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-nam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-nam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-nam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-nam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-nam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-nam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-nam

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