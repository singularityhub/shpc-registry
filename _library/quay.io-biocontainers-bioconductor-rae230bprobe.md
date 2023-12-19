---
layout: container
name:  "quay.io/biocontainers/bioconductor-rae230bprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rae230bprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rae230bprobe/container.yaml"
updated_at: "2023-12-19 02:33:05.744522"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rae230bprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rae230bprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rae230bprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rae230bprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:4808a42af832c54843c8c8b29f1f8cf9965fd5b378e023314b176361ef831125"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:362780265fc1de5a89f129c90cb43fef2ad7eaae31c5fac259a41ebb62dfe8ab", "2.18.0--r42hdfd78af_11": "sha256:2b50f0c6c25b533186cceb7d10038320c85cff947060422afa0be57d8b9c3e99", "2.18.0--r43hdfd78af_12": "sha256:4808a42af832c54843c8c8b29f1f8cf9965fd5b378e023314b176361ef831125"}, "docker": "quay.io/biocontainers/bioconductor-rae230bprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rae230bprobe.
shpc-registry automated BioContainers addition for bioconductor-rae230bprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rae230bprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rae230bprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rae230bprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rae230bprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rae230bprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rae230bprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rae230bprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rae230bprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rae230bprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rae230bprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rae230bprobe

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