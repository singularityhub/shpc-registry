---
layout: container
name:  "quay.io/biocontainers/bioconductor-phosr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phosr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phosr/container.yaml"
updated_at: "2025-11-10 03:43:23.177864"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phosr"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phosr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phosr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phosr", "latest": {"1.16.0--r44hdfd78af_0": "sha256:9d8bf879cb8dceece3892722772ba035ac8993b5256d576cb9a8971a201998d2"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:0f26621d084b3057bdf71a41148dbf00752304fa9d26dfd2b07585cf5294cdf4", "1.8.0--r42hdfd78af_0": "sha256:d420f3d8c4a1e2dd0c886bd7afa3022c1d7c619a83e58ea1e5fd30ece7abc7f1", "1.10.0--r43hdfd78af_0": "sha256:5a5f6c21a5f6a46fe6cc25f072531753803c8a8e1ed9ed0b642c46220edd331b", "1.12.0--r43hdfd78af_0": "sha256:cdf004cdfa3788b495d4cb0d2d73e833b1c124a3d54111de1e41f76748e9dca7", "1.16.0--r44hdfd78af_0": "sha256:9d8bf879cb8dceece3892722772ba035ac8993b5256d576cb9a8971a201998d2"}, "docker": "quay.io/biocontainers/bioconductor-phosr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phosr.
shpc-registry automated BioContainers addition for bioconductor-phosr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phosr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phosr:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phosr/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phosr/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phosr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phosr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phosr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phosr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phosr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phosr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phosr

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