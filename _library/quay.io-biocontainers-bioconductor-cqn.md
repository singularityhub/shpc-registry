---
layout: container
name:  "quay.io/biocontainers/bioconductor-cqn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cqn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cqn/container.yaml"
updated_at: "2025-05-19 03:51:56.533942"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cqn"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cqn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cqn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cqn", "latest": {"1.52.0--r44hdfd78af_0": "sha256:f5e16c24f7d3c692935a9971eeb09e4a8e1af4bcc9ea2fbc15687eac31f1ee37"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:e304ca5915d0112ffd5ccf22e201b585572bbe7e1cc970269e91a909a97af146", "1.44.0--r42hdfd78af_0": "sha256:9b49f56ea679de64e8642646e1d6f06829501644a095a2cf4170e7c7aaff0170", "1.46.0--r43hdfd78af_0": "sha256:6eca3c37b333ac0a90b522dbb7a3a4d587d3b3cbab837b408f6810588d4b3e04", "1.48.0--r43hdfd78af_0": "sha256:4f4ba2189477ca7492b8770ff1b8cfd24dce07e4fd280352c041dd7df2ca9637", "1.52.0--r44hdfd78af_0": "sha256:f5e16c24f7d3c692935a9971eeb09e4a8e1af4bcc9ea2fbc15687eac31f1ee37"}, "docker": "quay.io/biocontainers/bioconductor-cqn"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cqn.
shpc-registry automated BioContainers addition for bioconductor-cqn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cqn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cqn:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cqn/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cqn/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cqn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cqn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cqn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cqn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cqn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cqn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cqn

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