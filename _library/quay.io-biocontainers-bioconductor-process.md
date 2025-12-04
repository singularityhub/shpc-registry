---
layout: container
name:  "quay.io/biocontainers/bioconductor-process"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-process/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-process/container.yaml"
updated_at: "2025-12-04 04:14:49.036749"
latest: "1.82.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-process"

versions:
 - "1.70.0--r41hdfd78af_0"
 - "1.74.0--r42hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
 - "1.82.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-process"
config: {"url": "https://biocontainers.pro/tools/bioconductor-process", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-process", "latest": {"1.82.0--r44hdfd78af_0": "sha256:578c10d9b7b7c935a3d682eb3c5caf6b4532ac8dc179539f80d60d1849483e3a"}, "tags": {"1.70.0--r41hdfd78af_0": "sha256:b9508b3f6fa4bc635cd05232199eae182a1b5a66299a14e6791feaf39e629a43", "1.74.0--r42hdfd78af_0": "sha256:54e1f382d1dff3d9b27e504760537414cfcae3e9b70a89d851ecc65c43f563c5", "1.76.0--r43hdfd78af_0": "sha256:002eed6bc15eddccc699447c38c25a25df12fa9a924dbae29023aac129499a93", "1.78.0--r43hdfd78af_0": "sha256:939553da25ee12c33b0ba12c472bb6190f73e9159b5948f291ba5d99f6ea9606", "1.82.0--r44hdfd78af_0": "sha256:578c10d9b7b7c935a3d682eb3c5caf6b4532ac8dc179539f80d60d1849483e3a"}, "docker": "quay.io/biocontainers/bioconductor-process"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-process.
shpc-registry automated BioContainers addition for bioconductor-process
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-process
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-process:1.82.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-process/1.82.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-process/1.82.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-process-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-process-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-process-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-process-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-process-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-process-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-process

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