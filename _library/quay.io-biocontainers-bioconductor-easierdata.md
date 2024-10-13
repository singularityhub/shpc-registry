---
layout: container
name:  "quay.io/biocontainers/bioconductor-easierdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-easierdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-easierdata/container.yaml"
updated_at: "2024-10-13 11:20:42.941025"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-easierdata"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-easierdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-easierdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-easierdata", "latest": {"1.8.0--r43hdfd78af_0": "sha256:1ed47e268a5450f8f976772a7b9694a23032260a789e1625f4ab16aa90aa9aaa"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:a6f5c0f095c7b2e1672b72be58abc57867d705333a20e5467c6b68c9daad1d20", "1.4.0--r42hdfd78af_0": "sha256:7ea4fc7e52f55426654c1519ecc488bba2c4564510c9a85bb0f97037be804b75", "1.6.0--r43hdfd78af_0": "sha256:2324c4cab55cae9ba6e885a839e490d8d2717df2cbb32a439acdd4a4af863bd1", "1.8.0--r43hdfd78af_0": "sha256:1ed47e268a5450f8f976772a7b9694a23032260a789e1625f4ab16aa90aa9aaa"}, "docker": "quay.io/biocontainers/bioconductor-easierdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-easierdata.
shpc-registry automated BioContainers addition for bioconductor-easierdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-easierdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-easierdata:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-easierdata/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-easierdata/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-easierdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easierdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easierdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-easierdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-easierdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-easierdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-easierdata

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