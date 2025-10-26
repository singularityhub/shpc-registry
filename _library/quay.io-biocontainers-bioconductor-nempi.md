---
layout: container
name:  "quay.io/biocontainers/bioconductor-nempi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nempi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nempi/container.yaml"
updated_at: "2025-10-26 03:19:38.140762"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nempi"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nempi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nempi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nempi", "latest": {"1.10.0--r43hdfd78af_0": "sha256:61acb592a6392bdb968bac9950b25ca6c94b153b225756e141715d0311a7056a"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:3cba6b8ad8c5317d4ca619001e0fcba8316a43e45bb57b3517c8fee48c3e3491", "1.6.0--r42hdfd78af_0": "sha256:49521c8517ebc4f9f61dec79da32acf6eef726a20d809f1f74089ba0219c084e", "1.8.0--r43hdfd78af_0": "sha256:d2a947de06134374ad5f86bae8621e16b703c07ce3ff7af725bf1d80cfc826cb", "1.10.0--r43hdfd78af_0": "sha256:61acb592a6392bdb968bac9950b25ca6c94b153b225756e141715d0311a7056a"}, "docker": "quay.io/biocontainers/bioconductor-nempi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nempi.
shpc-registry automated BioContainers addition for bioconductor-nempi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nempi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nempi:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nempi/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nempi/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nempi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nempi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nempi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nempi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nempi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nempi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nempi

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