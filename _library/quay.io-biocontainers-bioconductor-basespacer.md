---
layout: container
name:  "quay.io/biocontainers/bioconductor-basespacer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-basespacer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-basespacer/container.yaml"
updated_at: "2024-02-26 03:50:18.270820"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-basespacer"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-basespacer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-basespacer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-basespacer", "latest": {"1.46.0--r43hdfd78af_0": "sha256:60a76299b32fe9a5bb637a51e6cbf484becbcb77b085ff3986d061cd7743b4d5"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:8ecdbdb59299c1825b1a080abd582fff071ec5db3633bda0453408298bfbf391", "1.42.0--r42hdfd78af_0": "sha256:bd08d35ac68252b7a199a64f58dcc7656bee6ab96c431b39227de8212a54dee5", "1.44.0--r43hdfd78af_0": "sha256:696442910e74dc780b180d6200f4c916e0810ee1e3fbb9422904aef5099ed661", "1.46.0--r43hdfd78af_0": "sha256:60a76299b32fe9a5bb637a51e6cbf484becbcb77b085ff3986d061cd7743b4d5"}, "docker": "quay.io/biocontainers/bioconductor-basespacer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-basespacer.
shpc-registry automated BioContainers addition for bioconductor-basespacer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-basespacer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-basespacer:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-basespacer/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-basespacer/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-basespacer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basespacer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basespacer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-basespacer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-basespacer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-basespacer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-basespacer

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