---
layout: container
name:  "quay.io/biocontainers/bioconductor-mspuritydata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mspuritydata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mspuritydata/container.yaml"
updated_at: "2025-04-11 03:48:44.336182"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mspuritydata"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_1"
 - "1.25.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_1"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_0"
 - "1.17.0--r40_0"
 - "1.26.0--r42hdfd78af_1"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mspuritydata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mspuritydata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mspuritydata", "latest": {"1.34.0--r44hdfd78af_0": "sha256:f5383de06e55e1fe2f09fe3e8a72eb8277c59f94ec30b93b0bc4f312be0f69db"}, "tags": {"1.8.0--r351_1": "sha256:66d750cb0bd95b2b6c953a90c21220c4ea2d0cd03f154695c5104f4cc5cd9722", "1.25.0--r42hdfd78af_0": "sha256:0c0ea25816219068915a8ea15d6c22343b7f731731cc11dd2afa99a28ec53843", "1.22.0--r41hdfd78af_1": "sha256:39b057323d6513a70705eba0cbc173d41f77620b74c767c500f6b935c8cd7193", "1.20.0--r41hdfd78af_0": "sha256:d72b6d2efcb48c2d80a56b05091b424e37ed19de40bad3c2ac0453198f010cb2", "1.18.0--r40hdfd78af_0": "sha256:dbe78efa597ddeeb8cb40037f295277fb6ef4292ec9c5c090a964b819f863ea0", "1.17.0--r40_0": "sha256:7ad5426adea173fea856cfd1cfa56be3c15d3f1a6f3d3b7cc9bbcf1471a25005", "1.26.0--r42hdfd78af_1": "sha256:550851787641f8a6a164508f5af9ef30a48029a5e1506e7c4546088aa9d89cf7", "1.28.0--r43hdfd78af_0": "sha256:1e79f792ca921fb433edd27e7d32d94c61ecca6a2cb1d85da2499216b1363be5", "1.30.0--r43hdfd78af_0": "sha256:d8163a1bb0495acd1bfa0a2f1455cd76fd3da829e2978bad9be5a9b6cbb0e13c", "1.34.0--r44hdfd78af_0": "sha256:f5383de06e55e1fe2f09fe3e8a72eb8277c59f94ec30b93b0bc4f312be0f69db"}, "docker": "quay.io/biocontainers/bioconductor-mspuritydata", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mspuritydata.
shpc-registry automated BioContainers addition for bioconductor-mspuritydata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mspuritydata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mspuritydata:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mspuritydata/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mspuritydata/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mspuritydata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mspuritydata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mspuritydata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mspuritydata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mspuritydata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mspuritydata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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