---
layout: container
name:  "quay.io/biocontainers/bioconductor-metapod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metapod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metapod/container.yaml"
updated_at: "2025-09-20 03:39:57.734449"
latest: "1.14.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-metapod"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_2"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_1"
 - "1.10.0--r43hf17093f_2"
 - "1.10.0--r43hf17093f_3"
 - "1.14.0--r44he5774e6_0"
 - "1.14.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-metapod"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metapod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metapod", "latest": {"1.14.0--r44he5774e6_1": "sha256:d751e1ce5820a16caf7fa1aa5bd32fcb80c6b3431d4c9907bcb852b715bc05a2"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:928cf849fb46ac357439fb25740455b265e0bc4f18a250a8b4a56b546de4cb26", "1.6.0--r42hc247a5b_0": "sha256:ad73555ccfc934134b418aa3c703981b486ffd32552c437e82b6aeba430bf074", "1.6.0--r42hf17093f_2": "sha256:dba394b2ba823e1dbdf0382c51dd6dbe46ae72c46816f136a32e3d9af52cf92d", "1.8.0--r43hf17093f_0": "sha256:43cca96eb3377869aaa7702805b87c72b12ae42603a2888106df088be8a9f78d", "1.10.0--r43hf17093f_1": "sha256:93b77e42b5f9e63fe73a919509b20e8e1e73fe71705b006fa2d3b395a392a5b1", "1.10.0--r43hf17093f_2": "sha256:53dba26f7a4d486cf3d7e329c152d27013bf8695a270d12bbd982359a772fe91", "1.10.0--r43hf17093f_3": "sha256:915d697726aac38bea9e5e945a9ba7806c83730734318bfec750439eec1125fa", "1.14.0--r44he5774e6_0": "sha256:41a2653985d93853814c96484568462ea4a903fca7257a88fbc24052b55eafe1", "1.14.0--r44he5774e6_1": "sha256:d751e1ce5820a16caf7fa1aa5bd32fcb80c6b3431d4c9907bcb852b715bc05a2"}, "docker": "quay.io/biocontainers/bioconductor-metapod"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metapod.
shpc-registry automated BioContainers addition for bioconductor-metapod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metapod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metapod:1.14.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metapod/1.14.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-metapod/1.14.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metapod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metapod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metapod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metapod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metapod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metapod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metapod

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