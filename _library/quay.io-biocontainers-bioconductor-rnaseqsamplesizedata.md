---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaseqsamplesizedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaseqsamplesizedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaseqsamplesizedata/container.yaml"
updated_at: "2025-02-13 03:13:35.274499"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaseqsamplesizedata"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.30.0--r42hdfd78af_1"
 - "1.29.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaseqsamplesizedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaseqsamplesizedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaseqsamplesizedata", "latest": {"1.38.0--r44hdfd78af_0": "sha256:78202c7eeaeea41709ac9b0671cc287f52d03ce1deaa5f7b0d90f6a72f3d8a8f"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:79893ccbe82c7526490da4ebcaa793d74ca18d77e17bf325f5787d23281d91e6", "1.30.0--r42hdfd78af_1": "sha256:bef58b5e269bf2e0c2a8a5446a0e836b16368c1866e13be2f3a6fee0e8a0bdc1", "1.29.0--r42hdfd78af_0": "sha256:6daf0d8d6c53a6162982cb5db0cd6461b5640e8cf15cb6023a242f231216815c", "1.32.0--r43hdfd78af_0": "sha256:96e366e3d9a58af61f0e8e75f1801f68ea2c83883fd46bffe2c0d9f7caace0d0", "1.34.0--r43hdfd78af_0": "sha256:d6b0ee34fbb56242f251d28aee3e697822f52745d80de2157287aa124468a742", "1.38.0--r44hdfd78af_0": "sha256:78202c7eeaeea41709ac9b0671cc287f52d03ce1deaa5f7b0d90f6a72f3d8a8f"}, "docker": "quay.io/biocontainers/bioconductor-rnaseqsamplesizedata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaseqsamplesizedata.
shpc-registry automated BioContainers addition for bioconductor-rnaseqsamplesizedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqsamplesizedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqsamplesizedata:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaseqsamplesizedata/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnaseqsamplesizedata/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaseqsamplesizedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqsamplesizedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqsamplesizedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaseqsamplesizedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaseqsamplesizedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaseqsamplesizedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnaseqsamplesizedata

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