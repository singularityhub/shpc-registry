---
layout: container
name:  "quay.io/biocontainers/bioconductor-ewce"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ewce/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ewce/container.yaml"
updated_at: "2025-12-11 03:35:03.011837"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ewce"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.2--r43hdfd78af_0"
 - "1.10.2--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ewce"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ewce", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ewce", "latest": {"1.14.0--r44hdfd78af_0": "sha256:0b7e4170aec9d4d1383d32e893c716de17e8d093c7feee451cd1ff2470c1f69e"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:745deb9a0cd62484210da4357840222560dc1ed22574e5c80ac79fa21065ec7a", "1.6.0--r42hdfd78af_0": "sha256:f8d301f97eafa95e88d6ca1a92bf86d093d13196a137325c11fdd7387fda2ff4", "1.8.2--r43hdfd78af_0": "sha256:1dd332f315fbce5b7bf86b352fd27d191e9c558710ddf97d29e7ba12c224a0b6", "1.10.2--r43hdfd78af_0": "sha256:3769b5bb8eb39753f90377dbbe647cb91274aba25ae91a3eff9f0b48ad421621", "1.14.0--r44hdfd78af_0": "sha256:0b7e4170aec9d4d1383d32e893c716de17e8d093c7feee451cd1ff2470c1f69e"}, "docker": "quay.io/biocontainers/bioconductor-ewce"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ewce.
shpc-registry automated BioContainers addition for bioconductor-ewce
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ewce
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ewce:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ewce/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ewce/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ewce-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ewce-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ewce-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ewce-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ewce-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ewce-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ewce

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