---
layout: container
name:  "quay.io/biocontainers/bioconductor-drosgenome1cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drosgenome1cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drosgenome1cdf/container.yaml"
updated_at: "2024-03-18 02:55:34.594932"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-drosgenome1cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-drosgenome1cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drosgenome1cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drosgenome1cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:9252113f585e9b2e5eb6e3f041e97cd70f1c0ea80d7137260c8c44bcfb17f375"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:700058eb6f84fedc88d16c46cef6b88aee24fabe7d25e3e90d6c5f74b28c8851", "2.18.0--r42hdfd78af_10": "sha256:d7b72ce0ccfb3216cd975c07d755dab8f0c0d113728f5664d6edf0fbfba4e72c", "2.18.0--r43hdfd78af_11": "sha256:d0266e01ac2a3e4ff18611ffb0436ebe7f63efa5693e0ed1d408e904ca4b6be1", "2.18.0--r43hdfd78af_12": "sha256:9252113f585e9b2e5eb6e3f041e97cd70f1c0ea80d7137260c8c44bcfb17f375"}, "docker": "quay.io/biocontainers/bioconductor-drosgenome1cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drosgenome1cdf.
shpc-registry automated BioContainers addition for bioconductor-drosgenome1cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drosgenome1cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drosgenome1cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drosgenome1cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-drosgenome1cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drosgenome1cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosgenome1cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosgenome1cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drosgenome1cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drosgenome1cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drosgenome1cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-drosgenome1cdf

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