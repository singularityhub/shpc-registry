---
layout: container
name:  "quay.io/biocontainers/bioconductor-coregx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-coregx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-coregx/container.yaml"
updated_at: "2024-10-26 03:34:11.116549"
latest: "2.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-coregx"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "2.2.0--r42hdfd78af_0"
 - "2.4.0--r43hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-coregx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-coregx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-coregx", "latest": {"2.6.0--r43hdfd78af_0": "sha256:74302da79221e48924c64b9f8a01c5a39137e00f7795d20a69ae78b0b41c6035"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:dc0e22e245e8fa644826838eed3e304b9d15b5e9ade059a3320f59b08cf8a720", "2.2.0--r42hdfd78af_0": "sha256:e5b0fcec83c3799198835c3a96a2c9350c0929026bae4e1e434141351e39ec3a", "2.4.0--r43hdfd78af_0": "sha256:008b7c3fd345228b97445852ffa44299d4222c168739ad539bd5136ded1040ff", "2.6.0--r43hdfd78af_0": "sha256:74302da79221e48924c64b9f8a01c5a39137e00f7795d20a69ae78b0b41c6035"}, "docker": "quay.io/biocontainers/bioconductor-coregx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-coregx.
shpc-registry automated BioContainers addition for bioconductor-coregx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-coregx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-coregx:2.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-coregx/2.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-coregx/2.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-coregx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coregx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-coregx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-coregx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-coregx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-coregx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-coregx

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