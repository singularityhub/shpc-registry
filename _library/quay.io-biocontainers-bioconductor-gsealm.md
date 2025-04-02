---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsealm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsealm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsealm/container.yaml"
updated_at: "2025-04-02 03:47:22.659582"
latest: "1.66.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsealm"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.66.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsealm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsealm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsealm", "latest": {"1.66.0--r44hdfd78af_0": "sha256:07ffb5776c055f054e7cffdc004d8d18f8879144b515d9b873d46a80fa475806"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:3ca0af58143953b265751753c97d585ba8f3b7969678647996eb48a7486e735f", "1.58.0--r42hdfd78af_0": "sha256:7bd5a4e0981e844f1d06a54b433938ae364851013671501de0ed7df69e1d039b", "1.60.0--r43hdfd78af_0": "sha256:281b615bfaa8acf70f980b19189fe95bb91b1f16725aabec41040e7d79f3fd57", "1.62.0--r43hdfd78af_0": "sha256:3806402b51c4992f30769991ed980db629c4a8656f8fb91e7f54cbc1a7f67cfb", "1.66.0--r44hdfd78af_0": "sha256:07ffb5776c055f054e7cffdc004d8d18f8879144b515d9b873d46a80fa475806"}, "docker": "quay.io/biocontainers/bioconductor-gsealm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsealm.
shpc-registry automated BioContainers addition for bioconductor-gsealm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsealm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsealm:1.66.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsealm/1.66.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gsealm/1.66.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsealm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsealm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsealm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsealm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsealm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsealm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gsealm

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