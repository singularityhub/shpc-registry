---
layout: container
name:  "quay.io/biocontainers/bioconductor-mousechrloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mousechrloc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mousechrloc/container.yaml"
updated_at: "2024-07-26 02:36:49.706804"
latest: "2.1.6--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mousechrloc"

versions:
 - "2.1.6--r41hdfd78af_9"
 - "2.1.6--r42hdfd78af_10"
 - "2.1.6--r43hdfd78af_11"
 - "2.1.6--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mousechrloc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mousechrloc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mousechrloc", "latest": {"2.1.6--r43hdfd78af_12": "sha256:9d07dd50d406e620cc40a5193585c6a254e0d8ed69b6cfc22f213e53221e2009"}, "tags": {"2.1.6--r41hdfd78af_9": "sha256:f99f36c3b100f1ff2d67cc8809a78ca9cc890ba7350cb2f85264755e3ff5fff3", "2.1.6--r42hdfd78af_10": "sha256:1a7b99b9261417bb9cba19b416d7e6b595071709b10953e1da5d63e068f43651", "2.1.6--r43hdfd78af_11": "sha256:c858a3aa79b6618aa5c79ddbf8e01db1536a0852910a9e5aa9ceb8e0f0195c68", "2.1.6--r43hdfd78af_12": "sha256:9d07dd50d406e620cc40a5193585c6a254e0d8ed69b6cfc22f213e53221e2009"}, "docker": "quay.io/biocontainers/bioconductor-mousechrloc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mousechrloc.
shpc-registry automated BioContainers addition for bioconductor-mousechrloc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mousechrloc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mousechrloc:2.1.6--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mousechrloc/2.1.6--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mousechrloc/2.1.6--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mousechrloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mousechrloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mousechrloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mousechrloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mousechrloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mousechrloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mousechrloc

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