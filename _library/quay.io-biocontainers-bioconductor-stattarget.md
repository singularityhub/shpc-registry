---
layout: container
name:  "quay.io/biocontainers/bioconductor-stattarget"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-stattarget/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-stattarget/container.yaml"
updated_at: "2023-07-28 03:25:22.806389"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-stattarget"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-stattarget"
config: {"url": "https://biocontainers.pro/tools/bioconductor-stattarget", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-stattarget", "latest": {"1.30.0--r43hdfd78af_0": "sha256:e9191781d833c8ad86985c45adbc4a87ae27ef4c61ca35ab2c5e585132c7617c"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:aaa0f8b11f40823242ec21e4e8e8a33a83312e77cde7c4e3eadcfadc21aee90d", "1.28.0--r42hdfd78af_0": "sha256:a16d7b9a17fb9ddab930d43994032ac9c2e4ba82f46a0fdc0b466d57aedf74e1", "1.30.0--r43hdfd78af_0": "sha256:e9191781d833c8ad86985c45adbc4a87ae27ef4c61ca35ab2c5e585132c7617c"}, "docker": "quay.io/biocontainers/bioconductor-stattarget"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-stattarget.
shpc-registry automated BioContainers addition for bioconductor-stattarget
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-stattarget
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-stattarget:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-stattarget/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-stattarget/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-stattarget-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stattarget-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stattarget-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-stattarget-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-stattarget-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-stattarget-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-stattarget

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