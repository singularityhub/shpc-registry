---
layout: container
name:  "quay.io/biocontainers/r-gkmsvm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-gkmsvm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-gkmsvm/container.yaml"
updated_at: "2024-04-11 02:56:37.020045"
latest: "0.83.0--r43h21a89ab_0"
container_url: "https://biocontainers.pro/tools/r-gkmsvm"

versions:
 - "0.81.0--r41h87f3376_3"
 - "0.81.0--r42h87f3376_4"
 - "0.82.0--r42hecf12ef_0"
 - "0.82.0--r42hecf12ef_1"
 - "0.82.0--r42h21a89ab_2"
 - "0.82.0--r43h21a89ab_3"
 - "0.83.0--r43h21a89ab_0"
description: "shpc-registry automated BioContainers addition for r-gkmsvm"
config: {"url": "https://biocontainers.pro/tools/r-gkmsvm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-gkmsvm", "latest": {"0.83.0--r43h21a89ab_0": "sha256:c9bfb1e04105d3ef57ade60839fd0a6ccf632d5858471cac79ab66c8cc261bb7"}, "tags": {"0.81.0--r41h87f3376_3": "sha256:76bb60f5402414c4c95086be4cdcac98a2c8f73fbec887c37368a109fd5f06b4", "0.81.0--r42h87f3376_4": "sha256:e54794d3fb8ce3d3398b253de78cd49caac23f2d4494e7ed42f969036b0b60f1", "0.82.0--r42hecf12ef_0": "sha256:f722b717b7db9d1bc35562942935fbfdd093978ef3c0756c36717561dc2a24ac", "0.82.0--r42hecf12ef_1": "sha256:24b5f7a5ae8eb9a300a8720db2ae9a08e4cc284ee690ef3ba7faaf9f9a8c1ee8", "0.82.0--r42h21a89ab_2": "sha256:1a6fb4e309479e8b34a3f904357d48e1c063d3119aee64ad5419d8ca634a8663", "0.82.0--r43h21a89ab_3": "sha256:3eba3878c08e6ee8ab74e4c1e0c7af42d7ceede9557be5884dd55d621af63464", "0.83.0--r43h21a89ab_0": "sha256:c9bfb1e04105d3ef57ade60839fd0a6ccf632d5858471cac79ab66c8cc261bb7"}, "docker": "quay.io/biocontainers/r-gkmsvm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-gkmsvm.
shpc-registry automated BioContainers addition for r-gkmsvm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-gkmsvm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-gkmsvm:0.83.0--r43h21a89ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-gkmsvm/0.83.0--r43h21a89ab_0
$ module help quay.io/biocontainers/r-gkmsvm/0.83.0--r43h21a89ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-gkmsvm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-gkmsvm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-gkmsvm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-gkmsvm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-gkmsvm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-gkmsvm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-gkmsvm

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