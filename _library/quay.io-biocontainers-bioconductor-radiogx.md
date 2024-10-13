---
layout: container
name:  "quay.io/biocontainers/bioconductor-radiogx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-radiogx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-radiogx/container.yaml"
updated_at: "2024-10-13 10:39:07.094347"
latest: "2.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-radiogx"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "2.2.0--r42hdfd78af_0"
 - "2.4.0--r43hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-radiogx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-radiogx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-radiogx", "latest": {"2.6.0--r43hdfd78af_0": "sha256:dbc8ef57c8204ac2c6f44ad41e3eab034458001593b1d1b5be61b48f9b453a3a"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:acaeceeb1d430de49232c80700f89832dff4f94b9b1545bdd91c532878f9f0d7", "2.2.0--r42hdfd78af_0": "sha256:e78c8b1d3f66ceb7015977f899ad34b7e7534a93da1913d2d5faae84708ec2f0", "2.4.0--r43hdfd78af_0": "sha256:215f98a3ca5cd0094e1314c9d2433664c42c1bbab59745410eebad199301d25e", "2.6.0--r43hdfd78af_0": "sha256:dbc8ef57c8204ac2c6f44ad41e3eab034458001593b1d1b5be61b48f9b453a3a"}, "docker": "quay.io/biocontainers/bioconductor-radiogx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-radiogx.
shpc-registry automated BioContainers addition for bioconductor-radiogx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-radiogx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-radiogx:2.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-radiogx/2.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-radiogx/2.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-radiogx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-radiogx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-radiogx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-radiogx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-radiogx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-radiogx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-radiogx

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