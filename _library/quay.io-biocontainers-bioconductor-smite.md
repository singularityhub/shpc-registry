---
layout: container
name:  "quay.io/biocontainers/bioconductor-smite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-smite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-smite/container.yaml"
updated_at: "2023-12-06 02:57:07.492131"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-smite"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-smite"
config: {"url": "https://biocontainers.pro/tools/bioconductor-smite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-smite", "latest": {"1.28.0--r43hdfd78af_0": "sha256:afb1d72eb20616cf982223d946ef104a9c974f40a6d7aa8fbc08c6ece8e81b34"}, "tags": {"1.8.0--r351_0": "sha256:245491c41b810d33aed198a4705936f1703bebf5689aa6ee1371385d4e83c756", "1.26.0--r42hdfd78af_0": "sha256:64b1fb04342761e6de9934ad6cfebe0d5e1e2bbc04e4ca7e473a73846542cf36", "1.22.0--r41hdfd78af_0": "sha256:d2971b37f67402a668252b32ca093831c2637440c9ad3786e9474d0fafd7527f", "1.20.0--r41hdfd78af_0": "sha256:4d156818abc25486396885a39d4dfa04339e7a2bf6cfe1fce8e270342ba261b1", "1.18.0--r40hdfd78af_1": "sha256:5e3ca6cf7fee8b15bbb60d953905b8f097067f2bb7f5d6649e84d8b356c5c41e", "1.16.0--r40_0": "sha256:3e2f550f64fa172e3671b500ee1ffd4e9dfced0e33ea00d65c200e57b0e74095", "1.28.0--r43hdfd78af_0": "sha256:afb1d72eb20616cf982223d946ef104a9c974f40a6d7aa8fbc08c6ece8e81b34"}, "docker": "quay.io/biocontainers/bioconductor-smite", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-smite.
shpc-registry automated BioContainers addition for bioconductor-smite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-smite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-smite:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-smite/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-smite/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-smite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-smite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-smite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-smite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-smite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-smite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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