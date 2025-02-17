---
layout: container
name:  "quay.io/biocontainers/bioconductor-affylmgui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affylmgui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affylmgui/container.yaml"
updated_at: "2025-02-17 03:24:35.290529"
latest: "1.80.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affylmgui"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.80.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affylmgui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affylmgui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affylmgui", "latest": {"1.80.0--r44hdfd78af_0": "sha256:d1d5901a8d6ef86cdfc166b6c9225c2004ca958cbd793ba26419b77868311fd9"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:0e6e91168cbbe9258397f9e7f951c831083528fee8ca1e30b167be63a9a6ee85", "1.72.0--r42hdfd78af_0": "sha256:2ccc9c0e0ac340d65167382fc2803e5ac0cc43c9509023921c5b0be9f04b3072", "1.74.0--r43hdfd78af_0": "sha256:cf3e7419f1b826f18d5df8deb581b6da6fbca3cddffd6655498eeb0895702b7c", "1.76.0--r43hdfd78af_0": "sha256:6c452ab94612747a581239da6a98de18905a512836a9e6aff707652f723d3ded", "1.80.0--r44hdfd78af_0": "sha256:d1d5901a8d6ef86cdfc166b6c9225c2004ca958cbd793ba26419b77868311fd9"}, "docker": "quay.io/biocontainers/bioconductor-affylmgui"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affylmgui.
shpc-registry automated BioContainers addition for bioconductor-affylmgui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affylmgui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affylmgui:1.80.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affylmgui/1.80.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affylmgui/1.80.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affylmgui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affylmgui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affylmgui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affylmgui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affylmgui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affylmgui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affylmgui

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