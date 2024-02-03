---
layout: container
name:  "quay.io/biocontainers/bioconductor-trare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trare/container.yaml"
updated_at: "2024-02-03 02:41:51.000843"
latest: "1.5.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trare"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.5.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trare"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trare", "latest": {"1.5.0--r42hdfd78af_0": "sha256:33a593497fb022764e45bcc866f67eb23f22881ea3165860a9094acafb206d77"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:87a50b37b3d0b280852615403626c89d22171fd18ab8d11a02798e8b7355f4cf", "1.5.0--r42hdfd78af_0": "sha256:33a593497fb022764e45bcc866f67eb23f22881ea3165860a9094acafb206d77"}, "docker": "quay.io/biocontainers/bioconductor-trare"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trare.
shpc-registry automated BioContainers addition for bioconductor-trare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trare:1.5.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trare/1.5.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trare/1.5.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trare-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-trare

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