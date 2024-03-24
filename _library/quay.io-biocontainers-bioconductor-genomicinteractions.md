---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicinteractions"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicinteractions/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicinteractions/container.yaml"
updated_at: "2024-03-24 02:57:49.619461"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicinteractions"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicinteractions"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicinteractions", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicinteractions", "latest": {"1.34.0--r43hdfd78af_0": "sha256:c387486a042f96ca54280e9e9b9c7fd3b8f5d67472c8c1eab1d363fa176a8360"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:e3c4c0754ecc47d2b6815efd2fbcb80eef51eddd5eae63e39e6cd9f7036ea47b", "1.32.0--r42hdfd78af_0": "sha256:884f547602a91b8fa8723e2504e390d9c4fef7cfd468690f992997477a429cef", "1.34.0--r43hdfd78af_0": "sha256:c387486a042f96ca54280e9e9b9c7fd3b8f5d67472c8c1eab1d363fa176a8360"}, "docker": "quay.io/biocontainers/bioconductor-genomicinteractions"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicinteractions.
shpc-registry automated BioContainers addition for bioconductor-genomicinteractions
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicinteractions
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicinteractions:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicinteractions/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomicinteractions/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicinteractions-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicinteractions-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicinteractions-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicinteractions-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicinteractions-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicinteractions-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomicinteractions

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