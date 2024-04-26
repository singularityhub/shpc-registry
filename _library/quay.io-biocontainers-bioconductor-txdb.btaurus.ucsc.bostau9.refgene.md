---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene/container.yaml"
updated_at: "2024-04-26 02:37:14.520817"
latest: "3.10.0--r43hdfd78af_9"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.btaurus.ucsc.bostau9.refgene"

versions:
 - "3.10.0--r41hdfd78af_6"
 - "3.10.0--r42hdfd78af_7"
 - "3.10.0--r43hdfd78af_8"
 - "3.10.0--r43hdfd78af_9"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.btaurus.ucsc.bostau9.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.btaurus.ucsc.bostau9.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.btaurus.ucsc.bostau9.refgene", "latest": {"3.10.0--r43hdfd78af_9": "sha256:3256995aabf5748098db8f610ce71e68e70d0e484b7a8e32d98f503c54e89d15"}, "tags": {"3.10.0--r41hdfd78af_6": "sha256:841ce7eb3058b58be45948921b6df93aaef36c80bb516051c40b3a7a85d257da", "3.10.0--r42hdfd78af_7": "sha256:2340df8dd2b03b2c39022b5ef114ba66ba5e4fe72dce68cf33e0a6e8f86cadb6", "3.10.0--r43hdfd78af_8": "sha256:7ee8716aa892c5fc46ac2d7d47908e8cbc2201bda472914b5b421b1ff875faca", "3.10.0--r43hdfd78af_9": "sha256:3256995aabf5748098db8f610ce71e68e70d0e484b7a8e32d98f503c54e89d15"}, "docker": "quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.btaurus.ucsc.bostau9.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene:3.10.0--r43hdfd78af_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene/3.10.0--r43hdfd78af_9
$ module help quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau9.refgene/3.10.0--r43hdfd78af_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.btaurus.ucsc.bostau9.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau9.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau9.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.btaurus.ucsc.bostau9.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau9.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau9.refgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.btaurus.ucsc.bostau9.refgene

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