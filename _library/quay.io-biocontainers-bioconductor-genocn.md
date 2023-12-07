---
layout: container
name:  "quay.io/biocontainers/bioconductor-genocn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genocn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genocn/container.yaml"
updated_at: "2023-12-07 02:38:34.487307"
latest: "1.54.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genocn"

versions:
 - "1.46.0--r41hc0cfd56_2"
 - "1.50.0--r42hc0cfd56_0"
 - "1.50.0--r42ha9d7317_2"
 - "1.52.0--r43ha9d7317_0"
 - "1.54.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genocn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genocn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genocn", "latest": {"1.54.0--r43ha9d7317_0": "sha256:e8c4ecb0006a7857970ef9bfc4ac305708b2d6cf350b150fe2e7c7b5f7b4bcd5"}, "tags": {"1.46.0--r41hc0cfd56_2": "sha256:a11862dbf154c749fa48d814c27b8cb8150a2794771494e3bf00b5b56f4913c0", "1.50.0--r42hc0cfd56_0": "sha256:9e2901eba9664227f2cadeaeeed41603bcee15adf8ba7849602f664bc7edff33", "1.50.0--r42ha9d7317_2": "sha256:3d5be177fe4f6d732128c5dd302c3524a917a84426f4255028652c1d929b97e6", "1.52.0--r43ha9d7317_0": "sha256:09731492b466139a7c1c9b87832bdddcecebcc3e1f7bd55660177515cabca981", "1.54.0--r43ha9d7317_0": "sha256:e8c4ecb0006a7857970ef9bfc4ac305708b2d6cf350b150fe2e7c7b5f7b4bcd5"}, "docker": "quay.io/biocontainers/bioconductor-genocn"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genocn.
shpc-registry automated BioContainers addition for bioconductor-genocn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genocn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genocn:1.54.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genocn/1.54.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-genocn/1.54.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genocn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genocn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genocn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genocn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genocn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genocn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genocn

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