---
layout: container
name:  "quay.io/biocontainers/bioconductor-bicare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bicare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bicare/container.yaml"
updated_at: "2023-12-10 02:44:42.458604"
latest: "1.58.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bicare"

versions:
 - "1.52.0--r41hc0cfd56_2"
 - "1.56.0--r42hc0cfd56_0"
 - "1.56.0--r42ha9d7317_1"
 - "1.58.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bicare"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bicare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bicare", "latest": {"1.58.0--r43ha9d7317_0": "sha256:fe80be77fd11b9bf5dae79a0ce2f82e1664a70eaaa123e82de32bf0ce73c2131"}, "tags": {"1.52.0--r41hc0cfd56_2": "sha256:075cec8c82a1be23aa37b98732ac6b11077735b349454c30f31a951097cd4f29", "1.56.0--r42hc0cfd56_0": "sha256:436960b67e3c56565d3282c204afc442bd80d3bfda59aabb55187c23ae1fb571", "1.56.0--r42ha9d7317_1": "sha256:8fd875868f363ecc91d7611f38a44b6b96b665dccb43cc486ce7ac43f9b74736", "1.58.0--r43ha9d7317_0": "sha256:fe80be77fd11b9bf5dae79a0ce2f82e1664a70eaaa123e82de32bf0ce73c2131"}, "docker": "quay.io/biocontainers/bioconductor-bicare"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bicare.
shpc-registry automated BioContainers addition for bioconductor-bicare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bicare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bicare:1.58.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bicare/1.58.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-bicare/1.58.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bicare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bicare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bicare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bicare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bicare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bicare-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bicare

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