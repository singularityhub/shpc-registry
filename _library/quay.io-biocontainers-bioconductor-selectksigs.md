---
layout: container
name:  "quay.io/biocontainers/bioconductor-selectksigs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-selectksigs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-selectksigs/container.yaml"
updated_at: "2024-02-09 03:26:40.414179"
latest: "1.14.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-selectksigs"
aliases:
 - "jags"
versions:
 - "1.6.0--r41hc247a5b_2"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_1"
 - "1.12.0--r43hf17093f_0"
 - "1.14.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-selectksigs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-selectksigs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-selectksigs", "latest": {"1.14.0--r43hf17093f_0": "sha256:1c2f8fc9ceb96a0da619b554a0e287d3c23e0e738ae84f7d66fd45ea07ababf8"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:fd843d1451d4dad93a6f94f9933c1c3fe05cda7da5a8ed20cff3a497e1c65eec", "1.10.0--r42hc247a5b_0": "sha256:d692b13eb51225e118e6c298a2028f14f71b63b650c37b0c2b6da136740e00b0", "1.10.0--r42hf17093f_1": "sha256:9e37e1d1d2870c697baf07bbde721048f1aa625daca03a85cb6f3591eb681159", "1.12.0--r43hf17093f_0": "sha256:fd97d5172442983df180cc22b58a70d4b3a85227ce899aeb7d400cf72a780f1a", "1.14.0--r43hf17093f_0": "sha256:1c2f8fc9ceb96a0da619b554a0e287d3c23e0e738ae84f7d66fd45ea07ababf8"}, "docker": "quay.io/biocontainers/bioconductor-selectksigs", "aliases": {"jags": "/usr/local/bin/jags"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-selectksigs.
shpc-registry automated BioContainers addition for bioconductor-selectksigs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-selectksigs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-selectksigs:1.14.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-selectksigs/1.14.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-selectksigs/1.14.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-selectksigs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-selectksigs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-selectksigs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-selectksigs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-selectksigs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-selectksigs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jags

```bash
$ singularity exec <container> /usr/local/bin/jags
$ podman run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
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