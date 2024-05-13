---
layout: container
name:  "quay.io/biocontainers/bioconductor-ancombc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ancombc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ancombc/container.yaml"
updated_at: "2024-05-13 03:01:55.601629"
latest: "2.4.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ancombc"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "2.0.1--r42hdfd78af_0"
 - "2.2.0--r43hdfd78af_0"
 - "2.4.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ancombc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ancombc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ancombc", "latest": {"2.4.0--r43hdfd78af_0": "sha256:ff823a0fe77ae7d68910b51dbcfadf4e91d59dae013616c5fb98ea11c0e05f7a"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:5bd373b2bd5ddd730d45b05e188f912ec43bf8dd993cc08ff3ec10328d0a990f", "2.0.1--r42hdfd78af_0": "sha256:15d8d1398cc6d6d966c81e498e4956dbb994541e3141bf6c0d43117810981caa", "2.2.0--r43hdfd78af_0": "sha256:2090bcd06a37bc289f89cea413dcfb3f4c1f3e6c2f48c1c3b332f93a1107c059", "2.4.0--r43hdfd78af_0": "sha256:ff823a0fe77ae7d68910b51dbcfadf4e91d59dae013616c5fb98ea11c0e05f7a"}, "docker": "quay.io/biocontainers/bioconductor-ancombc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ancombc.
shpc-registry automated BioContainers addition for bioconductor-ancombc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ancombc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ancombc:2.4.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ancombc/2.4.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ancombc/2.4.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ancombc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ancombc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ancombc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ancombc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ancombc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ancombc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ancombc

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