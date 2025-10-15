---
layout: container
name:  "quay.io/biocontainers/bioconductor-constand"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-constand/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-constand/container.yaml"
updated_at: "2025-10-15 03:25:22.000471"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-constand"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-constand"
config: {"url": "https://biocontainers.pro/tools/bioconductor-constand", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-constand", "latest": {"1.14.0--r44hdfd78af_0": "sha256:367ff54037da8e8582b1458899d40d07f5bafdc51f1f79ff907fda9335f969d1"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:55f6d60456d356bae51df3abd54e9605d5a43ca0cef3959d2e71249efb9d1616", "1.6.0--r42hdfd78af_0": "sha256:466f730f050de3de17892fcfffc9c45b3505aaa130654a4924cdbbef66c1bd1a", "1.8.0--r43hdfd78af_0": "sha256:b3be7d08f2c3d222be48325153157432f995c3f2da16b9d4cca377d7e8fc014f", "1.10.0--r43hdfd78af_0": "sha256:cbd4c8c125b876a6c1d4170e4fa97eafe5ec29363dd33f347f075e79a5088dad", "1.14.0--r44hdfd78af_0": "sha256:367ff54037da8e8582b1458899d40d07f5bafdc51f1f79ff907fda9335f969d1"}, "docker": "quay.io/biocontainers/bioconductor-constand"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-constand.
shpc-registry automated BioContainers addition for bioconductor-constand
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-constand
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-constand:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-constand/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-constand/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-constand-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-constand-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-constand-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-constand-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-constand-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-constand-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-constand

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