---
layout: container
name:  "quay.io/biocontainers/bioconductor-starank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-starank/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-starank/container.yaml"
updated_at: "2025-01-02 03:31:05.559331"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-starank"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-starank"
config: {"url": "https://biocontainers.pro/tools/bioconductor-starank", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-starank", "latest": {"1.44.0--r43hdfd78af_0": "sha256:878e6dac3cec1c84af0f669b5637f3f7b1e2cd8ba16529b1fad02d9c9fb47739"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:31117fc2eb77b02bd5d4b252ff68fd3e764c414adaa78d63d8380a31b271a40c", "1.40.0--r42hdfd78af_0": "sha256:483331f0482915fc2b9b645dca1e4f3d516d710ca31c8fe555244e466d2b91f7", "1.42.0--r43hdfd78af_0": "sha256:88840ff9d8959e3ce704e194de1b8406fcadcb70801091f9d1d17665a1fcbd7a", "1.44.0--r43hdfd78af_0": "sha256:878e6dac3cec1c84af0f669b5637f3f7b1e2cd8ba16529b1fad02d9c9fb47739"}, "docker": "quay.io/biocontainers/bioconductor-starank"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-starank.
shpc-registry automated BioContainers addition for bioconductor-starank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-starank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-starank:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-starank/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-starank/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-starank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-starank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-starank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-starank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-starank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-starank-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-starank

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