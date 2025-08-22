---
layout: container
name:  "quay.io/biocontainers/bioconductor-geva"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geva/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geva/container.yaml"
updated_at: "2025-08-22 03:46:07.294258"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geva"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geva"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geva", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geva", "latest": {"1.14.0--r44hdfd78af_0": "sha256:2cdf99d8547f785c217d478d18950b5b3d8ea86b4e2bc060bf355c845421ee3c"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:3bc85396a228782fecc837d99e89b11b34657945592b81344a24ad86c517e05d", "1.6.0--r42hdfd78af_0": "sha256:ac563017dad7ea32352b05ae930bb310b0c8238e7249ec783480dcb7798ece29", "1.8.0--r43hdfd78af_0": "sha256:b3c786b36f2b755c23a797ec94ee18795682fd697b847b45bc2761838ea50118", "1.10.0--r43hdfd78af_0": "sha256:a26f469b6bfceb8d6edc29aad6ef3e0b2685ee9c4b515675579cfd2670e7c206", "1.14.0--r44hdfd78af_0": "sha256:2cdf99d8547f785c217d478d18950b5b3d8ea86b4e2bc060bf355c845421ee3c"}, "docker": "quay.io/biocontainers/bioconductor-geva"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geva.
shpc-registry automated BioContainers addition for bioconductor-geva
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geva
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geva:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geva/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geva/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geva-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geva-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geva-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geva-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geva-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geva-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geva

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