---
layout: container
name:  "quay.io/biocontainers/bioconductor-sccb2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sccb2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sccb2/container.yaml"
updated_at: "2025-12-17 03:38:08.778413"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sccb2"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sccb2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sccb2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sccb2", "latest": {"1.16.0--r44hdfd78af_0": "sha256:98ce45645427328eda1ca4ed3bf852bd51ec6e8cf805a7f6e7ebdc8e1b901744"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:f1797104965483ec4c73774b4adc1ea56f6b57ca6d3e23d0984325a42d8f2329", "1.8.0--r42hdfd78af_0": "sha256:a822ba8da7e55fa0c7eeee3a6b4e09e46d6097cfc540e588a173f7c13ac7c8ab", "1.10.0--r43hdfd78af_0": "sha256:d8c5cdd5b49015d4e96b4e4e88628ff5f8ccd0ec112a60f3a6de4429330c64fb", "1.12.0--r43hdfd78af_0": "sha256:9c74d6da4e3f5042089342be4e0245dedae8adf9c3dcb9e4cf5af5a50daee181", "1.16.0--r44hdfd78af_0": "sha256:98ce45645427328eda1ca4ed3bf852bd51ec6e8cf805a7f6e7ebdc8e1b901744"}, "docker": "quay.io/biocontainers/bioconductor-sccb2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sccb2.
shpc-registry automated BioContainers addition for bioconductor-sccb2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sccb2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sccb2:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sccb2/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sccb2/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sccb2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sccb2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sccb2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sccb2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sccb2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sccb2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sccb2

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