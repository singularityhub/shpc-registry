---
layout: container
name:  "quay.io/biocontainers/bioconductor-tpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tpp/container.yaml"
updated_at: "2024-05-04 02:24:38.970346"
latest: "3.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tpp"

versions:
 - "3.22.0--r41hdfd78af_0"
 - "3.26.0--r42hdfd78af_0"
 - "3.28.0--r43hdfd78af_0"
 - "3.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tpp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tpp", "latest": {"3.30.0--r43hdfd78af_0": "sha256:25bc5754d76354613d43735b022d558a42b48030e8f883a2b0200819edf1c4a4"}, "tags": {"3.22.0--r41hdfd78af_0": "sha256:0e279430fbc4d6f9d049b41bbd4e14b48205410ed389acbcffa373819528a5ad", "3.26.0--r42hdfd78af_0": "sha256:2ea33abb853f1e6ba48ab3030908733103fcb07cf54e4011aee1567b318bf1cc", "3.28.0--r43hdfd78af_0": "sha256:c5bb2f39e57fa1a4e4b7443c4681ce4585b72b93e0adc3b18da7ebb7963c6506", "3.30.0--r43hdfd78af_0": "sha256:25bc5754d76354613d43735b022d558a42b48030e8f883a2b0200819edf1c4a4"}, "docker": "quay.io/biocontainers/bioconductor-tpp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tpp.
shpc-registry automated BioContainers addition for bioconductor-tpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tpp:3.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tpp/3.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tpp/3.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tpp

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