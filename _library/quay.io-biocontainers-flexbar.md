---
layout: container
name:  "quay.io/biocontainers/flexbar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flexbar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flexbar/container.yaml"
updated_at: "2024-03-23 02:44:42.348466"
latest: "3.5.0--hf92b6da_10"
container_url: "https://biocontainers.pro/tools/flexbar"
aliases:
 - "flexbar"
versions:
 - "3.5.0--hf53871c_6"
 - "3.5.0--hac0a8cf_8"
 - "3.5.0--hf92b6da_10"
description: "shpc-registry automated BioContainers addition for flexbar"
config: {"url": "https://biocontainers.pro/tools/flexbar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flexbar", "latest": {"3.5.0--hf92b6da_10": "sha256:ac4d1d5dd63ba853174805d22d021c119269befacd4fa65b30773b9909096c3a"}, "tags": {"3.5.0--hf53871c_6": "sha256:d40abb9636a555aee9e1c9343927a2a8931ea29bcc3483a938d48a81b44a2ba9", "3.5.0--hac0a8cf_8": "sha256:3a8e85519d5e2500776a66e6568abe52f3dc79e0148bc38682a2f12a7e651e52", "3.5.0--hf92b6da_10": "sha256:ac4d1d5dd63ba853174805d22d021c119269befacd4fa65b30773b9909096c3a"}, "docker": "quay.io/biocontainers/flexbar", "aliases": {"flexbar": "/usr/local/bin/flexbar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flexbar.
shpc-registry automated BioContainers addition for flexbar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flexbar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flexbar:3.5.0--hf92b6da_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flexbar/3.5.0--hf92b6da_10
$ module help quay.io/biocontainers/flexbar/3.5.0--hf92b6da_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flexbar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flexbar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flexbar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flexbar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flexbar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flexbar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flexbar

```bash
$ singularity exec <container> /usr/local/bin/flexbar
$ podman run --it --rm --entrypoint /usr/local/bin/flexbar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flexbar   -v ${PWD} -w ${PWD} <container> -c " $@"
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