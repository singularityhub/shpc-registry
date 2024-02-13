---
layout: container
name:  "quay.io/biocontainers/bioconductor-reder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-reder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-reder/container.yaml"
updated_at: "2024-02-13 02:43:00.767413"
latest: "2.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-reder"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "2.2.0--r42hdfd78af_0"
 - "2.4.1--r43hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-reder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-reder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-reder", "latest": {"2.6.0--r43hdfd78af_0": "sha256:995817281f99b6812879afce1b0586e6ea9b67dc65dbe1a1906b25094ed02eb4"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:9d44392aa5467d308688fbd4b58d39b3472d837ff9c04c82182014f932b732de", "2.2.0--r42hdfd78af_0": "sha256:df9182a693ad3d54901ba5c8b43d0ca04f4ec5d7229b3d032ff0611f344bfeb4", "2.4.1--r43hdfd78af_0": "sha256:1102cd165f4510e75f6eff73118ce9defc676a64cfd9be7e9a6c08a679bafb2d", "2.6.0--r43hdfd78af_0": "sha256:995817281f99b6812879afce1b0586e6ea9b67dc65dbe1a1906b25094ed02eb4"}, "docker": "quay.io/biocontainers/bioconductor-reder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-reder.
shpc-registry automated BioContainers addition for bioconductor-reder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-reder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-reder:2.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-reder/2.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-reder/2.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-reder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-reder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-reder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-reder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-reder

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