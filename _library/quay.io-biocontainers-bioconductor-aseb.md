---
layout: container
name:  "quay.io/biocontainers/bioconductor-aseb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aseb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aseb/container.yaml"
updated_at: "2023-10-05 02:47:17.238225"
latest: "1.44.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aseb"

versions:
 - "1.38.0--r41hc247a5b_2"
 - "1.42.0--r42hc247a5b_0"
 - "1.42.0--r42hf17093f_2"
 - "1.44.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aseb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aseb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aseb", "latest": {"1.44.0--r43hf17093f_0": "sha256:497cc36ca977523c202b4318c20dbca5adcda7e26fe73f154012962795b02aa6"}, "tags": {"1.38.0--r41hc247a5b_2": "sha256:f64337773f4b0abad28752dbe802bd072206344d04d30023d531297948246296", "1.42.0--r42hc247a5b_0": "sha256:fab4e1aaf729271b9639d721b9fa52fcf8e907a91deb81bbfa337dc15048f82c", "1.42.0--r42hf17093f_2": "sha256:f6d82460ef7d62a39e65e2ae7bcfe0f4f003f7f4e02c27f078a5062b56bb6938", "1.44.0--r43hf17093f_0": "sha256:497cc36ca977523c202b4318c20dbca5adcda7e26fe73f154012962795b02aa6"}, "docker": "quay.io/biocontainers/bioconductor-aseb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aseb.
shpc-registry automated BioContainers addition for bioconductor-aseb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aseb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aseb:1.44.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aseb/1.44.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-aseb/1.44.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aseb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aseb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aseb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aseb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aseb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aseb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-aseb

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