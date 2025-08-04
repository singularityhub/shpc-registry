---
layout: container
name:  "quay.io/biocontainers/bioconductor-ratchrloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ratchrloc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ratchrloc/container.yaml"
updated_at: "2025-08-04 04:23:51.223766"
latest: "2.1.6--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-ratchrloc"

versions:
 - "2.1.6--r41hdfd78af_9"
 - "2.1.6--r42hdfd78af_10"
 - "2.1.6--r43hdfd78af_11"
 - "2.1.6--r43hdfd78af_12"
 - "2.1.6--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-ratchrloc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ratchrloc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ratchrloc", "latest": {"2.1.6--r44hdfd78af_13": "sha256:6a0fe66a815a93e76d7585bbdaf5bad546da01df9007c40f13c5e177cd172e16"}, "tags": {"2.1.6--r41hdfd78af_9": "sha256:78705679c42b2813036ed6e5c8f0cde32ee8696ea18bbe18e9362e34d3da78d5", "2.1.6--r42hdfd78af_10": "sha256:d040185ab7477364e98868a1cbf611beb5fc1c48ba4302ab0ecda8cd4d6870b6", "2.1.6--r43hdfd78af_11": "sha256:61b4487524d29a6e1700902141728e9bba91ad52fd4eb37e7701ec84064a3fc9", "2.1.6--r43hdfd78af_12": "sha256:ed22f17c89ae67774cba26e8cca6490d1b316b1088bf41d85a9b017d8f612a26", "2.1.6--r44hdfd78af_13": "sha256:6a0fe66a815a93e76d7585bbdaf5bad546da01df9007c40f13c5e177cd172e16"}, "docker": "quay.io/biocontainers/bioconductor-ratchrloc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ratchrloc.
shpc-registry automated BioContainers addition for bioconductor-ratchrloc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ratchrloc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ratchrloc:2.1.6--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ratchrloc/2.1.6--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-ratchrloc/2.1.6--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ratchrloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ratchrloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ratchrloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ratchrloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ratchrloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ratchrloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ratchrloc

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