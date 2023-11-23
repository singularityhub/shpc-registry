---
layout: container
name:  "quay.io/biocontainers/bioconductor-olingui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-olingui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-olingui/container.yaml"
updated_at: "2023-11-23 04:09:44.764346"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-olingui"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-olingui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-olingui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-olingui", "latest": {"1.74.0--r43hdfd78af_0": "sha256:3b0a390b181a67aec5ff0b583d0db434915d68a096d71e03bb783afc6f844d30"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:0c68bf4faec1de2873b8b7339e31e1ddf8a66a425d336dc47fcfa743c913e3a4", "1.72.0--r42hdfd78af_0": "sha256:f1a06b9f195579d5bf0e6f9e74c3533b1ce177adbe2090e7764203cba2caebe1", "1.74.0--r43hdfd78af_0": "sha256:3b0a390b181a67aec5ff0b583d0db434915d68a096d71e03bb783afc6f844d30"}, "docker": "quay.io/biocontainers/bioconductor-olingui"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-olingui.
shpc-registry automated BioContainers addition for bioconductor-olingui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-olingui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-olingui:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-olingui/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-olingui/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-olingui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-olingui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-olingui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-olingui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-olingui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-olingui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-olingui

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