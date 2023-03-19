---
layout: container
name:  "quay.io/biocontainers/bioconductor-hspec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hspec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hspec/container.yaml"
updated_at: "2023-03-19 03:27:12.708092"
latest: "0.99.1--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-hspec"

versions:
 - "0.99.1--r41hdfd78af_9"
 - "0.99.1--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-hspec"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hspec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hspec", "latest": {"0.99.1--r42hdfd78af_10": "sha256:8b0e2abf3803feff6b8b712653c16086e56b3a93ba218db15ceb0550022db38e"}, "tags": {"0.99.1--r41hdfd78af_9": "sha256:2774d752de3e1a314713df4bc7c916e3877025bb588a1ef2d78f2444f40bbaf8", "0.99.1--r42hdfd78af_10": "sha256:8b0e2abf3803feff6b8b712653c16086e56b3a93ba218db15ceb0550022db38e"}, "docker": "quay.io/biocontainers/bioconductor-hspec"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hspec.
shpc-registry automated BioContainers addition for bioconductor-hspec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hspec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hspec:0.99.1--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hspec/0.99.1--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-hspec/0.99.1--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hspec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hspec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hspec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hspec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hspec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hspec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hspec

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