---
layout: container
name:  "quay.io/biocontainers/bioconductor-dexma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dexma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dexma/container.yaml"
updated_at: "2025-06-17 03:53:17.107993"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dexma"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.6--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dexma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dexma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dexma", "latest": {"1.14.0--r44hdfd78af_0": "sha256:f09387de011e18e30909936cfe6c3319d3502d092f7ae0545ca0636c11d7036e"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:a3cb64910b447c4a44e058f7b7b36311268e366b97cc08b9f1af00a68c2fe41c", "1.6.0--r42hdfd78af_0": "sha256:43544a65f278d7fc0ccb932a48aef95b37d8145a5e296184f17d27ba58cbf91d", "1.8.0--r43hdfd78af_0": "sha256:b97f284a957ab38e72c0e973fda0cdccc65aab8dcf28c1dc02b189e44c7a6d61", "1.10.6--r43hdfd78af_0": "sha256:28e3f0efd0e55ed93266dfa41f1863a871b66f2533c8f30a1be85d5f7e357634", "1.14.0--r44hdfd78af_0": "sha256:f09387de011e18e30909936cfe6c3319d3502d092f7ae0545ca0636c11d7036e"}, "docker": "quay.io/biocontainers/bioconductor-dexma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dexma.
shpc-registry automated BioContainers addition for bioconductor-dexma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dexma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dexma:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dexma/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dexma/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dexma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dexma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dexma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dexma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dexma

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