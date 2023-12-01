---
layout: container
name:  "quay.io/biocontainers/sdm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sdm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sdm/container.yaml"
updated_at: "2023-12-01 03:19:15.050919"
latest: "2.14--hdcf5f25_0"
container_url: "https://biocontainers.pro/tools/sdm"
aliases:
 - "sdm"
versions:
 - "2.02--hd03093a_1"
 - "2.05--hd03093a_0"
 - "2.06--hd03093a_0"
 - "2.08--hdcf5f25_2"
 - "2.09--hdcf5f25_0"
 - "2.10--hdcf5f25_0"
 - "2.13--hdcf5f25_0"
 - "2.11--hdcf5f25_0"
 - "2.14--hdcf5f25_0"
description: "shpc-registry automated BioContainers addition for sdm"
config: {"url": "https://biocontainers.pro/tools/sdm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sdm", "latest": {"2.14--hdcf5f25_0": "sha256:c89a527b9dd3b0d8f7ca45fa3a403a042f7e0a41799d8861684431300da0843b"}, "tags": {"2.02--hd03093a_1": "sha256:0db36867d5ebc88fedb13104f0cd5fe18c7a4c03d0ee8ea02b6c014c6bb47743", "2.05--hd03093a_0": "sha256:b5c541c136474e94901c2ab190aeb606c92ac93382a9a0e035845cd54c326c36", "2.06--hd03093a_0": "sha256:d9351b5c4555a87da0a8e0a3aa12e74986b5b77831eeb23d685e3f6d400d721d", "2.08--hdcf5f25_2": "sha256:a4ddf7fe302e3af22ab00355bc2d9c05cd2f7d1882ada2c8229dc7ac9e51b7be", "2.09--hdcf5f25_0": "sha256:f7b25701917aadde9009da7ce315ba26ead6ea6bf4d63ce41bf5cae9406701ba", "2.10--hdcf5f25_0": "sha256:0374080632f42638849b0d345b8c42a6a35b20e72172eb60883416e349ca8b17", "2.13--hdcf5f25_0": "sha256:6be101bd16bcda4fc6a9badfc20ad36bfc3c9bc4e847c7f60036536d8d6954ba", "2.11--hdcf5f25_0": "sha256:76dc01bf0a640b000415674619ebe4397c055389cf08d79c208a756319aa6841", "2.14--hdcf5f25_0": "sha256:c89a527b9dd3b0d8f7ca45fa3a403a042f7e0a41799d8861684431300da0843b"}, "docker": "quay.io/biocontainers/sdm", "aliases": {"sdm": "/usr/local/bin/sdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sdm.
shpc-registry automated BioContainers addition for sdm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sdm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sdm:2.14--hdcf5f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sdm/2.14--hdcf5f25_0
$ module help quay.io/biocontainers/sdm/2.14--hdcf5f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sdm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sdm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sdm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sdm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sdm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sdm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sdm

```bash
$ singularity exec <container> /usr/local/bin/sdm
$ podman run --it --rm --entrypoint /usr/local/bin/sdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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