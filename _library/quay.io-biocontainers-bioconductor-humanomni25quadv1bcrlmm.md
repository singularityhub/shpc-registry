---
layout: container
name:  "quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm/container.yaml"
updated_at: "2023-05-29 04:15:52.907625"
latest: "1.0.2--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-humanomni25quadv1bcrlmm"

versions:
 - "1.0.2--r41hdfd78af_9"
 - "1.0.2--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-humanomni25quadv1bcrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-humanomni25quadv1bcrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-humanomni25quadv1bcrlmm", "latest": {"1.0.2--r42hdfd78af_10": "sha256:80db4110248c92584cd38cdf6fabb61cce82fc6a5c34827d35b0d30761258896"}, "tags": {"1.0.2--r41hdfd78af_9": "sha256:b66dabb91413048c9d25b2a58bf02ea07bd2764b3804c11d1375da4fe5c8cdef", "1.0.2--r42hdfd78af_10": "sha256:80db4110248c92584cd38cdf6fabb61cce82fc6a5c34827d35b0d30761258896"}, "docker": "quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm.
shpc-registry automated BioContainers addition for bioconductor-humanomni25quadv1bcrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm:1.0.2--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm/1.0.2--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-humanomni25quadv1bcrlmm/1.0.2--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-humanomni25quadv1bcrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanomni25quadv1bcrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanomni25quadv1bcrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-humanomni25quadv1bcrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-humanomni25quadv1bcrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-humanomni25quadv1bcrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-humanomni25quadv1bcrlmm

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