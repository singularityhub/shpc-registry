---
layout: container
name:  "quay.io/biocontainers/r-acidgenomes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidgenomes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidgenomes/container.yaml"
updated_at: "2025-06-20 03:56:34.954031"
latest: "0.7.5--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidgenomes"

versions:
 - "0.3.0--r41hdfd78af_0"
 - "0.4.4--r42hdfd78af_1"
 - "0.4.5--r42hdfd78af_0"
 - "0.4.8--r42hdfd78af_0"
 - "0.4.8--r42hdfd78af_1"
 - "0.5.0--r42hdfd78af_0"
 - "0.5.0--r42hdfd78af_1"
 - "0.5.1--r43hdfd78af_0"
 - "0.6.1--r43hdfd78af_0"
 - "0.7.2--r43hdfd78af_0"
 - "0.7.2--r44hdfd78af_1"
 - "0.7.3--r44hdfd78af_0"
 - "0.7.5--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidgenomes"
config: {"url": "https://biocontainers.pro/tools/r-acidgenomes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidgenomes", "latest": {"0.7.5--r44hdfd78af_0": "sha256:3c7871f0ccc3c4a406b0c903d7389031486a33a63c1ff80ae8b517fa86124512"}, "tags": {"0.3.0--r41hdfd78af_0": "sha256:44d5d46dc2e579e3443a74aacca29eb700f3168cb05513863d84f7307eaea512", "0.4.4--r42hdfd78af_1": "sha256:e84f7017a7be9372600a058cb8b85b3ac4817b104b962827aff805ecf0a50012", "0.4.5--r42hdfd78af_0": "sha256:017b7ee4b11748dfa04810aaf5f387d419178917dc08a31e0deeefd6ff77da6e", "0.4.8--r42hdfd78af_0": "sha256:9fd12fd8ffbe7f4e6b343f44c8073dc53fa0115a6116e34ca80adeed91337827", "0.4.8--r42hdfd78af_1": "sha256:9756c9227d10fa8b24e3b6ba00c5dea0cb6744481844eb634df94d806d89bb89", "0.5.0--r42hdfd78af_0": "sha256:1ec2853cb704ca65684845abeea4fa24af00b42dd1126504329aa5ada6b57cc3", "0.5.0--r42hdfd78af_1": "sha256:f527a611336a66d5badc80241825ffa7c5f4794320a1b4603373a6ff21300fb5", "0.5.1--r43hdfd78af_0": "sha256:951a3d837ba439e925f1136dbdb0a11bb54ba7993cf7982346eb47269af907cf", "0.6.1--r43hdfd78af_0": "sha256:cc6ec3ed878eb627d65682b4556681e9ac15636b49618b1f2af7170b176b2202", "0.7.2--r43hdfd78af_0": "sha256:a278b23d3e6947372b060cb1e59077c68f9a93aad7d1699d3e7d89ef31b66d10", "0.7.2--r44hdfd78af_1": "sha256:6946d33cc773772906ca44f2ab50368d0fa9bdf4c15977aa3886a213e553e309", "0.7.3--r44hdfd78af_0": "sha256:f8c811092b2ce7fcbbfaefef157a187eb28cfd7802f82cd1233303dfe49ff8fc", "0.7.5--r44hdfd78af_0": "sha256:3c7871f0ccc3c4a406b0c903d7389031486a33a63c1ff80ae8b517fa86124512"}, "docker": "quay.io/biocontainers/r-acidgenomes"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidgenomes.
shpc-registry automated BioContainers addition for r-acidgenomes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidgenomes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidgenomes:0.7.5--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidgenomes/0.7.5--r44hdfd78af_0
$ module help quay.io/biocontainers/r-acidgenomes/0.7.5--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidgenomes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidgenomes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidgenomes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidgenomes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidgenomes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidgenomes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidgenomes

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