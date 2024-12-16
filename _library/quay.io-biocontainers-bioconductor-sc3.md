---
layout: container
name:  "quay.io/biocontainers/bioconductor-sc3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sc3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sc3/container.yaml"
updated_at: "2024-12-16 03:55:55.683185"
latest: "1.30.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sc3"

versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.16.0--r40h5f743cb_0"
 - "1.14.0--r36he1b5a44_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.3--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sc3"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sc3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sc3", "latest": {"1.30.0--r43hf17093f_0": "sha256:9745f73f184e303ffa5146e0bd51e49510ac09cea216fc3c1b7a7a83bb1ff014"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:40020cd9ccb21371b170c25abd47776733865bd131e2d3c317932d93a8adf50b", "1.22.0--r41hc247a5b_2": "sha256:4bb50eaefc15a90c33b2a65ee0d8636d63897a7032db8bac7a8496e68422fb55", "1.20.0--r41h399db7b_0": "sha256:fd0884ecbb56a93615070033e6851d9f8bbd164fff7020b424e1ccbbb59ceb10", "1.18.0--r40h399db7b_1": "sha256:703e12fb4561f8c614fcd106624f06ababf386fd12284553d68025844f42eac6", "1.16.0--r40h5f743cb_0": "sha256:2f7756554fa69a521f918b4f0b532bf91a79562a148c5ee5458a48a5d3c3f771", "1.14.0--r36he1b5a44_0": "sha256:5aeb07a0b3708a359170ff60568ed5aed1027811738749961970c0166ed3bbe7", "1.26.0--r42hc247a5b_0": "sha256:987f977515ba7c58418d2fc3250db148f3a784f9fe9fd88cd983680199fa106a", "1.26.0--r42hf17093f_1": "sha256:cc00dcfa40cd5e124910972fda4dd9a0a9799ac9a92a099bacccc5313e753a54", "1.28.3--r43hf17093f_0": "sha256:456229a8dcbe7220b8fbd7f2f258fffaabd0fa0d4f087d457bae113b68cac009", "1.30.0--r43hf17093f_0": "sha256:9745f73f184e303ffa5146e0bd51e49510ac09cea216fc3c1b7a7a83bb1ff014"}, "docker": "quay.io/biocontainers/bioconductor-sc3"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sc3.
shpc-registry automated BioContainers addition for bioconductor-sc3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sc3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sc3:1.30.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sc3/1.30.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-sc3/1.30.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sc3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sc3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sc3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sc3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sc3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sc3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sc3

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