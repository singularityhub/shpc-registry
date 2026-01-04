---
layout: container
name:  "quay.io/biocontainers/bioconductor-rocpai"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rocpai/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rocpai/container.yaml"
updated_at: "2026-01-04 04:38:51.628964"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rocpai"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rocpai"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rocpai", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rocpai", "latest": {"1.14.0--r43hdfd78af_0": "sha256:55093d55fb00cb0c603908f3a0262625327aa4c95ee734e6c90d5159b3cee0c8"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:bf8d1dc125126feff57d61c043f17ba7094315ffa931387ea7f27d0447cafcf6", "1.10.0--r42hdfd78af_0": "sha256:670984783a268a0e50e30f1857602ca20a7d6ac9470b29e28a7b573d93895270", "1.12.0--r43hdfd78af_0": "sha256:3d3226d69bf5aaa697753368e18935ddbbab873a502c14d9f2a67f922af92965", "1.14.0--r43hdfd78af_0": "sha256:55093d55fb00cb0c603908f3a0262625327aa4c95ee734e6c90d5159b3cee0c8"}, "docker": "quay.io/biocontainers/bioconductor-rocpai"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rocpai.
shpc-registry automated BioContainers addition for bioconductor-rocpai
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rocpai
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rocpai:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rocpai/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rocpai/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rocpai-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rocpai-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rocpai-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rocpai-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rocpai-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rocpai-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rocpai

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