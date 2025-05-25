---
layout: container
name:  "quay.io/biocontainers/bioconductor-codelink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-codelink/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-codelink/container.yaml"
updated_at: "2025-05-25 03:42:56.389371"
latest: "1.74.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-codelink"

versions:
 - "1.62.0--r41hdfd78af_0"
 - "1.66.0--r42hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
 - "1.74.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-codelink"
config: {"url": "https://biocontainers.pro/tools/bioconductor-codelink", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-codelink", "latest": {"1.74.0--r44hdfd78af_0": "sha256:64af5bc16853b75f713c4b2bdb6c6231199d3284a5f8b49975705dc6b272e0c8"}, "tags": {"1.62.0--r41hdfd78af_0": "sha256:b4f12167519b0874e9e205216981e965c066cbfa0e9c4ee8a84f3f6124a7e1c9", "1.66.0--r42hdfd78af_0": "sha256:2769f3144f32d09bef0b9b1daf54089ddc28491733918e64147bdfe648505d29", "1.68.0--r43hdfd78af_0": "sha256:053dd03a28403d3adf6ed4bb773d98531ed0cc18afb9363be60236898064394f", "1.70.0--r43hdfd78af_0": "sha256:9bf63ebdb136bd5c6318079b8ae2a9290a6c263e228f008c4e107a9a1460eeaf", "1.74.0--r44hdfd78af_0": "sha256:64af5bc16853b75f713c4b2bdb6c6231199d3284a5f8b49975705dc6b272e0c8"}, "docker": "quay.io/biocontainers/bioconductor-codelink"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-codelink.
shpc-registry automated BioContainers addition for bioconductor-codelink
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-codelink
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-codelink:1.74.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-codelink/1.74.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-codelink/1.74.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-codelink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-codelink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-codelink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-codelink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-codelink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-codelink-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-codelink

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