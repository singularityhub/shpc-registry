---
layout: container
name:  "quay.io/biocontainers/bioconductor-tomatoprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tomatoprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tomatoprobe/container.yaml"
updated_at: "2023-11-03 03:10:37.651182"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-tomatoprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-tomatoprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tomatoprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tomatoprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:c394d2831c51265926985ec2eac7897a287252e4b589da18c14cd837a7e563d0"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:cec0c6d05ce08e195140488df3e609f0e4352f1df8d49896902958eb4931bf3d", "2.18.0--r42hdfd78af_10": "sha256:94b97f635d075b13d27efc5da41304ce1e417d1fbfc481622057a13ce4ff1175", "2.18.0--r43hdfd78af_11": "sha256:c394d2831c51265926985ec2eac7897a287252e4b589da18c14cd837a7e563d0"}, "docker": "quay.io/biocontainers/bioconductor-tomatoprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tomatoprobe.
shpc-registry automated BioContainers addition for bioconductor-tomatoprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tomatoprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tomatoprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tomatoprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-tomatoprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tomatoprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tomatoprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tomatoprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tomatoprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tomatoprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tomatoprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tomatoprobe

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