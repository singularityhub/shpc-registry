---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowcore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowcore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowcore/container.yaml"
updated_at: "2024-03-21 03:58:13.759392"
latest: "2.14.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowcore"

versions:
 - "2.6.0--r41hc247a5b_2"
 - "2.10.0--r42hc247a5b_0"
 - "2.10.0--r42hf17093f_1"
 - "2.12.0--r43hf17093f_0"
 - "2.14.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowcore"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowcore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowcore", "latest": {"2.14.0--r43hf17093f_0": "sha256:ce5490a2943aea9db1b971df77e88bae7675bef13909134dfb7b9fa235bfc285"}, "tags": {"2.6.0--r41hc247a5b_2": "sha256:38f322759f3d3c90238c8ee8bbbc454254595f8af1672b946a994d17e99d436d", "2.10.0--r42hc247a5b_0": "sha256:a3dce66c6c5087a0cf27e3f1dd7fbb31d81b72a6f0d51491cfd1f20e119325ad", "2.10.0--r42hf17093f_1": "sha256:d24178a7f9718eba2de147c7c53fbf58be77292cfe647199b34ad5055fb66e49", "2.12.0--r43hf17093f_0": "sha256:b4e66a57d7c275e89f6558543bddf678f243ab75ec1a2396cada4c5b175313c9", "2.14.0--r43hf17093f_0": "sha256:ce5490a2943aea9db1b971df77e88bae7675bef13909134dfb7b9fa235bfc285"}, "docker": "quay.io/biocontainers/bioconductor-flowcore"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowcore.
shpc-registry automated BioContainers addition for bioconductor-flowcore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowcore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowcore:2.14.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowcore/2.14.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-flowcore/2.14.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowcore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowcore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowcore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowcore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowcore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowcore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowcore

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