---
layout: container
name:  "quay.io/biocontainers/psdm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psdm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psdm/container.yaml"
updated_at: "2024-04-16 02:39:50.046143"
latest: "0.2.0--h031d066_3"
container_url: "https://biocontainers.pro/tools/psdm"
aliases:
 - "psdm"
versions:
 - "0.2.0--hec16e2b_1"
 - "0.2.0--h031d066_3"
description: "shpc-registry automated BioContainers addition for psdm"
config: {"url": "https://biocontainers.pro/tools/psdm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for psdm", "latest": {"0.2.0--h031d066_3": "sha256:fa495bbe1c600390216466570cb4ff4b5bcdd419d83aaae55e7fe43dff97dac3"}, "tags": {"0.2.0--hec16e2b_1": "sha256:d217f8d5850dfd3dcafa49b194eba7b5579b94a81565570557b81118de305b6a", "0.2.0--h031d066_3": "sha256:fa495bbe1c600390216466570cb4ff4b5bcdd419d83aaae55e7fe43dff97dac3"}, "docker": "quay.io/biocontainers/psdm", "aliases": {"psdm": "/usr/local/bin/psdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psdm.
shpc-registry automated BioContainers addition for psdm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psdm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psdm:0.2.0--h031d066_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psdm/0.2.0--h031d066_3
$ module help quay.io/biocontainers/psdm/0.2.0--h031d066_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psdm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psdm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psdm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psdm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psdm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psdm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### psdm

```bash
$ singularity exec <container> /usr/local/bin/psdm
$ podman run --it --rm --entrypoint /usr/local/bin/psdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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