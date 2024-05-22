---
layout: container
name:  "quay.io/biocontainers/r-acidgenerics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidgenerics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidgenerics/container.yaml"
updated_at: "2024-05-22 03:06:12.227716"
latest: "0.7.8--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidgenerics"

versions:
 - "0.6.0--r41hdfd78af_0"
 - "0.6.5--r42hdfd78af_0"
 - "0.6.6--r42hdfd78af_0"
 - "0.6.6--r42hdfd78af_1"
 - "0.6.7--r42hdfd78af_0"
 - "0.6.7--r43hdfd78af_1"
 - "0.6.7--r43hdfd78af_2"
 - "0.6.11--r43hdfd78af_0"
 - "0.7.3--r43hdfd78af_0"
 - "0.6.12--r43hdfd78af_0"
 - "0.7.6--r43hdfd78af_0"
 - "0.7.7--r43hdfd78af_0"
 - "0.7.8--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidgenerics"
config: {"url": "https://biocontainers.pro/tools/r-acidgenerics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidgenerics", "latest": {"0.7.8--r43hdfd78af_0": "sha256:1f274a70de6212c911345edbf27502c140448d05d02d36c96c0d2c8d772f41b9"}, "tags": {"0.6.0--r41hdfd78af_0": "sha256:5aecd9de123be462df57a67f21f21e4120ae904213ec2257935a228f93cc982e", "0.6.5--r42hdfd78af_0": "sha256:eb404b2df7f957fe5ec4ae9b5a3a2c4df0fdd81e8688bac22425e62738a0b664", "0.6.6--r42hdfd78af_0": "sha256:ba82417bd0ce82db4c572afb7882c08552393edeeb7c005837909c86cf07ccdd", "0.6.6--r42hdfd78af_1": "sha256:1ff8f30101a5f8884c96b8dd29e304640fbaa764b2c25aea58e21933e51e0c3d", "0.6.7--r42hdfd78af_0": "sha256:dbe8c7c1023f081e981128e60ce920417d7c004e046d6623cb5c8315eace4dcd", "0.6.7--r43hdfd78af_1": "sha256:40fc111b6a990b80beb9ef0b92f9353f24dbe0019524d869acdb90a81952ddb2", "0.6.7--r43hdfd78af_2": "sha256:3fe18f554cb8dd481d98bac4c9d57a8bb278ba1825e6df8bcf8c00e06bdf8ba0", "0.6.11--r43hdfd78af_0": "sha256:f837967eb5d24a9e26aec9d813abd8e0bcf87c99ad24d89d75a9494a5b67a34a", "0.7.3--r43hdfd78af_0": "sha256:2b1c79014c0a6e4aab544af4f7f3c75d0c953afaa2ad5a1e2065908d2c69d279", "0.6.12--r43hdfd78af_0": "sha256:2c8db74568c0bf58305cdcb64450cafca325d14e72e8aec60e4bcebdcaf135a4", "0.7.6--r43hdfd78af_0": "sha256:2ff7ef9036d8814da2d8c92484ac91a42b04b62e8a65f6cbb7d1ccf0357dc557", "0.7.7--r43hdfd78af_0": "sha256:8eaa9a667d87985cbe29343eacd86bf0ff75f22e807a46d47866b079d64343b3", "0.7.8--r43hdfd78af_0": "sha256:1f274a70de6212c911345edbf27502c140448d05d02d36c96c0d2c8d772f41b9"}, "docker": "quay.io/biocontainers/r-acidgenerics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidgenerics.
shpc-registry automated BioContainers addition for r-acidgenerics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidgenerics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidgenerics:0.7.8--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidgenerics/0.7.8--r43hdfd78af_0
$ module help quay.io/biocontainers/r-acidgenerics/0.7.8--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidgenerics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidgenerics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidgenerics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidgenerics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidgenerics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidgenerics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidgenerics

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