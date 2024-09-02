---
layout: container
name:  "quay.io/biocontainers/bioconductor-nxtirfcore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nxtirfcore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nxtirfcore/container.yaml"
updated_at: "2024-09-02 04:36:15.167813"
latest: "1.6.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nxtirfcore"

versions:
 - "1.0.0--r41hc247a5b_2"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nxtirfcore"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nxtirfcore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nxtirfcore", "latest": {"1.6.0--r43hf17093f_0": "sha256:fe028b19fb934fca47ba8a2893de9bfbdf83ab44ce360ef9bdf661f6a3d3714c"}, "tags": {"1.0.0--r41hc247a5b_2": "sha256:6be7184ed850e5620b02aec271d5f81e627ecc41e08227178f9d7e064ea8ac11", "1.4.0--r42hc247a5b_0": "sha256:70cea63d31cd26dad4192fb577b9acd502715a4b9ac987a56bd2ce98f6a297e5", "1.4.0--r42hf17093f_1": "sha256:aff4ff7d5fd5ae21311e87bcde11f1d9c6c51a882f14a66239296866bd64c941", "1.6.0--r43hf17093f_0": "sha256:fe028b19fb934fca47ba8a2893de9bfbdf83ab44ce360ef9bdf661f6a3d3714c"}, "docker": "quay.io/biocontainers/bioconductor-nxtirfcore"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nxtirfcore.
shpc-registry automated BioContainers addition for bioconductor-nxtirfcore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nxtirfcore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nxtirfcore:1.6.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nxtirfcore/1.6.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-nxtirfcore/1.6.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nxtirfcore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nxtirfcore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nxtirfcore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nxtirfcore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nxtirfcore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nxtirfcore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nxtirfcore

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