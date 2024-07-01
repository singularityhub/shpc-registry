---
layout: container
name:  "quay.io/biocontainers/bioconductor-lionessr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lionessr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lionessr/container.yaml"
updated_at: "2024-07-01 04:21:02.583598"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lionessr"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lionessr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lionessr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lionessr", "latest": {"1.16.0--r43hdfd78af_0": "sha256:71abbf9e773b9e73c13e595cb23d1952aa5765ba44e39a72251e175503e41b80"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:61130e02720d338c5a492e6562931de28f4720006a91dcbe05d9f11956ff4426", "1.12.0--r42hdfd78af_0": "sha256:ba5e84ae5af4e3b639ee3fe84414576c9ec9f160423b340dcecb4f9378b8132c", "1.14.0--r43hdfd78af_0": "sha256:04d14b12e94e9b6b538c8e3688623ddebf7a0b4c3b71060c9866528279b474c2", "1.16.0--r43hdfd78af_0": "sha256:71abbf9e773b9e73c13e595cb23d1952aa5765ba44e39a72251e175503e41b80"}, "docker": "quay.io/biocontainers/bioconductor-lionessr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lionessr.
shpc-registry automated BioContainers addition for bioconductor-lionessr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lionessr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lionessr:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lionessr/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lionessr/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lionessr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lionessr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lionessr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lionessr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lionessr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lionessr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lionessr

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