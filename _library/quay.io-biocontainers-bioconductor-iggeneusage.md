---
layout: container
name:  "quay.io/biocontainers/bioconductor-iggeneusage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iggeneusage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iggeneusage/container.yaml"
updated_at: "2025-11-14 03:59:39.414578"
latest: "1.20.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-iggeneusage"

versions:
 - "1.8.0--r41hc247a5b_2"
 - "1.12.0--r42hc247a5b_0"
 - "1.12.0--r42hf17093f_1"
 - "1.14.0--r43hf17093f_0"
 - "1.16.0--r43hf17093f_0"
 - "1.20.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-iggeneusage"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iggeneusage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iggeneusage", "latest": {"1.20.0--r44he5774e6_0": "sha256:ff31271148230a7b6bfa41626f028978466855c211f3c8ea63f400548a63892d"}, "tags": {"1.8.0--r41hc247a5b_2": "sha256:61f76c2ff410f5efb8debdd8b6a5fadf8bc816d684d337fa336dd556ce7dc9b9", "1.12.0--r42hc247a5b_0": "sha256:30cfd8c5c538d84ed7c6f40b635ae3f449bde0cb75d7862793cbd337a7d46aff", "1.12.0--r42hf17093f_1": "sha256:3b81ba08e30026d04666c85cba0a8717c9f34d6762c6ef4df8bb1184304250e2", "1.14.0--r43hf17093f_0": "sha256:06bef08ef085dc3198cd36888540e00f0c8cdddcdbd9cc0259038e84ff43b4cc", "1.16.0--r43hf17093f_0": "sha256:8ebf43de0b6aace69ca05661b0b78e20b0966fe18bd42044f8550b16f77e1601", "1.20.0--r44he5774e6_0": "sha256:ff31271148230a7b6bfa41626f028978466855c211f3c8ea63f400548a63892d"}, "docker": "quay.io/biocontainers/bioconductor-iggeneusage"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iggeneusage.
shpc-registry automated BioContainers addition for bioconductor-iggeneusage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iggeneusage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iggeneusage:1.20.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iggeneusage/1.20.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-iggeneusage/1.20.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iggeneusage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iggeneusage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iggeneusage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iggeneusage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iggeneusage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iggeneusage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-iggeneusage

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