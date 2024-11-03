---
layout: container
name:  "quay.io/biocontainers/bioconductor-biscuiteerdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biscuiteerdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biscuiteerdata/container.yaml"
updated_at: "2024-11-03 03:22:57.266717"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biscuiteerdata"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.1--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biscuiteerdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biscuiteerdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biscuiteerdata", "latest": {"1.16.0--r43hdfd78af_0": "sha256:226c77c2936e010124c317c6898f26fee25f3e41d61ddf29c8c6c77b5ff9ec67"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:2a1e30640b7e361eb353527a7ee5a4e42b5f1a0a3d72676554ed125b149ee071", "1.12.0--r42hdfd78af_0": "sha256:cddc19beaf22821c96c06ed8af8483e0c8ecd2238e9cd087e077d5b38eca266f", "1.14.1--r43hdfd78af_0": "sha256:a0c4b032836dfa621676ddd69a4a067c4761db6f3f831068f3a532718848dd29", "1.16.0--r43hdfd78af_0": "sha256:226c77c2936e010124c317c6898f26fee25f3e41d61ddf29c8c6c77b5ff9ec67"}, "docker": "quay.io/biocontainers/bioconductor-biscuiteerdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biscuiteerdata.
shpc-registry automated BioContainers addition for bioconductor-biscuiteerdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biscuiteerdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biscuiteerdata:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biscuiteerdata/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biscuiteerdata/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biscuiteerdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biscuiteerdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biscuiteerdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biscuiteerdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biscuiteerdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biscuiteerdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biscuiteerdata

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