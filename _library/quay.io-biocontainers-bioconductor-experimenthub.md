---
layout: container
name:  "quay.io/biocontainers/bioconductor-experimenthub"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-experimenthub/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-experimenthub/container.yaml"
updated_at: "2025-10-11 03:08:39.267833"
latest: "2.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-experimenthub"

versions:
 - "2.2.0--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
 - "2.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-experimenthub"
config: {"url": "https://biocontainers.pro/tools/bioconductor-experimenthub", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-experimenthub", "latest": {"2.14.0--r44hdfd78af_0": "sha256:ff4f23a2ca3916123ad9da716f675673f74e08682ed92b043f5918d27d8bbef5"}, "tags": {"2.2.0--r41hdfd78af_0": "sha256:0d1c16d5069ba5a318c9057e51059e1628df22d761d51fe2c6a7ac1fe415890e", "2.6.0--r42hdfd78af_0": "sha256:30f04f78f21ded5620a2764b54606d9edd8f56cfd27d55a7c311291f1c872cb3", "2.8.0--r43hdfd78af_0": "sha256:7fcb9c3bf644b8f6d7d16f8d6bd6176abe1a65a94165a5e908ce29f9ae79aab7", "2.10.0--r43hdfd78af_0": "sha256:27676d8e31aaccf869a33efb6bc9d8cb59c10f890b63f3f31e3832be2fa6c55c", "2.14.0--r44hdfd78af_0": "sha256:ff4f23a2ca3916123ad9da716f675673f74e08682ed92b043f5918d27d8bbef5"}, "docker": "quay.io/biocontainers/bioconductor-experimenthub"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-experimenthub.
shpc-registry automated BioContainers addition for bioconductor-experimenthub
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-experimenthub
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-experimenthub:2.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-experimenthub/2.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-experimenthub/2.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-experimenthub-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-experimenthub-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-experimenthub-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-experimenthub-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-experimenthub-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-experimenthub-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-experimenthub

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