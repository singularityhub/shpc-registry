---
layout: container
name:  "quay.io/biocontainers/bioconductor-zellkonverter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-zellkonverter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-zellkonverter/container.yaml"
updated_at: "2024-11-14 04:47:35.358459"
latest: "1.12.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-zellkonverter"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
 - "1.12.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-zellkonverter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-zellkonverter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-zellkonverter", "latest": {"1.12.1--r43hdfd78af_0": "sha256:9df6b1944329e1690eecb6c8896421f4bfffc68e95b1a12ca65330bfad8de29f"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:3e2864fd74b6299c5b04b9fada95caeee13b8dba6169096e41f7500d966e44b0", "1.8.0--r42hdfd78af_0": "sha256:87ae0f4521990faebc0d9c35d78b965612224b8a7315a36b5039f5ae846d5cf7", "1.10.1--r43hdfd78af_0": "sha256:5d968b651fcd4a952e9cb4f66b77864e4700b8fde9794828acd30732277c9035", "1.12.1--r43hdfd78af_0": "sha256:9df6b1944329e1690eecb6c8896421f4bfffc68e95b1a12ca65330bfad8de29f"}, "docker": "quay.io/biocontainers/bioconductor-zellkonverter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-zellkonverter.
shpc-registry automated BioContainers addition for bioconductor-zellkonverter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-zellkonverter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-zellkonverter:1.12.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-zellkonverter/1.12.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-zellkonverter/1.12.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-zellkonverter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zellkonverter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zellkonverter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-zellkonverter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-zellkonverter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-zellkonverter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-zellkonverter

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