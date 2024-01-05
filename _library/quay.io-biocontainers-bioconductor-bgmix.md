---
layout: container
name:  "quay.io/biocontainers/bioconductor-bgmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bgmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bgmix/container.yaml"
updated_at: "2024-01-05 02:41:02.286877"
latest: "1.59.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bgmix"

versions:
 - "1.54.0--r41hc247a5b_2"
 - "1.58.0--r42hc247a5b_0"
 - "1.58.0--r42hc247a5b_1"
 - "1.58.0--r42hf17093f_2"
 - "1.59.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bgmix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bgmix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bgmix", "latest": {"1.59.0--r43hf17093f_0": "sha256:8ca36955c8a2da2cd83f7518d51c745a6e428fc28258f39ec21b635ffe7fd001"}, "tags": {"1.54.0--r41hc247a5b_2": "sha256:c5a3d5e8ecb4f2f8338c63c483a976e353eff0253bb12986d29ce07b11022bf4", "1.58.0--r42hc247a5b_0": "sha256:acfb1abe7e749d2edf11249036f4a9a8f5967e24fa29918e19b355a8bc124abf", "1.58.0--r42hc247a5b_1": "sha256:6e51f40e2f86582b8c2f6b726daaefa83fc30f98197ecaf52bca418c1a795303", "1.58.0--r42hf17093f_2": "sha256:ef8349c6c732ba2fa24f8697b39bef63492e49040681ab5471969fc1e2149358", "1.59.0--r43hf17093f_0": "sha256:8ca36955c8a2da2cd83f7518d51c745a6e428fc28258f39ec21b635ffe7fd001"}, "docker": "quay.io/biocontainers/bioconductor-bgmix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bgmix.
shpc-registry automated BioContainers addition for bioconductor-bgmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bgmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bgmix:1.59.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bgmix/1.59.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-bgmix/1.59.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bgmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bgmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bgmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bgmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bgmix

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