---
layout: container
name:  "quay.io/biocontainers/bioconductor-goexpress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-goexpress/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-goexpress/container.yaml"
updated_at: "2024-02-15 02:49:04.267167"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-goexpress"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-goexpress"
config: {"url": "https://biocontainers.pro/tools/bioconductor-goexpress", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-goexpress", "latest": {"1.36.0--r43hdfd78af_0": "sha256:7618383e1bdfc671a6590fedb6d481dead7e64cd2e7e4406a6e8f7ca3e74d526"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:28af0a8a9c87e34f0cb591aad3f2ae8b5631d86eeb044e386a277dc12bee06e4", "1.32.0--r42hdfd78af_0": "sha256:c74b6da3a06a7e9e27046adbfbc042129f2bf2f34badd262e5e2a5966aa3e0d4", "1.34.0--r43hdfd78af_0": "sha256:37202a207e698ca830daa5951d5563403a177a7aa9b9b30e657097dc2f30fb27", "1.36.0--r43hdfd78af_0": "sha256:7618383e1bdfc671a6590fedb6d481dead7e64cd2e7e4406a6e8f7ca3e74d526"}, "docker": "quay.io/biocontainers/bioconductor-goexpress"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-goexpress.
shpc-registry automated BioContainers addition for bioconductor-goexpress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-goexpress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-goexpress:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-goexpress/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-goexpress/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-goexpress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-goexpress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-goexpress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-goexpress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-goexpress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-goexpress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-goexpress

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