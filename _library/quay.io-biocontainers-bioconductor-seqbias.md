---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqbias"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqbias/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqbias/container.yaml"
updated_at: "2024-06-02 03:13:10.105143"
latest: "1.50.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqbias"

versions:
 - "1.42.0--r41hc247a5b_2"
 - "1.46.0--r42hc247a5b_0"
 - "1.46.0--r42hf17093f_1"
 - "1.48.0--r43hf17093f_0"
 - "1.50.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqbias"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqbias", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqbias", "latest": {"1.50.0--r43hf17093f_0": "sha256:b00cfa7eb2d74b575c60f0b446be88b3b1315aab7410df9af2a7c4a64d6311ca"}, "tags": {"1.42.0--r41hc247a5b_2": "sha256:eeea2a558e3b230722e58bdc77c6829ae4787aca92cd927ad0ed823d6da1dfcc", "1.46.0--r42hc247a5b_0": "sha256:c334c7cccb9b5248bed4d816125b6f80ea60350979827a20dd8f8877f916efa6", "1.46.0--r42hf17093f_1": "sha256:90dd6322695bea73052edb88538e67162695f60178a502b381f216c39ed370d2", "1.48.0--r43hf17093f_0": "sha256:5c9842611df0ad8fd8e532694d9e4dc16e061d0a50d5be8a3e15077f344f9aa8", "1.50.0--r43hf17093f_0": "sha256:b00cfa7eb2d74b575c60f0b446be88b3b1315aab7410df9af2a7c4a64d6311ca"}, "docker": "quay.io/biocontainers/bioconductor-seqbias"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqbias.
shpc-registry automated BioContainers addition for bioconductor-seqbias
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqbias
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqbias:1.50.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqbias/1.50.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-seqbias/1.50.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqbias-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqbias-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqbias-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqbias-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqbias-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqbias-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqbias

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