---
layout: container
name:  "quay.io/biocontainers/r-restfulr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-restfulr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-restfulr/container.yaml"
updated_at: "2025-02-08 03:20:21.717192"
latest: "0.0.15--r44h5ef9028_5"
container_url: "https://biocontainers.pro/tools/r-restfulr"

versions:
 - "0.0.15--r41h73dbb54_0"
 - "0.0.15--r42h73dbb54_1"
 - "0.0.15--r42h56115f1_2"
 - "0.0.15--r43h56115f1_3"
 - "0.0.15--r43h56115f1_4"
 - "0.0.15--r44h5ef9028_5"
description: "shpc-registry automated BioContainers addition for r-restfulr"
config: {"url": "https://biocontainers.pro/tools/r-restfulr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-restfulr", "latest": {"0.0.15--r44h5ef9028_5": "sha256:7d4c33a1a9fd7a77c6387cf004a133d68b590bcc55aa29590b29182abcbf3672"}, "tags": {"0.0.15--r41h73dbb54_0": "sha256:340fa0079df70852cfeda06b7b65b587920b430198631b2a51cff6b1281b16df", "0.0.15--r42h73dbb54_1": "sha256:5c1c466da19a9dd64c7913eaca2d62025efc0a70176f4f0947072c46b74f8568", "0.0.15--r42h56115f1_2": "sha256:e99253362d746e4be9c5966bebf9a20915579a6dda095bc1f13b376651e65a59", "0.0.15--r43h56115f1_3": "sha256:425129327d8e3dca29f39dbe88be581a6a7df68013d54db299a4122c1e16c0b3", "0.0.15--r43h56115f1_4": "sha256:652de562cdce491ca77380359d5748a8aed98f25960803d4bd215dd50105ff97", "0.0.15--r44h5ef9028_5": "sha256:7d4c33a1a9fd7a77c6387cf004a133d68b590bcc55aa29590b29182abcbf3672"}, "docker": "quay.io/biocontainers/r-restfulr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-restfulr.
shpc-registry automated BioContainers addition for r-restfulr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-restfulr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-restfulr:0.0.15--r44h5ef9028_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-restfulr/0.0.15--r44h5ef9028_5
$ module help quay.io/biocontainers/r-restfulr/0.0.15--r44h5ef9028_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-restfulr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-restfulr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-restfulr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-restfulr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-restfulr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-restfulr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-restfulr

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