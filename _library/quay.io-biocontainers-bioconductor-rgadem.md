---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgadem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgadem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgadem/container.yaml"
updated_at: "2025-11-01 03:49:04.872755"
latest: "2.54.0--r44h3df3fcb_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rgadem"

versions:
 - "2.42.0--r41hc0cfd56_2"
 - "2.46.0--r42hc0cfd56_0"
 - "2.46.0--r42ha9d7317_1"
 - "2.48.0--r43ha9d7317_0"
 - "2.50.0--r43ha9d7317_0"
 - "2.54.0--r44h3df3fcb_0"
 - "2.54.0--r44h3df3fcb_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rgadem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgadem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgadem", "latest": {"2.54.0--r44h3df3fcb_1": "sha256:884032606b0f132f856f3ada757255b4eb5054703b96f0abfdab457c9dfa664b"}, "tags": {"2.42.0--r41hc0cfd56_2": "sha256:46ed0f62604fc8ec7ab7a01bd5d7bde2c99904d12e6de58d1995ea9f66a11dae", "2.46.0--r42hc0cfd56_0": "sha256:92a919abe26585b01f64603b07edcfd681cf9f48193731d44fc3d441fc2566bd", "2.46.0--r42ha9d7317_1": "sha256:fd90d6a01a0bfb97dd79ed7c1e923a00f82d27301a6d49ddb1ae5c64b904b35d", "2.48.0--r43ha9d7317_0": "sha256:f6ada7a6ae788296497f8d2e2f4d951d784a2e7befc7c40921494215b7cf6314", "2.50.0--r43ha9d7317_0": "sha256:1ce5f907fe57c69200531310761a041cbb467a9f93593daab9674de03116ecc1", "2.54.0--r44h3df3fcb_0": "sha256:c6cd0effca8ec121a16fd102c7678f6771c775986c242783616da14beff80bf5", "2.54.0--r44h3df3fcb_1": "sha256:884032606b0f132f856f3ada757255b4eb5054703b96f0abfdab457c9dfa664b"}, "docker": "quay.io/biocontainers/bioconductor-rgadem"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgadem.
shpc-registry automated BioContainers addition for bioconductor-rgadem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgadem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgadem:2.54.0--r44h3df3fcb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgadem/2.54.0--r44h3df3fcb_1
$ module help quay.io/biocontainers/bioconductor-rgadem/2.54.0--r44h3df3fcb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgadem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgadem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgadem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgadem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgadem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgadem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgadem

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