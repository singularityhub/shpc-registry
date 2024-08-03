---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirna10cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirna10cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirna10cdf/container.yaml"
updated_at: "2024-08-03 02:37:38.365216"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mirna10cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mirna10cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirna10cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirna10cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:c5187ca0ea0086c0c880df054a1c9a3ab48ba0fecd4ac54a8ad23009d8c6e521"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f8fbbe6e36436de63c27eb4a6305b88fd4f98ae3e228cd12fada6d9c5be45cb2", "2.18.0--r42hdfd78af_10": "sha256:ba9edba25f2fdaf0ec3b256305e0e69a112e25f8eddda317700bef16d04752e5", "2.18.0--r43hdfd78af_11": "sha256:b8ad677a4d42c0a6cc60636c39471192dcfe973c42c5751aa283380fac1a06b5", "2.18.0--r43hdfd78af_12": "sha256:c5187ca0ea0086c0c880df054a1c9a3ab48ba0fecd4ac54a8ad23009d8c6e521"}, "docker": "quay.io/biocontainers/bioconductor-mirna10cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirna10cdf.
shpc-registry automated BioContainers addition for bioconductor-mirna10cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna10cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirna10cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirna10cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mirna10cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirna10cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna10cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirna10cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirna10cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirna10cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirna10cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirna10cdf

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