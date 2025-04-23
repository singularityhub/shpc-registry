---
layout: container
name:  "quay.io/biocontainers/bioconductor-interaccircos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-interaccircos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-interaccircos/container.yaml"
updated_at: "2025-04-23 03:42:57.782897"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-interaccircos"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-interaccircos"
config: {"url": "https://biocontainers.pro/tools/bioconductor-interaccircos", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-interaccircos", "latest": {"1.16.0--r44hdfd78af_0": "sha256:c26551e8f38eb512dabf300c588cef574b9cb4dec8159101cc2ca034c7339c6d"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:db009e2e1d0db0926be91d0da1ac0f9c2681e46891f819c031d4326aefcd1811", "1.8.0--r42hdfd78af_0": "sha256:4af3f77f6935bba660b83427b37f004b584537b97ff1ab132614a53519cbdfa7", "1.10.0--r43hdfd78af_0": "sha256:7fe2ca2e3d14b3fb8ad566b2eda9cd97d40eebbb7126b502aa088ce7b8f432a9", "1.12.0--r43hdfd78af_0": "sha256:0ce3c39ef43580fb060cf582f624c8fd6ddf49a424cce2e5e12a4b7a3c97f7c2", "1.16.0--r44hdfd78af_0": "sha256:c26551e8f38eb512dabf300c588cef574b9cb4dec8159101cc2ca034c7339c6d"}, "docker": "quay.io/biocontainers/bioconductor-interaccircos"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-interaccircos.
shpc-registry automated BioContainers addition for bioconductor-interaccircos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-interaccircos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-interaccircos:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-interaccircos/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-interaccircos/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-interaccircos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interaccircos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interaccircos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-interaccircos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-interaccircos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-interaccircos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-interaccircos

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