---
layout: container
name:  "quay.io/biocontainers/bioconductor-benchmarkfdrdata2019"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-benchmarkfdrdata2019/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-benchmarkfdrdata2019/container.yaml"
updated_at: "2024-03-28 02:27:53.834533"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-benchmarkfdrdata2019"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-benchmarkfdrdata2019"
config: {"url": "https://biocontainers.pro/tools/bioconductor-benchmarkfdrdata2019", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-benchmarkfdrdata2019", "latest": {"1.16.0--r43hdfd78af_0": "sha256:600db0d68a6e09a57b5b1349f3c6f5d82cb126534d2f8584e6cdb2c9f9d12525"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:8bea3722723df1fd800e892802cc4a0ccd01fbdef3ebdaf2f2fc133013391eec", "1.12.0--r42hdfd78af_0": "sha256:0b9339356f631d00e163b9a1d6d68e53d5f256e4ef20aa861eea6705ae65276d", "1.14.0--r43hdfd78af_0": "sha256:a40439dbe5a394e4adb0a7022d250279bec2f09c3fabb9453ac1e86ec012b215", "1.16.0--r43hdfd78af_0": "sha256:600db0d68a6e09a57b5b1349f3c6f5d82cb126534d2f8584e6cdb2c9f9d12525"}, "docker": "quay.io/biocontainers/bioconductor-benchmarkfdrdata2019"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-benchmarkfdrdata2019.
shpc-registry automated BioContainers addition for bioconductor-benchmarkfdrdata2019
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-benchmarkfdrdata2019
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-benchmarkfdrdata2019:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-benchmarkfdrdata2019/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-benchmarkfdrdata2019/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-benchmarkfdrdata2019-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-benchmarkfdrdata2019-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-benchmarkfdrdata2019-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-benchmarkfdrdata2019-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-benchmarkfdrdata2019-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-benchmarkfdrdata2019-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-benchmarkfdrdata2019

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