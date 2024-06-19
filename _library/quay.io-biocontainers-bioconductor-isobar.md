---
layout: container
name:  "quay.io/biocontainers/bioconductor-isobar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-isobar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-isobar/container.yaml"
updated_at: "2024-06-19 02:49:35.781502"
latest: "1.48.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-isobar"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-isobar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-isobar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-isobar", "latest": {"1.48.0--r43hdfd78af_0": "sha256:734fe8674f141175c67d79c8b429aebfacbc00dd328b7b7d631c873f9f65d39d"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:06bc967f38b82014860c949c32b88ec60f749ec98d5d80b8477517a04eb25a39", "1.44.0--r42hdfd78af_0": "sha256:fd06ea4eb320f9a45540cf0c62035175cfd93dde2f4762176935144cfd0c9b5d", "1.46.0--r43hdfd78af_0": "sha256:8ecbdbfa01862434c3d0f6e9f9f44a156985133bc4ea2b13770686cbda4a4ab8", "1.48.0--r43hdfd78af_0": "sha256:734fe8674f141175c67d79c8b429aebfacbc00dd328b7b7d631c873f9f65d39d"}, "docker": "quay.io/biocontainers/bioconductor-isobar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-isobar.
shpc-registry automated BioContainers addition for bioconductor-isobar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-isobar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-isobar:1.48.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-isobar/1.48.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-isobar/1.48.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-isobar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isobar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isobar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-isobar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-isobar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-isobar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-isobar

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