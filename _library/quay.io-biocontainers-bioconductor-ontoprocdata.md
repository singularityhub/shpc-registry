---
layout: container
name:  "quay.io/biocontainers/bioconductor-ontoprocdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ontoprocdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ontoprocdata/container.yaml"
updated_at: "2023-07-26 03:29:02.216193"
latest: "0.99.9901--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-ontoprocdata"

versions:
 - "0.99.9--r41hdfd78af_1"
 - "0.99.9901--r42hdfd78af_0"
 - "0.99.9901--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-ontoprocdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ontoprocdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ontoprocdata", "latest": {"0.99.9901--r43hdfd78af_1": "sha256:974d5cedf59f0674211f20f11bde504020315026d89e74fb824c139a57ebdcb3"}, "tags": {"0.99.9--r41hdfd78af_1": "sha256:513546f1630c241e5d72aaa52f7d4189432c03567ba2140d69cd794201592b40", "0.99.9901--r42hdfd78af_0": "sha256:6b3acaf4539eca4b0ea6bc56f6871be3e7e11aecc539f235ed7845a3b44ce285", "0.99.9901--r43hdfd78af_1": "sha256:974d5cedf59f0674211f20f11bde504020315026d89e74fb824c139a57ebdcb3"}, "docker": "quay.io/biocontainers/bioconductor-ontoprocdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ontoprocdata.
shpc-registry automated BioContainers addition for bioconductor-ontoprocdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ontoprocdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ontoprocdata:0.99.9901--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ontoprocdata/0.99.9901--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-ontoprocdata/0.99.9901--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ontoprocdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ontoprocdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ontoprocdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ontoprocdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ontoprocdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ontoprocdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ontoprocdata

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