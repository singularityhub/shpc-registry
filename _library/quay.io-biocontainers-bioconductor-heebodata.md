---
layout: container
name:  "quay.io/biocontainers/bioconductor-heebodata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-heebodata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-heebodata/container.yaml"
updated_at: "2025-08-23 03:23:38.832287"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-heebodata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-heebodata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-heebodata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-heebodata", "latest": {"1.44.0--r44hdfd78af_0": "sha256:277e460d34f0ed4c037558ed3e368c91eeb2d887a1446316067592c4da20fe59"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:019cf87a86a879654c107a461ceae33a42f695301a97b7ce670a8f4a11f2d66b", "1.35.0--r42hdfd78af_0": "sha256:bb1c936768a90bd050ff5bc6b09a6ba7bbd5e358966730139083a44d4ed33d06", "1.38.0--r43hdfd78af_0": "sha256:723a0092be9d6fabd828f2a131ad478498424725c70ed740d9e8f0d71daa6d0c", "1.40.0--r43hdfd78af_0": "sha256:c0e710123d0dc7d404f8359853117ddcceb5e1ab47a0ac4906602532b0065c94", "1.44.0--r44hdfd78af_0": "sha256:277e460d34f0ed4c037558ed3e368c91eeb2d887a1446316067592c4da20fe59"}, "docker": "quay.io/biocontainers/bioconductor-heebodata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-heebodata.
shpc-registry automated BioContainers addition for bioconductor-heebodata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-heebodata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-heebodata:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-heebodata/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-heebodata/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-heebodata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-heebodata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-heebodata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-heebodata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-heebodata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-heebodata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-heebodata

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