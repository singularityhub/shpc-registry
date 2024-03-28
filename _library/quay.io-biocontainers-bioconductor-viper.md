---
layout: container
name:  "quay.io/biocontainers/bioconductor-viper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-viper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-viper/container.yaml"
updated_at: "2024-03-28 02:55:13.218151"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-viper"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-viper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-viper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-viper", "latest": {"1.36.0--r43hdfd78af_0": "sha256:a747d7470ba6b01f09a3c2de737fb489490dd6c75c6fffeb636316c9241388f1"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:5116714e0804a77e69562a6c736b893d22993aea225c212c00ecf96516dc6585", "1.32.0--r42hdfd78af_0": "sha256:b6d5f9530685637421abf109c6594c9a83e75a7b32115f56b19b4d1c3c12d2a5", "1.34.0--r43hdfd78af_0": "sha256:0485c54e582d3ff15b5ace0145b14f13dce528c14132ba1406b2bcec8bc373a8", "1.36.0--r43hdfd78af_0": "sha256:a747d7470ba6b01f09a3c2de737fb489490dd6c75c6fffeb636316c9241388f1"}, "docker": "quay.io/biocontainers/bioconductor-viper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-viper.
shpc-registry automated BioContainers addition for bioconductor-viper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-viper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-viper:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-viper/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-viper/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-viper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-viper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-viper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-viper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-viper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-viper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-viper

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