---
layout: container
name:  "quay.io/biocontainers/bioconductor-ewcedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ewcedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ewcedata/container.yaml"
updated_at: "2025-07-31 11:47:33.219893"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ewcedata"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ewcedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ewcedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ewcedata", "latest": {"1.14.0--r44hdfd78af_0": "sha256:9cb559f843aeedf0d4eb1b7a2950a7e28977acb610538dd581284d094a7631e1"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:ae26eb8c3bde8917033c632f4e1b69b591deea96d400746f88ebb32d3cb907a4", "1.6.0--r42hdfd78af_0": "sha256:9e8050ae54348485dd13c49a4969e49d5eabf744e65acbf123fe6059f298a64b", "1.8.0--r43hdfd78af_0": "sha256:687bc1ac0010b5debbdc5fce014914a3c3f27f84349843df842914b7de69f678", "1.10.0--r43hdfd78af_0": "sha256:e624a7e57695721cf7ba959f5f043bdba2b5ca7651702777b0ea1cce47444964", "1.14.0--r44hdfd78af_0": "sha256:9cb559f843aeedf0d4eb1b7a2950a7e28977acb610538dd581284d094a7631e1"}, "docker": "quay.io/biocontainers/bioconductor-ewcedata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ewcedata.
shpc-registry automated BioContainers addition for bioconductor-ewcedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ewcedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ewcedata:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ewcedata/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ewcedata/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ewcedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ewcedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ewcedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ewcedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ewcedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ewcedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ewcedata

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