---
layout: container
name:  "quay.io/biocontainers/bioconductor-bayesspace"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bayesspace/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bayesspace/container.yaml"
updated_at: "2025-10-09 04:29:29.555217"
latest: "1.12.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bayesspace"
aliases:
 - "xgboost"
 - "glpsol"
versions:
 - "1.4.1--r41hc247a5b_1"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.12.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bayesspace"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bayesspace", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bayesspace", "latest": {"1.12.0--r43hf17093f_0": "sha256:2a6ed26ee316e224cfd7a93f631c4595a4299bbc56ab425311735feaa9be4e5b"}, "tags": {"1.4.1--r41hc247a5b_1": "sha256:741b190033024c02a7fa75e7bbda7e4f22cf47c097d2d843a47ec66030931327", "1.8.0--r42hc247a5b_0": "sha256:d6ebc9ac153906cb540bec174cd9a68ee3e196a4658c4fb3478940e165ee092c", "1.8.0--r42hf17093f_1": "sha256:a4d50c604efe30267dfd45173159c33781163a44920682be099b3942bde4959e", "1.12.0--r43hf17093f_0": "sha256:2a6ed26ee316e224cfd7a93f631c4595a4299bbc56ab425311735feaa9be4e5b"}, "docker": "quay.io/biocontainers/bioconductor-bayesspace", "aliases": {"xgboost": "/usr/local/bin/xgboost", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bayesspace.
shpc-registry automated BioContainers addition for bioconductor-bayesspace
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bayesspace
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bayesspace:1.12.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bayesspace/1.12.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-bayesspace/1.12.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bayesspace-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bayesspace-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bayesspace-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bayesspace-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bayesspace-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bayesspace-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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