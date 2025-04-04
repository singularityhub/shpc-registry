---
layout: container
name:  "quay.io/biocontainers/bioconductor-cimice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cimice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cimice/container.yaml"
updated_at: "2025-04-04 03:03:19.492849"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cimice"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cimice"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cimice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cimice", "latest": {"1.14.0--r44hdfd78af_0": "sha256:280ffc9f3e1f34054c6f9c68b47ef2b0cc10eb4e5ffe7f467bb315350b210d92"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:95fd1d9e0d4c46b0172d8ffa457519b5de03a1f634efae3cd7956e66384b466a", "1.6.0--r42hdfd78af_0": "sha256:87d6d4c57e0decbb4ed552a00b1834fa577d5058de41421373fa4b1b94e597af", "1.8.0--r43hdfd78af_0": "sha256:533b22e2410fd630ce1e439f6d2e429585c78be40b8ae636cc1e343c7787a557", "1.10.0--r43hdfd78af_0": "sha256:f4b1d4f4465bd91caf03e6db2c2fb6ba52aeafc189d33e1959f653d5a1c25194", "1.14.0--r44hdfd78af_0": "sha256:280ffc9f3e1f34054c6f9c68b47ef2b0cc10eb4e5ffe7f467bb315350b210d92"}, "docker": "quay.io/biocontainers/bioconductor-cimice"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cimice.
shpc-registry automated BioContainers addition for bioconductor-cimice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cimice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cimice:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cimice/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cimice/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cimice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cimice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cimice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cimice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cimice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cimice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cimice

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