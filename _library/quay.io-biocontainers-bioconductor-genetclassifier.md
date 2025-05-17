---
layout: container
name:  "quay.io/biocontainers/bioconductor-genetclassifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genetclassifier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genetclassifier/container.yaml"
updated_at: "2025-05-17 03:28:48.438580"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genetclassifier"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genetclassifier"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genetclassifier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genetclassifier", "latest": {"1.46.0--r44hdfd78af_0": "sha256:f008754fb9e98390df2fab89f5ba17d29e19708abc2307e448e474fdcf67f8b7"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:fb3f0f5caeddd45fe2f7fd901f8bd6479812750abf337c04883ed236bbc72df0", "1.38.0--r42hdfd78af_0": "sha256:c01d9a4ada86a3b4223e1e580f788021049ce3cbde97ec61c10bcded623b1768", "1.40.0--r43hdfd78af_0": "sha256:1f402d8987cc503e0ae716d7fbf02f01e2244dec3ce2e9eb43a330853a569279", "1.42.0--r43hdfd78af_0": "sha256:6a69c46c9edfcb2b7b87e6e273c9111e2f61e67d5db0482c8b18544950551844", "1.46.0--r44hdfd78af_0": "sha256:f008754fb9e98390df2fab89f5ba17d29e19708abc2307e448e474fdcf67f8b7"}, "docker": "quay.io/biocontainers/bioconductor-genetclassifier"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genetclassifier.
shpc-registry automated BioContainers addition for bioconductor-genetclassifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genetclassifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genetclassifier:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genetclassifier/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genetclassifier/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genetclassifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genetclassifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genetclassifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genetclassifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genetclassifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genetclassifier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genetclassifier

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