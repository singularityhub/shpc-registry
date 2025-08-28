---
layout: container
name:  "quay.io/biocontainers/r-acidplots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidplots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidplots/container.yaml"
updated_at: "2025-08-28 12:32:19.688293"
latest: "0.7.4--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidplots"

versions:
 - "0.4.0--r41hdfd78af_0"
 - "0.5.3--r42hdfd78af_1"
 - "0.5.4--r42hdfd78af_0"
 - "0.5.4--r42hdfd78af_1"
 - "0.5.5--r42hdfd78af_1"
 - "0.5.5--r43hdfd78af_2"
 - "0.6.1--r43hdfd78af_0"
 - "0.7.1--r43hdfd78af_0"
 - "0.7.2--r43hdfd78af_0"
 - "0.7.3--r43hdfd78af_0"
 - "0.7.3--r44hdfd78af_1"
 - "0.7.4--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidplots"
config: {"url": "https://biocontainers.pro/tools/r-acidplots", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidplots", "latest": {"0.7.4--r44hdfd78af_0": "sha256:eca5fe891eb2afc5805b27af4c47183e38f10cc6526e663afa175eba9b646c9f"}, "tags": {"0.4.0--r41hdfd78af_0": "sha256:51aca75c76f442f3e9af355ad80d4b1d5006ecfe214ae17e4a0bd7fa83a34843", "0.5.3--r42hdfd78af_1": "sha256:b6c03328839ea124fbaf3fc0eae52971e5f2e4423c5efec58d0647eaf06c53cf", "0.5.4--r42hdfd78af_0": "sha256:22571437fc8eb8c060573f8dfbbfbcc05b59d60b574fe658c8dce15ef46632d3", "0.5.4--r42hdfd78af_1": "sha256:68014cf2fcb201f447a42dbcb1db146398ca33c06981f8d75020b0f79c262490", "0.5.5--r42hdfd78af_1": "sha256:5087715d867e2c3716bbd4511c7e09d8fb34c461e65afcc4a002beeb9761618f", "0.5.5--r43hdfd78af_2": "sha256:0ae832afef6157e8253d1a92056d56a7bf46cc6fccda58d3c5aab37a7bc17b53", "0.6.1--r43hdfd78af_0": "sha256:dc688e5afaf5588b23dfb4642ecd4f577cccdc3d93c1f233b64ca74fd683930c", "0.7.1--r43hdfd78af_0": "sha256:11300b7c951f34c50c25607d2a6415bfe4b6e616edcef130225d580bbbf200a4", "0.7.2--r43hdfd78af_0": "sha256:08b3f07560c4b26d497cb7f84ceb6801fb923e97ff41e5e1d9a41e84c2c6d43b", "0.7.3--r43hdfd78af_0": "sha256:28f8aeffbd3d417e86e0aceb44bb0a38677b699d6a80ac76bec9abbc3fc1183a", "0.7.3--r44hdfd78af_1": "sha256:9623918dcb58709dff3fef97c3f39f88598048008d8e7a3a3f03617c0390ef19", "0.7.4--r44hdfd78af_0": "sha256:eca5fe891eb2afc5805b27af4c47183e38f10cc6526e663afa175eba9b646c9f"}, "docker": "quay.io/biocontainers/r-acidplots"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidplots.
shpc-registry automated BioContainers addition for r-acidplots
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidplots
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidplots:0.7.4--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidplots/0.7.4--r44hdfd78af_0
$ module help quay.io/biocontainers/r-acidplots/0.7.4--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidplots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidplots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidplots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidplots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidplots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidplots-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidplots

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