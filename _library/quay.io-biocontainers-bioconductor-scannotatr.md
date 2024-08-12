---
layout: container
name:  "quay.io/biocontainers/bioconductor-scannotatr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scannotatr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scannotatr/container.yaml"
updated_at: "2024-08-12 03:43:39.164310"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scannotatr"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scannotatr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scannotatr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scannotatr", "latest": {"1.8.0--r43hdfd78af_0": "sha256:6b65aacdbd8dbd3f0a79dd648d1c320b67b979160bac986a506f07a5b5c46a5d"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:b841f43b16cb98d525845f0a56ca5008ca0d8c54fe87036cae50f4a187ab8ffe", "1.4.0--r42hdfd78af_0": "sha256:144f50e295c71c785e9d61d1cbc3dee9a154642aace32258bcfafb58d5e64e30", "1.6.0--r43hdfd78af_0": "sha256:ed1fa2fe30e051f21f4b976959155aa31e638fc64429c0414d022267f2167e44", "1.8.0--r43hdfd78af_0": "sha256:6b65aacdbd8dbd3f0a79dd648d1c320b67b979160bac986a506f07a5b5c46a5d"}, "docker": "quay.io/biocontainers/bioconductor-scannotatr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scannotatr.
shpc-registry automated BioContainers addition for bioconductor-scannotatr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scannotatr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scannotatr:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scannotatr/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scannotatr/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scannotatr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scannotatr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scannotatr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scannotatr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scannotatr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scannotatr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scannotatr

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