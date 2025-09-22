---
layout: container
name:  "quay.io/biocontainers/bioconductor-plpe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plpe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plpe/container.yaml"
updated_at: "2025-09-22 03:26:03.811812"
latest: "1.66.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-plpe"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.66.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-plpe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plpe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plpe", "latest": {"1.66.0--r44hdfd78af_0": "sha256:ed06f3d59f575cd76a7af96b60f863ebe9f7c0bef917615a048c9b763a75b684"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:10a9dd29c49e58f808758f388998c1b731674ade9de5865a734cd01a9873a3e8", "1.58.0--r42hdfd78af_0": "sha256:439ea7fd1e171c97559d2cdf32bb03d8a0bf45ed75ab26ea4fe8fedb88ba399d", "1.60.0--r43hdfd78af_0": "sha256:ff29d75a7c8da4c0e280ec08beb293a47d6604106f3ebc5b8e5101c2025678de", "1.62.0--r43hdfd78af_0": "sha256:caf68ec93d9611b05d9a79f923adb207f771bc2cc09ed9be731a4112451ed34f", "1.66.0--r44hdfd78af_0": "sha256:ed06f3d59f575cd76a7af96b60f863ebe9f7c0bef917615a048c9b763a75b684"}, "docker": "quay.io/biocontainers/bioconductor-plpe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plpe.
shpc-registry automated BioContainers addition for bioconductor-plpe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plpe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plpe:1.66.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plpe/1.66.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-plpe/1.66.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plpe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plpe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plpe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plpe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plpe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plpe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-plpe

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