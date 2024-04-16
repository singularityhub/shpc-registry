---
layout: container
name:  "quay.io/biocontainers/bioconductor-les"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-les/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-les/container.yaml"
updated_at: "2024-04-16 03:05:49.245635"
latest: "1.52.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-les"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.48.0--r42hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.52.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-les"
config: {"url": "https://biocontainers.pro/tools/bioconductor-les", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-les", "latest": {"1.52.0--r43hdfd78af_1": "sha256:49414ac75237f3623f21dbfd4f4cd2f41addc110f8f4bdad0a3206a3c0db0cee"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:78508b43a0803d5e853fd0d262eb2b1cab90ed7fcae64a20f6fdfc722b4effb3", "1.48.0--r42hdfd78af_0": "sha256:84d08a8a97ac655027232330a6dab05af757776e84e14846778aef53855e260d", "1.50.0--r43hdfd78af_0": "sha256:faccbb0f6ee75a2dca71bc55d65a7922113c81288a2aa076b86c1070cd328d2a", "1.52.0--r43hdfd78af_1": "sha256:49414ac75237f3623f21dbfd4f4cd2f41addc110f8f4bdad0a3206a3c0db0cee"}, "docker": "quay.io/biocontainers/bioconductor-les"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-les.
shpc-registry automated BioContainers addition for bioconductor-les
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-les
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-les:1.52.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-les/1.52.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-les/1.52.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-les-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-les-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-les-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-les-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-les-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-les-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-les

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