---
layout: container
name:  "quay.io/biocontainers/bioconductor-human650v3acrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human650v3acrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human650v3acrlmm/container.yaml"
updated_at: "2025-05-11 03:44:08.567022"
latest: "1.0.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-human650v3acrlmm"

versions:
 - "1.0.3--r41hdfd78af_9"
 - "1.0.3--r42hdfd78af_10"
 - "1.0.3--r43hdfd78af_11"
 - "1.0.3--r43hdfd78af_12"
 - "1.0.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-human650v3acrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human650v3acrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human650v3acrlmm", "latest": {"1.0.3--r44hdfd78af_13": "sha256:a21a485d91db60ec6f5ff31c823fa7ad9dc14ee99a8a1d310fd427ec31bacd90"}, "tags": {"1.0.3--r41hdfd78af_9": "sha256:bfc7f464044b57c539d5682c61c859963fe13e897c92e128b934f5773cc266da", "1.0.3--r42hdfd78af_10": "sha256:cd37ee24ec3994ca4d6a3e952289cf5b513c5a5c8d280c58c6e2c36fac90a0c2", "1.0.3--r43hdfd78af_11": "sha256:7cae0d7dfda3a1b13c1dc41710dcca8f529dbf7c9378afe6cbb68f6d7cf415b6", "1.0.3--r43hdfd78af_12": "sha256:6c03ec6caa8369082e5596c870e226f28d1c919f3a52d9de66338705a71717e3", "1.0.3--r44hdfd78af_13": "sha256:a21a485d91db60ec6f5ff31c823fa7ad9dc14ee99a8a1d310fd427ec31bacd90"}, "docker": "quay.io/biocontainers/bioconductor-human650v3acrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human650v3acrlmm.
shpc-registry automated BioContainers addition for bioconductor-human650v3acrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human650v3acrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human650v3acrlmm:1.0.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human650v3acrlmm/1.0.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-human650v3acrlmm/1.0.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human650v3acrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human650v3acrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human650v3acrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human650v3acrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human650v3acrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human650v3acrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-human650v3acrlmm

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