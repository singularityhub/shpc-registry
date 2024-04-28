---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedovariandata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedovariandata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedovariandata/container.yaml"
updated_at: "2024-04-28 02:48:16.687127"
latest: "1.40.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedovariandata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedovariandata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedovariandata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedovariandata", "latest": {"1.40.1--r43hdfd78af_0": "sha256:c9a40b86c8aeac632c7113ec530e2112626ddf934eb6763b05b58ef57a8ab96b"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:51881a8658749c63a8757c5f565121586b26a0ace3978252c7838b77de9061e7", "1.36.0--r42hdfd78af_0": "sha256:01ad8594de63d543c841949444ef6ebd47791c50c6e49f35d8a7a7ceffecf22a", "1.38.0--r43hdfd78af_0": "sha256:7ebbe11e68453b32a6da98297a22b99ccc4a95222deec95dfe803182dbe61250", "1.40.1--r43hdfd78af_0": "sha256:c9a40b86c8aeac632c7113ec530e2112626ddf934eb6763b05b58ef57a8ab96b"}, "docker": "quay.io/biocontainers/bioconductor-curatedovariandata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedovariandata.
shpc-registry automated BioContainers addition for bioconductor-curatedovariandata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedovariandata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedovariandata:1.40.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedovariandata/1.40.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedovariandata/1.40.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedovariandata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedovariandata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedovariandata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedovariandata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedovariandata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedovariandata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-curatedovariandata

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