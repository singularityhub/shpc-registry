---
layout: container
name:  "quay.io/biocontainers/bioconductor-dyebiasexamples"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dyebiasexamples/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dyebiasexamples/container.yaml"
updated_at: "2024-07-23 03:16:12.481259"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dyebiasexamples"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dyebiasexamples"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dyebiasexamples", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dyebiasexamples", "latest": {"1.42.0--r43hdfd78af_0": "sha256:7a3f490f60f9c6dac59bf9747b707ea44215bbb0af4ba39f968df03dbfc38b5d"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:43202517e6a299942e2f16e27b56b661423224676fe8d0573ea1553fa126f7bf", "1.38.0--r42hdfd78af_0": "sha256:dd8a63e0299dc1b749caa6492046c50048169b970cd6a649391cb2e2d5937405", "1.40.0--r43hdfd78af_0": "sha256:3b1bd9dd8acca2896775e5b0c69a21bad40916f87a3d60d58aecd53642c47a15", "1.42.0--r43hdfd78af_0": "sha256:7a3f490f60f9c6dac59bf9747b707ea44215bbb0af4ba39f968df03dbfc38b5d"}, "docker": "quay.io/biocontainers/bioconductor-dyebiasexamples"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dyebiasexamples.
shpc-registry automated BioContainers addition for bioconductor-dyebiasexamples
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dyebiasexamples
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dyebiasexamples:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dyebiasexamples/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dyebiasexamples/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dyebiasexamples-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dyebiasexamples-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dyebiasexamples-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dyebiasexamples-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dyebiasexamples-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dyebiasexamples-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dyebiasexamples

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