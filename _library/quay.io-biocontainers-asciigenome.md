---
layout: container
name:  "quay.io/biocontainers/asciigenome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/asciigenome/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/asciigenome/container.yaml"
updated_at: "2022-10-27 00:21:19.189552"
latest: "1.8.0--0"
container_url: "https://biocontainers.pro/tools/asciigenome"
aliases:
 - "ASCIIGenome"
versions:
 - "1.8.0--0"
description: "shpc-registry automated BioContainers addition for asciigenome"
config: {"url": "https://biocontainers.pro/tools/asciigenome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for asciigenome", "latest": {"1.8.0--0": "sha256:0ad0505b4c6ff89bf69a28ff1d937a71afe19c1e8caa73e35553f11757f2f89c"}, "tags": {"1.8.0--0": "sha256:0ad0505b4c6ff89bf69a28ff1d937a71afe19c1e8caa73e35553f11757f2f89c"}, "docker": "quay.io/biocontainers/asciigenome", "aliases": {"ASCIIGenome": "/usr/local/bin/ASCIIGenome"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/asciigenome.
shpc-registry automated BioContainers addition for asciigenome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/asciigenome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/asciigenome:1.8.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/asciigenome/1.8.0--0
$ module help quay.io/biocontainers/asciigenome/1.8.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### asciigenome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### asciigenome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### asciigenome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### asciigenome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### asciigenome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### asciigenome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ASCIIGenome

```bash
$ singularity exec <container> /usr/local/bin/ASCIIGenome
$ podman run --it --rm --entrypoint /usr/local/bin/ASCIIGenome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ASCIIGenome   -v ${PWD} -w ${PWD} <container> -c " $@"
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