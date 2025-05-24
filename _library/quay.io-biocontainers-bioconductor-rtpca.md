---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtpca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtpca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtpca/container.yaml"
updated_at: "2025-05-24 03:56:32.416713"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtpca"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtpca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtpca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtpca", "latest": {"1.16.0--r44hdfd78af_0": "sha256:40f9dd30b47152220c69f321a95c7fb60ece717d678e3c88d4692f29a3e8b746"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:c5f917b4ff1fccc3d7baf837c8605808eb1b436025d4207ba6b301c70d556171", "1.8.0--r42hdfd78af_0": "sha256:aaaa0524c5faa13b3a2a430e11ee97d991bd47b0e1fc726f78e895417fae0fd2", "1.10.0--r43hdfd78af_0": "sha256:e7898d234df3698d5ab1f49ccb6d1d01a711f23268e3d6daffc385b8f7cec723", "1.12.0--r43hdfd78af_0": "sha256:b1a0c3a7cd941c8e56a86e3a55068daa1969b839ce161bd2cb7f4ec1862a59ea", "1.16.0--r44hdfd78af_0": "sha256:40f9dd30b47152220c69f321a95c7fb60ece717d678e3c88d4692f29a3e8b746"}, "docker": "quay.io/biocontainers/bioconductor-rtpca"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtpca.
shpc-registry automated BioContainers addition for bioconductor-rtpca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtpca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtpca:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtpca/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtpca/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtpca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtpca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtpca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtpca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtpca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtpca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rtpca

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