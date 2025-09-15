---
layout: container
name:  "quay.io/biocontainers/bioconductor-sqldataframe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sqldataframe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sqldataframe/container.yaml"
updated_at: "2025-09-15 03:38:09.684719"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sqldataframe"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sqldataframe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sqldataframe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sqldataframe", "latest": {"1.20.0--r44hdfd78af_0": "sha256:ac2a93cf5d2309216cac706d1d05b09ad6846d6d96beee36ec2ef229716cedbd"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:9f8b0a2de15fc3ca513fe9f8afd6ccf8d2b2bf55062c88253b1966b25675aece", "1.12.0--r42hdfd78af_0": "sha256:5cb8595c9237b0676bce2e1356579517c4362d7c0665ef26abd602392428dade", "1.14.0--r43hdfd78af_0": "sha256:84df052a74e8d60a436ffa82e03a72715180970ad18c903607b56ed698e670ca", "1.16.0--r43hdfd78af_0": "sha256:2ff8ca4f8d535ec09def785ef8f416eedcec61f8d54da782dd43baff1419c217", "1.20.0--r44hdfd78af_0": "sha256:ac2a93cf5d2309216cac706d1d05b09ad6846d6d96beee36ec2ef229716cedbd"}, "docker": "quay.io/biocontainers/bioconductor-sqldataframe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sqldataframe.
shpc-registry automated BioContainers addition for bioconductor-sqldataframe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sqldataframe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sqldataframe:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sqldataframe/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sqldataframe/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sqldataframe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sqldataframe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sqldataframe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sqldataframe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sqldataframe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sqldataframe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sqldataframe

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