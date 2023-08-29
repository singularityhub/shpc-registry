---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedbladderdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedbladderdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedbladderdata/container.yaml"
updated_at: "2023-08-29 03:32:01.960921"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedbladderdata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedbladderdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedbladderdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedbladderdata", "latest": {"1.36.0--r43hdfd78af_0": "sha256:8aeb7b004d69f12749d1781b313f79c72710c871f4a0893fb26b76d8403115a2"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:ed4a523db9f37dbc89890af9c08c7ce51e7adef1395ab07d12439796c69c2a22", "1.34.0--r42hdfd78af_0": "sha256:a9d62a2e0c14fca3943e1b119782af31c1f5ac6a5e27a123b5f1e22db5016d11", "1.36.0--r43hdfd78af_0": "sha256:8aeb7b004d69f12749d1781b313f79c72710c871f4a0893fb26b76d8403115a2"}, "docker": "quay.io/biocontainers/bioconductor-curatedbladderdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedbladderdata.
shpc-registry automated BioContainers addition for bioconductor-curatedbladderdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedbladderdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedbladderdata:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedbladderdata/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedbladderdata/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedbladderdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedbladderdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedbladderdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedbladderdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedbladderdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedbladderdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-curatedbladderdata

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