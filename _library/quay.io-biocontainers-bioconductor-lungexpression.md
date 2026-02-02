---
layout: container
name:  "quay.io/biocontainers/bioconductor-lungexpression"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lungexpression/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lungexpression/container.yaml"
updated_at: "2026-02-02 12:45:14.976694"
latest: "0.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lungexpression"

versions:
 - "0.32.1--r41hdfd78af_1"
 - "0.36.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
 - "0.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lungexpression"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lungexpression", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lungexpression", "latest": {"0.44.0--r44hdfd78af_0": "sha256:e634ecfaa9b113ce9dab70484bec9a277c3276cbdd6e379fb22fe1013ad9675a"}, "tags": {"0.32.1--r41hdfd78af_1": "sha256:5d361f045d1d04ab29f199588119ec3834a804edf49412560567976365e403d5", "0.36.0--r42hdfd78af_0": "sha256:5a8c23fcd537a14cf7c845f69d5b88b5a65f775e3c904f75274bfa23d7143f27", "0.38.0--r43hdfd78af_0": "sha256:48d0f8cb895f2e3d442da773ebe9cd1670b3eeed53cce2ac9283436cd539bddb", "0.40.0--r43hdfd78af_0": "sha256:74aa15549fca85b363ddeef64461128cb365a21df219a54b5989ad710be62343", "0.44.0--r44hdfd78af_0": "sha256:e634ecfaa9b113ce9dab70484bec9a277c3276cbdd6e379fb22fe1013ad9675a"}, "docker": "quay.io/biocontainers/bioconductor-lungexpression"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lungexpression.
shpc-registry automated BioContainers addition for bioconductor-lungexpression
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lungexpression
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lungexpression:0.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lungexpression/0.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lungexpression/0.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lungexpression-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lungexpression-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lungexpression-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lungexpression-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lungexpression-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lungexpression-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lungexpression

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