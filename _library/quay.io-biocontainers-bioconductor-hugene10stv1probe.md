---
layout: container
name:  "quay.io/biocontainers/bioconductor-hugene10stv1probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hugene10stv1probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hugene10stv1probe/container.yaml"
updated_at: "2025-10-01 03:30:56.668587"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hugene10stv1probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hugene10stv1probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hugene10stv1probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hugene10stv1probe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:31c06bf5f607ca046d127e3e72e9b620d7c701d3fd07a50e1f644d906985bceb"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:af76ac3fc02a482dd58ba7f9fcefc6166aee9b49a5af46749823a3f3058b11aa", "2.18.0--r42hdfd78af_10": "sha256:cdace5dd7d8a06a53c51eb09bda96b369767f238012e7477f6c4ffc613858e8d", "2.18.0--r43hdfd78af_11": "sha256:025a1888e18bbe930420cf7d5fdfc28791a60aa4faca906ebc7ba50836fa7d5c", "2.18.0--r43hdfd78af_12": "sha256:346d15a112e221bc57d144131ce0fd34ebbbb420f39f0d3e34d3ddf356d121a9", "2.18.0--r44hdfd78af_13": "sha256:31c06bf5f607ca046d127e3e72e9b620d7c701d3fd07a50e1f644d906985bceb"}, "docker": "quay.io/biocontainers/bioconductor-hugene10stv1probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hugene10stv1probe.
shpc-registry automated BioContainers addition for bioconductor-hugene10stv1probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hugene10stv1probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hugene10stv1probe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hugene10stv1probe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hugene10stv1probe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hugene10stv1probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hugene10stv1probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hugene10stv1probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hugene10stv1probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hugene10stv1probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hugene10stv1probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hugene10stv1probe

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