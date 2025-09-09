---
layout: container
name:  "quay.io/biocontainers/bioconductor-samspectral"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-samspectral/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-samspectral/container.yaml"
updated_at: "2025-09-09 03:06:45.179973"
latest: "1.60.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-samspectral"

versions:
 - "1.48.0--r41hc0cfd56_2"
 - "1.52.0--r42hc0cfd56_0"
 - "1.52.0--r42ha9d7317_1"
 - "1.54.0--r43ha9d7317_0"
 - "1.56.0--r43ha9d7317_1"
 - "1.60.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-samspectral"
config: {"url": "https://biocontainers.pro/tools/bioconductor-samspectral", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-samspectral", "latest": {"1.60.0--r44h3df3fcb_0": "sha256:5a51ed62dced35bbe51ef4d8e8568b1adf56480887f974b384f2997a8dd59b19"}, "tags": {"1.48.0--r41hc0cfd56_2": "sha256:f4fd858ba58961ae7585211a5d11f2a1aa493d1252b41b73278de5011879ac35", "1.52.0--r42hc0cfd56_0": "sha256:77c76917c1eda0d8c273eee61291b6b668c0c03962e31a86c89e6dd0d3345069", "1.52.0--r42ha9d7317_1": "sha256:e7f34a25dba8222a28ca6381cc7a9af1cedc68478245e0dc3225c41a90c38ab8", "1.54.0--r43ha9d7317_0": "sha256:45e148ab88d5d90f50db4154b3f3b4b6034634393b945fb666f107c274c5b654", "1.56.0--r43ha9d7317_1": "sha256:8b76bf800c5dbc5b58bc573188e020ec1a03dbc791a6ada44fe22c813d43d66d", "1.60.0--r44h3df3fcb_0": "sha256:5a51ed62dced35bbe51ef4d8e8568b1adf56480887f974b384f2997a8dd59b19"}, "docker": "quay.io/biocontainers/bioconductor-samspectral"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-samspectral.
shpc-registry automated BioContainers addition for bioconductor-samspectral
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-samspectral
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-samspectral:1.60.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-samspectral/1.60.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-samspectral/1.60.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-samspectral-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-samspectral-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-samspectral-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-samspectral-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-samspectral-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-samspectral-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-samspectral

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