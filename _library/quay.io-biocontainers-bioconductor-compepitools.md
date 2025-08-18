---
layout: container
name:  "quay.io/biocontainers/bioconductor-compepitools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-compepitools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-compepitools/container.yaml"
updated_at: "2025-08-18 04:15:32.766614"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-compepitools"

versions:
 - "1.27.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.1--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-compepitools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-compepitools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-compepitools", "latest": {"1.40.0--r44hdfd78af_0": "sha256:afc42a6c3b00579cec24fd031a28f0c03ca18a6b81ef56472b68408b3a817f7a"}, "tags": {"1.27.0--r41hdfd78af_0": "sha256:041c0c2d3d617c665ef4c966f8b9b9bce12de7262dddc32be531771e45dd064b", "1.32.0--r42hdfd78af_0": "sha256:66430ff39ae16db3da94daf715cc99d20414d7dac4a58ce1694a68fac78f9cce", "1.34.1--r43hdfd78af_0": "sha256:4fffec32598367f10d10c66b20b712ad1b89723d55d710954543900f07845be7", "1.36.0--r43hdfd78af_0": "sha256:b4c0a8590ffd13c030a38c50504601cc9983d03887fc1a1f8bf65896c9f3542a", "1.40.0--r44hdfd78af_0": "sha256:afc42a6c3b00579cec24fd031a28f0c03ca18a6b81ef56472b68408b3a817f7a"}, "docker": "quay.io/biocontainers/bioconductor-compepitools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-compepitools.
shpc-registry automated BioContainers addition for bioconductor-compepitools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-compepitools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-compepitools:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-compepitools/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-compepitools/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-compepitools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compepitools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compepitools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-compepitools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-compepitools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-compepitools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-compepitools

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