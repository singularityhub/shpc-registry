---
layout: container
name:  "quay.io/biocontainers/bioconductor-pvac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pvac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pvac/container.yaml"
updated_at: "2024-12-03 04:15:52.077699"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pvac"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pvac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pvac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pvac", "latest": {"1.50.0--r43hdfd78af_0": "sha256:42a427927fc6416f2b60eb9e89480badc15f28d755b8769f089cd17b58ded38b"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:23cf14b66668df674e3fa6e75e8d6e2658bc15a449ac20f10f5c562448a99689", "1.46.0--r42hdfd78af_0": "sha256:18800f1b59e9bd4818052c720535968cf2cef609989268a94e449859b3fd7834", "1.48.0--r43hdfd78af_0": "sha256:37d6c5316f5c67a07dd24ab868f76625d71cb8d80ea16d5e3b064f96a37a9d35", "1.50.0--r43hdfd78af_0": "sha256:42a427927fc6416f2b60eb9e89480badc15f28d755b8769f089cd17b58ded38b"}, "docker": "quay.io/biocontainers/bioconductor-pvac"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pvac.
shpc-registry automated BioContainers addition for bioconductor-pvac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pvac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pvac:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pvac/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pvac/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pvac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pvac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pvac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pvac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pvac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pvac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pvac

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