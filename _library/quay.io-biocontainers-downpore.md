---
layout: container
name:  "quay.io/biocontainers/downpore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/downpore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/downpore/container.yaml"
updated_at: "2023-06-03 03:44:10.787694"
latest: "0.3.4--he881be0_1"
container_url: "https://biocontainers.pro/tools/downpore"
aliases:
 - "downpore"
versions:
 - "0.3.4--he881be0_1"
description: "shpc-registry automated BioContainers addition for downpore"
config: {"url": "https://biocontainers.pro/tools/downpore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for downpore", "latest": {"0.3.4--he881be0_1": "sha256:3f39bab60fae4af1d180dc6a55fe114f665099e30456d3c66d6b223e509a5194"}, "tags": {"0.3.4--he881be0_1": "sha256:3f39bab60fae4af1d180dc6a55fe114f665099e30456d3c66d6b223e509a5194"}, "docker": "quay.io/biocontainers/downpore", "aliases": {"downpore": "/usr/local/bin/downpore"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/downpore.
shpc-registry automated BioContainers addition for downpore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/downpore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/downpore:0.3.4--he881be0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/downpore/0.3.4--he881be0_1
$ module help quay.io/biocontainers/downpore/0.3.4--he881be0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### downpore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### downpore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### downpore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### downpore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### downpore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### downpore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### downpore

```bash
$ singularity exec <container> /usr/local/bin/downpore
$ podman run --it --rm --entrypoint /usr/local/bin/downpore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/downpore   -v ${PWD} -w ${PWD} <container> -c " $@"
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