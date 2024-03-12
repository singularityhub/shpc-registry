---
layout: container
name:  "quay.io/biocontainers/bioconductor-viseago"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-viseago/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-viseago/container.yaml"
updated_at: "2024-03-12 02:52:33.235483"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-viseago"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-viseago"
config: {"url": "https://biocontainers.pro/tools/bioconductor-viseago", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-viseago", "latest": {"1.16.0--r43hdfd78af_0": "sha256:61e2dd165de4e72d1b1bb09756f8518db51bbf5176afc58b1764cca8f12a5f82"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:d2271654e4ba6083718a806ff2bc7b02ffb84aaaed8dd3bafd763af07473ac72", "1.12.0--r42hdfd78af_0": "sha256:5efcf8bc25040516a084b330500ec0056478439e2bc83173f02b2b493655fab0", "1.14.0--r43hdfd78af_0": "sha256:02aa43e778523ce75cb68ea60b757ae17bd556d7e72ae8925b1d70f9ce3468ec", "1.16.0--r43hdfd78af_0": "sha256:61e2dd165de4e72d1b1bb09756f8518db51bbf5176afc58b1764cca8f12a5f82"}, "docker": "quay.io/biocontainers/bioconductor-viseago"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-viseago.
shpc-registry automated BioContainers addition for bioconductor-viseago
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-viseago
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-viseago:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-viseago/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-viseago/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-viseago-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-viseago-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-viseago-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-viseago-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-viseago-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-viseago-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-viseago

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