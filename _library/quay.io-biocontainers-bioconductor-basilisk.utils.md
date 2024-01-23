---
layout: container
name:  "quay.io/biocontainers/bioconductor-basilisk.utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-basilisk.utils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-basilisk.utils/container.yaml"
updated_at: "2024-01-23 02:44:53.549678"
latest: "1.14.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-basilisk.utils"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.1--r43hdfd78af_0"
 - "1.14.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-basilisk.utils"
config: {"url": "https://biocontainers.pro/tools/bioconductor-basilisk.utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-basilisk.utils", "latest": {"1.14.1--r43hdfd78af_0": "sha256:b6c79940d9094db5fa7a222fc8d7f4b9eb3e336f4ccb632fcc31ff6763a01cab"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:53c76e81260bd5473c294a5a36806daa731d74f89cdb4a46c55d29675bb8bae6", "1.10.0--r42hdfd78af_0": "sha256:07229edd6b355ef2e99935162ecbdfeae5f45e0e5916e04d17ac26d1b6e3c2c7", "1.12.1--r43hdfd78af_0": "sha256:13127287c88c49f0f0968a478125decc5e83e494f6e324106966bbfc15027863", "1.14.1--r43hdfd78af_0": "sha256:b6c79940d9094db5fa7a222fc8d7f4b9eb3e336f4ccb632fcc31ff6763a01cab"}, "docker": "quay.io/biocontainers/bioconductor-basilisk.utils"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-basilisk.utils.
shpc-registry automated BioContainers addition for bioconductor-basilisk.utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-basilisk.utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-basilisk.utils:1.14.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-basilisk.utils/1.14.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-basilisk.utils/1.14.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-basilisk.utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basilisk.utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basilisk.utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-basilisk.utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-basilisk.utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-basilisk.utils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-basilisk.utils

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