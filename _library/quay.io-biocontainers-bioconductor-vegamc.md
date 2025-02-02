---
layout: container
name:  "quay.io/biocontainers/bioconductor-vegamc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-vegamc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-vegamc/container.yaml"
updated_at: "2025-02-02 02:50:39.656041"
latest: "3.44.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-vegamc"

versions:
 - "3.32.0--r41hc0cfd56_2"
 - "3.36.0--r42hc0cfd56_0"
 - "3.36.0--r42ha9d7317_1"
 - "3.38.0--r43ha9d7317_0"
 - "3.40.0--r43ha9d7317_0"
 - "3.44.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-vegamc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-vegamc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-vegamc", "latest": {"3.44.0--r44h3df3fcb_0": "sha256:4d42c2019c99015a76b7be68fe40b45827bd8ee414afe76332054693c9c044b9"}, "tags": {"3.32.0--r41hc0cfd56_2": "sha256:1b40ecae1fd4f39679f129563b7287b702f0200ff80d1e94fd4738f6df5e2a31", "3.36.0--r42hc0cfd56_0": "sha256:8d9df5a17ab3d60b59ce00bb91baf0bc24e8232c6c678773c3e838a715fff28a", "3.36.0--r42ha9d7317_1": "sha256:84834ea0cad4b719fdcfe8b1f98a2e3c7668464dc8fd7e47bb95bd8493991cb5", "3.38.0--r43ha9d7317_0": "sha256:1dbb6f33575412707fd56a08786f714a157b0c8cb588449fa1ac4a8d092df3d0", "3.40.0--r43ha9d7317_0": "sha256:3190d2add6abe06bf7851bed01abf33831052b2e7816133add4bb40496d1e0a5", "3.44.0--r44h3df3fcb_0": "sha256:4d42c2019c99015a76b7be68fe40b45827bd8ee414afe76332054693c9c044b9"}, "docker": "quay.io/biocontainers/bioconductor-vegamc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-vegamc.
shpc-registry automated BioContainers addition for bioconductor-vegamc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-vegamc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-vegamc:3.44.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-vegamc/3.44.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-vegamc/3.44.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-vegamc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vegamc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-vegamc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-vegamc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-vegamc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-vegamc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-vegamc

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