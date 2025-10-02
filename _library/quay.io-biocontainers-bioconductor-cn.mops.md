---
layout: container
name:  "quay.io/biocontainers/bioconductor-cn.mops"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cn.mops/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cn.mops/container.yaml"
updated_at: "2025-10-02 03:33:03.186276"
latest: "1.52.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-cn.mops"

versions:
 - "1.40.0--r41hc247a5b_2"
 - "1.44.0--r42hc247a5b_0"
 - "1.44.0--r42hf17093f_1"
 - "1.46.0--r43hf17093f_0"
 - "1.48.0--r43hf17093f_0"
 - "1.52.0--r44he5774e6_0"
 - "1.52.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-cn.mops"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cn.mops", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cn.mops", "latest": {"1.52.0--r44he5774e6_1": "sha256:797362ee740b84183f34edc4890977916a154056a86511fe82cc218b5f7c82fb"}, "tags": {"1.40.0--r41hc247a5b_2": "sha256:777a5d495827b8662cfdeebae569fdad085c6a821ca9dd204c67e8370ddd7230", "1.44.0--r42hc247a5b_0": "sha256:099b0d673675d1c99e2c026af289a232843bdb4c3cdb765dd3afe5d035876374", "1.44.0--r42hf17093f_1": "sha256:a8e809283293a94be2100cf7a89b8b46fc0012cc41a156be2c36cf8d46af3894", "1.46.0--r43hf17093f_0": "sha256:2db0c91a520fb85adb5883691d0c192bc0885994923ad8b7ceb68e521dedcf82", "1.48.0--r43hf17093f_0": "sha256:9c76e492de84dc51db3cd08aa9c095093646f116288cf08489ff94c58460708d", "1.52.0--r44he5774e6_0": "sha256:1c0cdad1e5889fe555039da8f58a166d6b4687279cc575e3f0fb02d90ab757a4", "1.52.0--r44he5774e6_1": "sha256:797362ee740b84183f34edc4890977916a154056a86511fe82cc218b5f7c82fb"}, "docker": "quay.io/biocontainers/bioconductor-cn.mops"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cn.mops.
shpc-registry automated BioContainers addition for bioconductor-cn.mops
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cn.mops
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cn.mops:1.52.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cn.mops/1.52.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-cn.mops/1.52.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cn.mops-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cn.mops-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cn.mops-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cn.mops-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cn.mops-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cn.mops-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cn.mops

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