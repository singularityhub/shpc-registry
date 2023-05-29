---
layout: container
name:  "quay.io/biocontainers/bioconductor-quasr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-quasr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-quasr/container.yaml"
updated_at: "2023-05-29 04:27:17.161096"
latest: "1.38.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-quasr"

versions:
 - "1.34.0--r41hc247a5b_2"
 - "1.38.0--r42hc247a5b_0"
 - "1.38.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-quasr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-quasr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-quasr", "latest": {"1.38.0--r42hf17093f_1": "sha256:9959c1cd46ed0a704cb5941d5dae3a7156ef134a981889cea33287b93ce9db3c"}, "tags": {"1.34.0--r41hc247a5b_2": "sha256:f0a06ec8246db558b45cfd3dd3ca8e329620ff4edc5c1a32b5da1ad4c2a7dcce", "1.38.0--r42hc247a5b_0": "sha256:360caa19c57247149be4105348e087169d95eb5b7968d10deac6d810826da7c9", "1.38.0--r42hf17093f_1": "sha256:9959c1cd46ed0a704cb5941d5dae3a7156ef134a981889cea33287b93ce9db3c"}, "docker": "quay.io/biocontainers/bioconductor-quasr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-quasr.
shpc-registry automated BioContainers addition for bioconductor-quasr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-quasr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-quasr:1.38.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-quasr/1.38.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-quasr/1.38.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-quasr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quasr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quasr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-quasr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-quasr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-quasr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-quasr

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