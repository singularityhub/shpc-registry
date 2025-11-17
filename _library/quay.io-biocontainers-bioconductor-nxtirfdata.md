---
layout: container
name:  "quay.io/biocontainers/bioconductor-nxtirfdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nxtirfdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nxtirfdata/container.yaml"
updated_at: "2025-11-17 04:45:41.544277"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nxtirfdata"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nxtirfdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nxtirfdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nxtirfdata", "latest": {"1.12.0--r44hdfd78af_0": "sha256:91a99f03be6b3477c509ae87e6b2d35b35a64eb0b0b31280b52be2431c4da005"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:d26ba19cda272edea0e6abd384f072b0bc42456cc2e7a9ac43681fdbc96e51af", "1.4.0--r42hdfd78af_0": "sha256:59230306267bd4c5d6a321f835b9d4de39052a4122496793a126531a1a5c65e2", "1.6.0--r43hdfd78af_0": "sha256:841856c22a00e76bcadc2329126876c243f2547fe637d4658679e68508a30697", "1.8.0--r43hdfd78af_0": "sha256:8fe5a5c527e82d2b5b69dcd006cf0b56f6dc7a0e581738870dfd8dca82a34070", "1.12.0--r44hdfd78af_0": "sha256:91a99f03be6b3477c509ae87e6b2d35b35a64eb0b0b31280b52be2431c4da005"}, "docker": "quay.io/biocontainers/bioconductor-nxtirfdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nxtirfdata.
shpc-registry automated BioContainers addition for bioconductor-nxtirfdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nxtirfdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nxtirfdata:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nxtirfdata/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nxtirfdata/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nxtirfdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nxtirfdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nxtirfdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nxtirfdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nxtirfdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nxtirfdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nxtirfdata

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