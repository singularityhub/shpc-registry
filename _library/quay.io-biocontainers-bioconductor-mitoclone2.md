---
layout: container
name:  "quay.io/biocontainers/bioconductor-mitoclone2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mitoclone2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mitoclone2/container.yaml"
updated_at: "2024-11-03 03:34:55.770011"
latest: "1.8.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mitoclone2"

versions:
 - "1.0.0--r41hc247a5b_2"
 - "1.4.0--r42hc247a5b_0"
 - "1.4.0--r42hf17093f_1"
 - "1.6.0--r43hf17093f_0"
 - "1.8.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mitoclone2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mitoclone2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mitoclone2", "latest": {"1.8.1--r43hf17093f_0": "sha256:e85cd791a68453208943002f50efbb2f1f33ed8634e66fabdbdea82b91ea4607"}, "tags": {"1.0.0--r41hc247a5b_2": "sha256:bab002f7303685066a2f0cca57c4240a86fed25576ba0479b6e910b68a67afe0", "1.4.0--r42hc247a5b_0": "sha256:af37a807fa2a0e4ab1da9e91cfdb9f8696ef3702c300bdbc0593f159b26298ae", "1.4.0--r42hf17093f_1": "sha256:8045c79caeebe01297518d7623d5f37367c71d8ee5592dbcd9a83aa5b2e69794", "1.6.0--r43hf17093f_0": "sha256:411f4ef1f35a5f37820fe149c4dc3f0fc3e325b41cc7207af03599ce8636ae98", "1.8.1--r43hf17093f_0": "sha256:e85cd791a68453208943002f50efbb2f1f33ed8634e66fabdbdea82b91ea4607"}, "docker": "quay.io/biocontainers/bioconductor-mitoclone2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mitoclone2.
shpc-registry automated BioContainers addition for bioconductor-mitoclone2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mitoclone2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mitoclone2:1.8.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mitoclone2/1.8.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-mitoclone2/1.8.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mitoclone2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mitoclone2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mitoclone2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mitoclone2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mitoclone2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mitoclone2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mitoclone2

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