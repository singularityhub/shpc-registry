---
layout: container
name:  "quay.io/biocontainers/bioconductor-siggenes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-siggenes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-siggenes/container.yaml"
updated_at: "2024-01-10 23:43:26.272557"
latest: "1.76.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-siggenes"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-siggenes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-siggenes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-siggenes", "latest": {"1.76.0--r43hdfd78af_0": "sha256:1e48cbc51da758cc1651d9bc3350e522b6c7349d4874062dcff0a10900fab31a"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:63f8adf23b59e7b9cfe87dec801fe501301e6523303a45751faa347021520a7b", "1.72.0--r42hdfd78af_0": "sha256:41a0d48ecadf0f487ba6fc4eaf054b0e40370993a2b6e3cca80f83f0111d845e", "1.74.0--r43hdfd78af_0": "sha256:964a9a5e7e558248621a1db31dbce26fdc93170a2d10f29b00116d8372561f35", "1.76.0--r43hdfd78af_0": "sha256:1e48cbc51da758cc1651d9bc3350e522b6c7349d4874062dcff0a10900fab31a"}, "docker": "quay.io/biocontainers/bioconductor-siggenes"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-siggenes.
shpc-registry automated BioContainers addition for bioconductor-siggenes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-siggenes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-siggenes:1.76.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-siggenes/1.76.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-siggenes/1.76.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-siggenes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-siggenes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-siggenes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-siggenes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-siggenes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-siggenes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-siggenes

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