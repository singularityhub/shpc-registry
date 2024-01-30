---
layout: container
name:  "quay.io/biocontainers/r-bcbiosinglecell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bcbiosinglecell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-bcbiosinglecell/container.yaml"
updated_at: "2024-01-30 02:40:50.069091"
latest: "0.7.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-bcbiosinglecell"
aliases:
 - "pandoc"
versions:
 - "0.5.0--r41hdfd78af_0"
 - "0.6.2--r42hdfd78af_1"
 - "0.6.3--r42hdfd78af_0"
 - "0.6.3--r42hdfd78af_1"
 - "0.6.3--r43hdfd78af_2"
 - "0.6.4--r43hdfd78af_0"
 - "0.7.0--r43hdfd78af_0"
 - "0.7.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-bcbiosinglecell"
config: {"url": "https://biocontainers.pro/tools/r-bcbiosinglecell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bcbiosinglecell", "latest": {"0.7.1--r43hdfd78af_0": "sha256:061e4acb5c00a6186781a4a0fccf21f5471f9f10d73b46b22b060d54dcaf4c8e"}, "tags": {"0.5.0--r41hdfd78af_0": "sha256:4c2a569223ad69aded39d480542e20da64feb1e9d5da7fa5b85b069f624633fe", "0.6.2--r42hdfd78af_1": "sha256:c3bf8be79eaebdd37624d10659a6405b30cd69785507985b5754c83c58bce459", "0.6.3--r42hdfd78af_0": "sha256:66bc7083853e81623501a6920352ba6961f569e9a56c3d756bcedc1499612b54", "0.6.3--r42hdfd78af_1": "sha256:5456f6b700d6cff8b7d0592ebf12683626cbea1ac0b638e8e0cf8baf77c7d195", "0.6.3--r43hdfd78af_2": "sha256:b9f609b5daf02a648a65eed37159f1a3f921c17245e44edae5bce2a39dc98fa1", "0.6.4--r43hdfd78af_0": "sha256:d5a7b81d6560448a23450fcaf5f20d14953a2e52e248cc15dd2f7a504875811a", "0.7.0--r43hdfd78af_0": "sha256:b77fd553c95eb302c50527339a0043a15cd7a05b06038974e1cbf079a7051d61", "0.7.1--r43hdfd78af_0": "sha256:061e4acb5c00a6186781a4a0fccf21f5471f9f10d73b46b22b060d54dcaf4c8e"}, "docker": "quay.io/biocontainers/r-bcbiosinglecell", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bcbiosinglecell.
shpc-registry automated BioContainers addition for r-bcbiosinglecell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bcbiosinglecell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bcbiosinglecell:0.7.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bcbiosinglecell/0.7.1--r43hdfd78af_0
$ module help quay.io/biocontainers/r-bcbiosinglecell/0.7.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bcbiosinglecell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiosinglecell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiosinglecell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bcbiosinglecell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bcbiosinglecell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bcbiosinglecell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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