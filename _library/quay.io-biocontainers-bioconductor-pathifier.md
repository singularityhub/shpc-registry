---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathifier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathifier/container.yaml"
updated_at: "2025-04-20 03:28:06.144056"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathifier"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathifier"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathifier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathifier", "latest": {"1.44.0--r44hdfd78af_0": "sha256:3de6ff1bd1e9e704fd6220704d13bd94c3bc5fbd82b407f4bd1106c0f0ccb004"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:2de8ba184502b024d6144cd1f4469d74acdd21a84cb98ac9a57d6613513505e7", "1.36.0--r42hdfd78af_0": "sha256:6b8dafdbd80c48abf8751efdd0b389dd5118dc89b4d6be03436bc5db9c668874", "1.38.0--r43hdfd78af_0": "sha256:8cec56c84bf4572b0de85d0e10620dcb72bb66c3cad2b9a749c1de7be566379f", "1.40.0--r43hdfd78af_0": "sha256:ea00555f49be8977beab07fa6e8299c0fa595d80a335a680140d86cb2b7258e4", "1.44.0--r44hdfd78af_0": "sha256:3de6ff1bd1e9e704fd6220704d13bd94c3bc5fbd82b407f4bd1106c0f0ccb004"}, "docker": "quay.io/biocontainers/bioconductor-pathifier"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathifier.
shpc-registry automated BioContainers addition for bioconductor-pathifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathifier:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathifier/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pathifier/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathifier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pathifier

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