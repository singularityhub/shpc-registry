---
layout: container
name:  "quay.io/biocontainers/bioconductor-rlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rlmm/container.yaml"
updated_at: "2025-05-18 03:33:19.796407"
latest: "1.68.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rlmm"

versions:
 - "1.56.0--r41hdfd78af_0"
 - "1.60.0--r42hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.64.0--r43hdfd78af_0"
 - "1.68.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rlmm", "latest": {"1.68.0--r44hdfd78af_0": "sha256:09fdcbc841c8480feb942a90fd68eafe7cddf2702102740e5b229fac7a0fde45"}, "tags": {"1.56.0--r41hdfd78af_0": "sha256:ab1bcbcbb13f1e33f45e37911919aa0953e3d09361ee99301424760fb549009e", "1.60.0--r42hdfd78af_0": "sha256:510d460dda1dc25483cd8821b780637dde64ee9b71363a9e9ff7f0101b8d1eba", "1.62.0--r43hdfd78af_0": "sha256:f07022a9c6fdbededa6ffc6a554c9c9cbea8ea829b359e27d83c35a5faedd129", "1.64.0--r43hdfd78af_0": "sha256:1d26eb374e378e47ffec2c57f874a8d74fd3de594c25930dec90f72fc5b92d0d", "1.68.0--r44hdfd78af_0": "sha256:09fdcbc841c8480feb942a90fd68eafe7cddf2702102740e5b229fac7a0fde45"}, "docker": "quay.io/biocontainers/bioconductor-rlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rlmm.
shpc-registry automated BioContainers addition for bioconductor-rlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rlmm:1.68.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rlmm/1.68.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rlmm/1.68.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rlmm

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