---
layout: container
name:  "quay.io/biocontainers/bioconductor-beadarrayexampledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beadarrayexampledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beadarrayexampledata/container.yaml"
updated_at: "2023-12-25 02:34:41.534860"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-beadarrayexampledata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-beadarrayexampledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beadarrayexampledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beadarrayexampledata", "latest": {"1.40.0--r43hdfd78af_0": "sha256:1f1f47bc736b49c5e57214f91779493bf42f4553f61fb89dc3e3e901fe63b355"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:51786ff7d1f6dad02a1f5b568c7d1d6ab01d8b464b921b37654e6bda245905d7", "1.36.0--r42hdfd78af_0": "sha256:4a8e43cbf3f2c621bc97e865bd03fc64261cfab17b14d448d9f3553e24661003", "1.38.0--r43hdfd78af_0": "sha256:ea36d73d4b9ed0722b3d6976568bf9be5b92b0326a527b2456fea3a30bd7f513", "1.40.0--r43hdfd78af_0": "sha256:1f1f47bc736b49c5e57214f91779493bf42f4553f61fb89dc3e3e901fe63b355"}, "docker": "quay.io/biocontainers/bioconductor-beadarrayexampledata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beadarrayexampledata.
shpc-registry automated BioContainers addition for bioconductor-beadarrayexampledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarrayexampledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarrayexampledata:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beadarrayexampledata/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-beadarrayexampledata/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beadarrayexampledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarrayexampledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarrayexampledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beadarrayexampledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beadarrayexampledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beadarrayexampledata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-beadarrayexampledata

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