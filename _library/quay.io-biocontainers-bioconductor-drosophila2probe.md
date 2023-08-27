---
layout: container
name:  "quay.io/biocontainers/bioconductor-drosophila2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drosophila2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drosophila2probe/container.yaml"
updated_at: "2023-08-27 03:14:09.090417"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-drosophila2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-drosophila2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drosophila2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drosophila2probe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:18c7be32a2e1964bd45b79890298458909faeed0d3d03c64cf1d77e9f00e6655"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:4e681b739520ec5db6d4414c46f7470cbfaaff280a91413791b4c3315bfb7fa0", "2.18.0--r42hdfd78af_10": "sha256:a62d94b1122d02f31aa5f695f6f68bd698dd5649db776f249b07f1c401615c31", "2.18.0--r43hdfd78af_11": "sha256:18c7be32a2e1964bd45b79890298458909faeed0d3d03c64cf1d77e9f00e6655"}, "docker": "quay.io/biocontainers/bioconductor-drosophila2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drosophila2probe.
shpc-registry automated BioContainers addition for bioconductor-drosophila2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drosophila2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drosophila2probe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drosophila2probe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-drosophila2probe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drosophila2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosophila2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosophila2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drosophila2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drosophila2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drosophila2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-drosophila2probe

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