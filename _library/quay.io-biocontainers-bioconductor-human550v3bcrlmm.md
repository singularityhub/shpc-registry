---
layout: container
name:  "quay.io/biocontainers/bioconductor-human550v3bcrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human550v3bcrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human550v3bcrlmm/container.yaml"
updated_at: "2025-05-01 06:41:20.962444"
latest: "1.0.4--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-human550v3bcrlmm"

versions:
 - "1.0.4--r41hdfd78af_9"
 - "1.0.4--r42hdfd78af_10"
 - "1.0.4--r43hdfd78af_11"
 - "1.0.4--r43hdfd78af_12"
 - "1.0.4--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-human550v3bcrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human550v3bcrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human550v3bcrlmm", "latest": {"1.0.4--r44hdfd78af_13": "sha256:998c189e6064c2f73c8233b665eabdb4730ba4737ed6c5607188c79b7b683cde"}, "tags": {"1.0.4--r41hdfd78af_9": "sha256:dc5f97202024482ab8061af9e8425646f93e1598b8f7507f89c6fac389ece359", "1.0.4--r42hdfd78af_10": "sha256:1cb5918c78b1463c9962701c2bef3f7abfcd9e8d7dd1887e8545016c7ffd75b7", "1.0.4--r43hdfd78af_11": "sha256:1781528e32a12f42a81aaadb16743821e051ef16bdf86084d90e13b5e4d8c564", "1.0.4--r43hdfd78af_12": "sha256:0c0b45dc2b6befa52a31da725b97833fac38bf0db5e1e6166f963a8516be2253", "1.0.4--r44hdfd78af_13": "sha256:998c189e6064c2f73c8233b665eabdb4730ba4737ed6c5607188c79b7b683cde"}, "docker": "quay.io/biocontainers/bioconductor-human550v3bcrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human550v3bcrlmm.
shpc-registry automated BioContainers addition for bioconductor-human550v3bcrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human550v3bcrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human550v3bcrlmm:1.0.4--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human550v3bcrlmm/1.0.4--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-human550v3bcrlmm/1.0.4--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human550v3bcrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human550v3bcrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human550v3bcrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human550v3bcrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human550v3bcrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human550v3bcrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-human550v3bcrlmm

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