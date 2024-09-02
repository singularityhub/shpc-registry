---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomewidesnp6crlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomewidesnp6crlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomewidesnp6crlmm/container.yaml"
updated_at: "2024-09-02 04:21:48.220360"
latest: "1.0.7--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-genomewidesnp6crlmm"

versions:
 - "1.0.7--r41hdfd78af_9"
 - "1.0.7--r42hdfd78af_10"
 - "1.0.7--r43hdfd78af_11"
 - "1.0.7--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-genomewidesnp6crlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomewidesnp6crlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomewidesnp6crlmm", "latest": {"1.0.7--r43hdfd78af_12": "sha256:6c4b451068e43e005ef9090a7b53c89274a717022905809cfe01984aaeb28282"}, "tags": {"1.0.7--r41hdfd78af_9": "sha256:f445455a18f9d4be1183c9010b41085ac54391c28bdda59d5247828b1bc99a3c", "1.0.7--r42hdfd78af_10": "sha256:a48d16b712c8992819543c3ce43616d62ca140bb84b55289ff5ec14aa45fce19", "1.0.7--r43hdfd78af_11": "sha256:bdc170ec10204dd8b72d640ec8876576e2cabdf1a00ed0599aab229d69976113", "1.0.7--r43hdfd78af_12": "sha256:6c4b451068e43e005ef9090a7b53c89274a717022905809cfe01984aaeb28282"}, "docker": "quay.io/biocontainers/bioconductor-genomewidesnp6crlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomewidesnp6crlmm.
shpc-registry automated BioContainers addition for bioconductor-genomewidesnp6crlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomewidesnp6crlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomewidesnp6crlmm:1.0.7--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomewidesnp6crlmm/1.0.7--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-genomewidesnp6crlmm/1.0.7--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomewidesnp6crlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomewidesnp6crlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomewidesnp6crlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomewidesnp6crlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomewidesnp6crlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomewidesnp6crlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomewidesnp6crlmm

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