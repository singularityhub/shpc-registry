---
layout: container
name:  "quay.io/biocontainers/bioconductor-limma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-limma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-limma/container.yaml"
updated_at: "2025-04-25 02:14:22.872973"
latest: "3.62.1--r44h15a9599_1"
container_url: "https://biocontainers.pro/tools/bioconductor-limma"

versions:
 - "3.50.3--r41hc0cfd56_0"
 - "3.54.0--r42hc0cfd56_0"
 - "3.54.0--r42ha9d7317_1"
 - "3.56.2--r43ha9d7317_0"
 - "3.58.1--r43ha9d7317_0"
 - "3.58.1--r43ha9d7317_1"
 - "3.62.0--r44h3df3fcb_0"
 - "3.62.1--r44h15a9599_0"
 - "3.62.1--r44h15a9599_1"
description: "shpc-registry automated BioContainers addition for bioconductor-limma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-limma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-limma", "latest": {"3.62.1--r44h15a9599_1": "sha256:d7a479f4708c1d10cb4ff0b06a21bababe3bb3a6078a5937e0accff23d8862c8"}, "tags": {"3.50.3--r41hc0cfd56_0": "sha256:ebe08bf8c6a098e89b76c5d79b0f6067da6b41971b6ef6b1c6fb0a5ce74e6eea", "3.54.0--r42hc0cfd56_0": "sha256:f7a607e4a49ad05903e61b010dc8fe7f41abf82499935c2a987373b243c428e6", "3.54.0--r42ha9d7317_1": "sha256:ae9917d2e0603bf18ac255fe5f8369e109cfeb04af3e82981014561c347af6bb", "3.56.2--r43ha9d7317_0": "sha256:c3ac0aee43d92e5792b109d0047e50bc0b7934b39c193c8ae965fe3a6777027e", "3.58.1--r43ha9d7317_0": "sha256:1421da35360fecab780873012c618fbba3f27d5f9336ad93fae05c2a7bf68b83", "3.58.1--r43ha9d7317_1": "sha256:496d2026f7bf6f11562bcaec9a20738e2c68fdcef5925b4d8db2df23094e3ecb", "3.62.0--r44h3df3fcb_0": "sha256:f65c70cf30898ab4aa0b195fa75a4bc3380769b3eb7d32d4d05c0122c397719f", "3.62.1--r44h15a9599_0": "sha256:142f005da938f5e1de8ebe7f12a0bdccb83568faeb555414ee1c14d2774fc1c9", "3.62.1--r44h15a9599_1": "sha256:d7a479f4708c1d10cb4ff0b06a21bababe3bb3a6078a5937e0accff23d8862c8"}, "docker": "quay.io/biocontainers/bioconductor-limma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-limma.
shpc-registry automated BioContainers addition for bioconductor-limma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-limma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-limma:3.62.1--r44h15a9599_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-limma/3.62.1--r44h15a9599_1
$ module help quay.io/biocontainers/bioconductor-limma/3.62.1--r44h15a9599_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-limma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-limma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-limma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-limma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-limma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-limma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-limma

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