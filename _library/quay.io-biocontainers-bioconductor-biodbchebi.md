---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodbchebi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodbchebi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodbchebi/container.yaml"
updated_at: "2023-10-22 03:13:28.389560"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodbchebi"

versions:
 - "1.0.1--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biodbchebi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodbchebi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biodbchebi", "latest": {"1.6.0--r43hdfd78af_0": "sha256:9861abbad028fe5d2e5087ded917611d9f316a5140d0b73d424fc3049d4c911a"}, "tags": {"1.0.1--r41hdfd78af_0": "sha256:c4e03aa65059f1eadafbe06ad51884b80fc1a7997c45d4f5f5abf1269bca7004", "1.4.0--r42hdfd78af_0": "sha256:5f6b1d4dfa21f85258e350f92563f9e2233c5d66ff293f9f4e9bc8da190108ab", "1.6.0--r43hdfd78af_0": "sha256:9861abbad028fe5d2e5087ded917611d9f316a5140d0b73d424fc3049d4c911a"}, "docker": "quay.io/biocontainers/bioconductor-biodbchebi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodbchebi.
shpc-registry automated BioContainers addition for bioconductor-biodbchebi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbchebi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbchebi:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodbchebi/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biodbchebi/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodbchebi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbchebi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbchebi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodbchebi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodbchebi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodbchebi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodbchebi

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