---
layout: container
name:  "quay.io/biocontainers/bioconductor-fmrs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fmrs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fmrs/container.yaml"
updated_at: "2025-01-21 03:01:27.027960"
latest: "1.16.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fmrs"

versions:
 - "1.4.0--r41hc0cfd56_2"
 - "1.8.0--r42hc0cfd56_0"
 - "1.8.0--r42ha9d7317_2"
 - "1.10.0--r43ha9d7317_0"
 - "1.12.0--r43ha9d7317_0"
 - "1.16.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fmrs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fmrs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fmrs", "latest": {"1.16.0--r44h3df3fcb_0": "sha256:b7e3da144b677b5a24a756157e152594f93f046384e18a5a85c68a53ca3149a3"}, "tags": {"1.4.0--r41hc0cfd56_2": "sha256:113a54545b22b3011f6993b95a83a51a0f73be167061f3c58a73bd031e959a43", "1.8.0--r42hc0cfd56_0": "sha256:8eb54bcba1b4d44b4d3c8701195e275cdac45c6188e154040274f0de5182ad0e", "1.8.0--r42ha9d7317_2": "sha256:710036a85c077bb8fba8bcb5db8a20bac4b791a191c8a9298a7a17ec23dd2cd9", "1.10.0--r43ha9d7317_0": "sha256:96d0f0e2ac1e957e59950219009c4caa9c29385b85c94a0ff71adb816936063d", "1.12.0--r43ha9d7317_0": "sha256:ce11e921791b8759494303bc2c347de4df3ea7373ea861388c8189974d82ef33", "1.16.0--r44h3df3fcb_0": "sha256:b7e3da144b677b5a24a756157e152594f93f046384e18a5a85c68a53ca3149a3"}, "docker": "quay.io/biocontainers/bioconductor-fmrs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fmrs.
shpc-registry automated BioContainers addition for bioconductor-fmrs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fmrs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fmrs:1.16.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fmrs/1.16.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-fmrs/1.16.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fmrs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fmrs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fmrs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fmrs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fmrs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fmrs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fmrs

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