---
layout: container
name:  "quay.io/biocontainers/coast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coast/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/coast/container.yaml"
updated_at: "2022-10-27 00:50:04.805831"
latest: "0.2.2--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/coast"
aliases:
 - "coast"
versions:
 - "0.2.2--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for coast"
config: {"url": "https://biocontainers.pro/tools/coast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for coast", "latest": {"0.2.2--pyh5e36f6f_0": "sha256:d83452302f64630cd49d8fecb16ff78bf5c47edb439cb3a53cc4c4d795d9f41a"}, "tags": {"0.2.2--pyh5e36f6f_0": "sha256:d83452302f64630cd49d8fecb16ff78bf5c47edb439cb3a53cc4c4d795d9f41a"}, "docker": "quay.io/biocontainers/coast", "aliases": {"coast": "/usr/local/bin/coast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coast.
shpc-registry automated BioContainers addition for coast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coast:0.2.2--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coast/0.2.2--pyh5e36f6f_0
$ module help quay.io/biocontainers/coast/0.2.2--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coast

```bash
$ singularity exec <container> /usr/local/bin/coast
$ podman run --it --rm --entrypoint /usr/local/bin/coast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coast   -v ${PWD} -w ${PWD} <container> -c " $@"
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