---
layout: container
name:  "quay.io/biocontainers/vcfpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcfpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcfpy/container.yaml"
updated_at: "2024-09-12 03:04:28.465488"
latest: "0.13.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/vcfpy"

versions:
 - "0.13.4--pyhdfd78af_0"
 - "0.13.5--pyhdfd78af_0"
 - "0.13.6--pyhdfd78af_0"
 - "0.13.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for vcfpy"
config: {"url": "https://biocontainers.pro/tools/vcfpy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcfpy", "latest": {"0.13.8--pyhdfd78af_0": "sha256:ee4705716c61e4e9c9b97335e36aed1b979109408a2bef3610d23b3d60197917"}, "tags": {"0.13.4--pyhdfd78af_0": "sha256:bd650b279f85c24c8f3626893213f521159322b0209fc5029efa997f2ffac033", "0.13.5--pyhdfd78af_0": "sha256:f34797abe6f0f65697ecb9caf8300d68122ea96e12beb2f86faff6f072ad3878", "0.13.6--pyhdfd78af_0": "sha256:bf89f7bc5545f59705e640d3077f8837950c08f7103c7cf182b2311f1a6ffd85", "0.13.8--pyhdfd78af_0": "sha256:ee4705716c61e4e9c9b97335e36aed1b979109408a2bef3610d23b3d60197917"}, "docker": "quay.io/biocontainers/vcfpy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcfpy.
shpc-registry automated BioContainers addition for vcfpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcfpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcfpy:0.13.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcfpy/0.13.8--pyhdfd78af_0
$ module help quay.io/biocontainers/vcfpy/0.13.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcfpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcfpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcfpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcfpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcfpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcfpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### vcfpy

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