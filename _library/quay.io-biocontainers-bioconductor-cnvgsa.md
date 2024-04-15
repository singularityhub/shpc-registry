---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvgsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvgsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvgsa/container.yaml"
updated_at: "2024-04-15 06:21:58.618675"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvgsa"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvgsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvgsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvgsa", "latest": {"1.46.0--r43hdfd78af_0": "sha256:f6548bbaea104ab54b9db7d5c602b338217ab67779d2ea787fb7fa1637fd89f4"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:6c72e0d34bfdaa3b5e7d72707fdac4968c65040e3f331a8ddf8a6e7b406b76ce", "1.42.0--r42hdfd78af_0": "sha256:c3f7a79894d2a13c630059919d1022095b825f2df41131c19d1d845d25d76bb7", "1.44.0--r43hdfd78af_0": "sha256:c8f5f1d1a8120c89aff23f35ea33187cb3dde189000c3697ba5b9a8fca676864", "1.46.0--r43hdfd78af_0": "sha256:f6548bbaea104ab54b9db7d5c602b338217ab67779d2ea787fb7fa1637fd89f4"}, "docker": "quay.io/biocontainers/bioconductor-cnvgsa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvgsa.
shpc-registry automated BioContainers addition for bioconductor-cnvgsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvgsa:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvgsa/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnvgsa/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnvgsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvgsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvgsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnvgsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnvgsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnvgsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cnvgsa

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