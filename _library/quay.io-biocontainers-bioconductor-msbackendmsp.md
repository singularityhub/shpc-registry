---
layout: container
name:  "quay.io/biocontainers/bioconductor-msbackendmsp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msbackendmsp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msbackendmsp/container.yaml"
updated_at: "2024-03-18 02:31:59.093347"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msbackendmsp"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-msbackendmsp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msbackendmsp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-msbackendmsp", "latest": {"1.6.0--r43hdfd78af_0": "sha256:4785da430a902674e0a076addd8f81d09f517a3730dd6589d0e8a84209fd0720"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:cfcb9e007b019a92234147d0f55926ef1ea879a3fcbbcbc29900027aa57afc76", "1.4.0--r43hdfd78af_0": "sha256:0182cb4e3cba6aea4aee810bab8f773f7988eec39f0f64bad3cf69eca2ee50d9", "1.6.0--r43hdfd78af_0": "sha256:4785da430a902674e0a076addd8f81d09f517a3730dd6589d0e8a84209fd0720"}, "docker": "quay.io/biocontainers/bioconductor-msbackendmsp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msbackendmsp.
singularity registry hpc automated addition for bioconductor-msbackendmsp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendmsp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendmsp:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msbackendmsp/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msbackendmsp/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msbackendmsp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendmsp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendmsp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msbackendmsp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msbackendmsp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msbackendmsp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msbackendmsp

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