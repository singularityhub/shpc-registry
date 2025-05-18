---
layout: container
name:  "quay.io/biocontainers/bioconductor-htqpcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htqpcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htqpcr/container.yaml"
updated_at: "2025-05-18 03:22:46.210598"
latest: "1.56.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-htqpcr"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-htqpcr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htqpcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htqpcr", "latest": {"1.56.0--r43hdfd78af_0": "sha256:cea6fdd9188f2d4cae5d9295c970ae5f5dfdaaa5a55b942e6c9b1a9836af9a2a"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:3ed305a8a9bbaa5138133e71c3f9739a978439110d14ea6292a1f27f4da69370", "1.52.0--r42hdfd78af_0": "sha256:b1b032752dcbde0352e3a485ecebf6fa40959f9b96aa91c19285250ecb11edc3", "1.54.0--r43hdfd78af_0": "sha256:59ead975d92db3bd05602b89b39e45aa8d29a7a289734698766469f3d4837934", "1.56.0--r43hdfd78af_0": "sha256:cea6fdd9188f2d4cae5d9295c970ae5f5dfdaaa5a55b942e6c9b1a9836af9a2a"}, "docker": "quay.io/biocontainers/bioconductor-htqpcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htqpcr.
shpc-registry automated BioContainers addition for bioconductor-htqpcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htqpcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htqpcr:1.56.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htqpcr/1.56.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-htqpcr/1.56.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htqpcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htqpcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htqpcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htqpcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htqpcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htqpcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htqpcr

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