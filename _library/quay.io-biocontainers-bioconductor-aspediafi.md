---
layout: container
name:  "quay.io/biocontainers/bioconductor-aspediafi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aspediafi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aspediafi/container.yaml"
updated_at: "2025-10-27 03:35:53.524774"
latest: "1.11.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aspediafi"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.11.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aspediafi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aspediafi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aspediafi", "latest": {"1.11.0--r42hdfd78af_0": "sha256:914835450e8fefebdce3ce69e4fc06b5b680ff0f61865af4261b8bf209675925"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:e02c324a403bb0529478401404a64a57bd777a37de20a039c7499ee5a254fa00", "1.11.0--r42hdfd78af_0": "sha256:914835450e8fefebdce3ce69e4fc06b5b680ff0f61865af4261b8bf209675925"}, "docker": "quay.io/biocontainers/bioconductor-aspediafi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aspediafi.
shpc-registry automated BioContainers addition for bioconductor-aspediafi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aspediafi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aspediafi:1.11.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aspediafi/1.11.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-aspediafi/1.11.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aspediafi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aspediafi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aspediafi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aspediafi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aspediafi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aspediafi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-aspediafi

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