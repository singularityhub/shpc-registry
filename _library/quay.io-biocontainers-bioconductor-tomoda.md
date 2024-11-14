---
layout: container
name:  "quay.io/biocontainers/bioconductor-tomoda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tomoda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tomoda/container.yaml"
updated_at: "2024-11-14 04:11:01.402621"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tomoda"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tomoda"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tomoda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tomoda", "latest": {"1.12.0--r43hdfd78af_0": "sha256:476d40620d700a2fe795241582f9fff973fc6a6961d5810055f938c685d549aa"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:7c2e38c08d77b595b190f68cc0f81c8cd6160c27679767bab628a84f4f04daf2", "1.8.0--r42hdfd78af_0": "sha256:7a6feb84a085909de807a6510761a4a6d52e9b4ad4641d712d41dc0dcb3622d6", "1.10.0--r43hdfd78af_0": "sha256:bb3fb10a9683b52448430e8c9924f040ba1103ec8c94e785054a8e8ca370da5e", "1.12.0--r43hdfd78af_0": "sha256:476d40620d700a2fe795241582f9fff973fc6a6961d5810055f938c685d549aa"}, "docker": "quay.io/biocontainers/bioconductor-tomoda"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tomoda.
shpc-registry automated BioContainers addition for bioconductor-tomoda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tomoda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tomoda:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tomoda/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tomoda/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tomoda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tomoda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tomoda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tomoda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tomoda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tomoda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tomoda

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