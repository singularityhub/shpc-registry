---
layout: container
name:  "quay.io/biocontainers/bioconductor-signer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-signer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-signer/container.yaml"
updated_at: "2023-06-22 03:09:17.611485"
latest: "2.0.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-signer"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351hf484d3e_0"
 - "2.0.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "2.0.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-signer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-signer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-signer", "latest": {"2.0.0--r42hf17093f_1": "sha256:e821004e9c2f84932992fb16d03ffc6cc307be0430508aec1b9d49d2db9c0c3e"}, "tags": {"1.8.0--r351hf484d3e_0": "sha256:e3f9ad9dbb1aea0cce7a0f33aa052efe4232116e5298480dbe7e41720ccd02c1", "2.0.0--r42hc247a5b_0": "sha256:cf669403031d49b3d5c24104ad86f325671b9d793068763ef97e817f636a4aa2", "1.20.0--r41hc247a5b_2": "sha256:386145a6f1c72624dc7b2b890ecca9d0dfdf241d349f04535f6934b73e12378c", "1.18.0--r41h399db7b_0": "sha256:d90f539cd5106e51838a6ed4897078becd691d76ed90cd286107cd677e7d0da5", "1.16.0--r40h399db7b_1": "sha256:95761aa7ec37978f0959b2b20ef028175d6fae0756e9fc3d3f72167fc9891ce0", "1.14.0--r40h5f743cb_0": "sha256:d2c95b1f48f81cbc7d9cebe698a091fc6c7c31d750812eacb79b43dc2092e43f", "2.0.0--r42hf17093f_1": "sha256:e821004e9c2f84932992fb16d03ffc6cc307be0430508aec1b9d49d2db9c0c3e"}, "docker": "quay.io/biocontainers/bioconductor-signer", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-signer.
shpc-registry automated BioContainers addition for bioconductor-signer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-signer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-signer:2.0.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-signer/2.0.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-signer/2.0.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-signer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-signer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-signer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-signer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-signer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-signer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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