---
layout: container
name:  "quay.io/biocontainers/bioconductor-bcellviper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bcellviper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bcellviper/container.yaml"
updated_at: "2025-11-27 03:52:17.765674"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bcellviper"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bcellviper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bcellviper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bcellviper", "latest": {"1.42.0--r44hdfd78af_0": "sha256:568fcec5101331271e1bbf12db1d9644296d65df4fc92bf766d7397a651b13b3"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:a8a979f5220e7eb2ef61d0d4cd6ebf98858ceefdc664194f671a86b366e88356", "1.34.0--r42hdfd78af_0": "sha256:52390641f5268fa4545b1843a965893c2b121f0d661ec92e54cb10c4f55cc28c", "1.36.0--r43hdfd78af_0": "sha256:897bc962e303e02599d05bf64e08523ddac89f34a006a8262207ab6c567bb0c7", "1.38.0--r43hdfd78af_0": "sha256:b60132123436c62e3840f79d577be7ded51b0c283f62603e0f062b053b365b21", "1.42.0--r44hdfd78af_0": "sha256:568fcec5101331271e1bbf12db1d9644296d65df4fc92bf766d7397a651b13b3"}, "docker": "quay.io/biocontainers/bioconductor-bcellviper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bcellviper.
shpc-registry automated BioContainers addition for bioconductor-bcellviper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bcellviper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bcellviper:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bcellviper/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bcellviper/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bcellviper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bcellviper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bcellviper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bcellviper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bcellviper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bcellviper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bcellviper

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