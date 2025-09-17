---
layout: container
name:  "quay.io/biocontainers/bioconductor-typeinfo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-typeinfo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-typeinfo/container.yaml"
updated_at: "2025-09-17 03:45:40.374763"
latest: "1.68.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-typeinfo"

versions:
 - "1.60.0--r41hdfd78af_0"
 - "1.64.0--r42hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-typeinfo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-typeinfo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-typeinfo", "latest": {"1.68.0--r43hdfd78af_0": "sha256:a0d8880489559c5e0587efa698ab851b01aa129263dcc1dc1167cf0a790f14ec"}, "tags": {"1.60.0--r41hdfd78af_0": "sha256:6c1c6ae9637c36378fb9d24abae85b7d8f9dea72b18918dcde7dfaf752293749", "1.64.0--r42hdfd78af_0": "sha256:9863856e8c3b1cb2f9e4373cb8236d52a9631def2eadd2fab77798cf623b489e", "1.66.0--r43hdfd78af_0": "sha256:8c2334c393ca92f05c60eba8405fd41cc5db8faad330231ef099110bb8d664ce", "1.68.0--r43hdfd78af_0": "sha256:a0d8880489559c5e0587efa698ab851b01aa129263dcc1dc1167cf0a790f14ec"}, "docker": "quay.io/biocontainers/bioconductor-typeinfo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-typeinfo.
shpc-registry automated BioContainers addition for bioconductor-typeinfo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-typeinfo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-typeinfo:1.68.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-typeinfo/1.68.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-typeinfo/1.68.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-typeinfo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-typeinfo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-typeinfo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-typeinfo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-typeinfo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-typeinfo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-typeinfo

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