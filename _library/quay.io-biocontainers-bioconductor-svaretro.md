---
layout: container
name:  "quay.io/biocontainers/bioconductor-svaretro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-svaretro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-svaretro/container.yaml"
updated_at: "2024-12-05 03:23:42.739674"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-svaretro"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-svaretro"
config: {"url": "https://biocontainers.pro/tools/bioconductor-svaretro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-svaretro", "latest": {"1.8.0--r43hdfd78af_0": "sha256:a94c8313e127b92f1bf3e1485894c0bf7e6f202ada73ecd241679398712f4e0d"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:770cca9735b372122e8edbf58acecfd7f552b0415f396dfbf5615267de7cbc73", "1.4.0--r42hdfd78af_0": "sha256:8ba70467b5644eb865f1611d101749cd693bd6a4804d4ab810ccb1e82302ab72", "1.6.0--r43hdfd78af_0": "sha256:b11582ced7cec814cd372fd2f43dd6c657ce9a85c8811b612b760bf382896a42", "1.8.0--r43hdfd78af_0": "sha256:a94c8313e127b92f1bf3e1485894c0bf7e6f202ada73ecd241679398712f4e0d"}, "docker": "quay.io/biocontainers/bioconductor-svaretro"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-svaretro.
shpc-registry automated BioContainers addition for bioconductor-svaretro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-svaretro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-svaretro:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-svaretro/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-svaretro/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-svaretro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svaretro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svaretro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-svaretro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-svaretro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-svaretro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-svaretro

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