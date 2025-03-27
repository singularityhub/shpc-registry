---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu35ksubbcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu35ksubbcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu35ksubbcdf/container.yaml"
updated_at: "2025-03-27 03:35:27.755648"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hu35ksubbcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hu35ksubbcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu35ksubbcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu35ksubbcdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:be9704e483a54c2188c89afdf5682eb4efac852522e9bf32fc1b840bbaedffd2"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:b9b39155519837d2b84bd4f84fcb739e14503bfca24cc26917d911368d428f46", "2.18.0--r42hdfd78af_10": "sha256:8bff5cc038f865d2dcb97cea1add398767aa56564d5b7dbed45b3c964c48c782", "2.18.0--r43hdfd78af_11": "sha256:ace6280b748d182b1215683dd5db2c6b90bfbbd8dba1756bb852c0e7e7a186eb", "2.18.0--r43hdfd78af_12": "sha256:981538721c4865b3d18cfb4d74e9ffc4a60be32222c429b1a775407e254dcd85", "2.18.0--r44hdfd78af_13": "sha256:be9704e483a54c2188c89afdf5682eb4efac852522e9bf32fc1b840bbaedffd2"}, "docker": "quay.io/biocontainers/bioconductor-hu35ksubbcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu35ksubbcdf.
shpc-registry automated BioContainers addition for bioconductor-hu35ksubbcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubbcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubbcdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu35ksubbcdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hu35ksubbcdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu35ksubbcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubbcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubbcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu35ksubbcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu35ksubbcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu35ksubbcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu35ksubbcdf

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