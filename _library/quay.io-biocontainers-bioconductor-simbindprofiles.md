---
layout: container
name:  "quay.io/biocontainers/bioconductor-simbindprofiles"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simbindprofiles/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simbindprofiles/container.yaml"
updated_at: "2024-08-12 03:27:06.177977"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simbindprofiles"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simbindprofiles"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simbindprofiles", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simbindprofiles", "latest": {"1.40.0--r43hdfd78af_0": "sha256:31bc09ec65b34c6357eb06c7a4a10ac49e19e83c1a47ac21912fd00aa0459ac0"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:226b3644c4f20f5e36b7c315c479694ed056112479bc7fb2b5a70f725b9155b5", "1.36.0--r42hdfd78af_0": "sha256:bed1fd328de26b484945ccb537869929c25d2acc753ff82e4c95364261c6e883", "1.38.0--r43hdfd78af_0": "sha256:655ae91939eadedbe2d3c6bffc4a2c966812d56632f3859c2abe1f3c211ee59b", "1.40.0--r43hdfd78af_0": "sha256:31bc09ec65b34c6357eb06c7a4a10ac49e19e83c1a47ac21912fd00aa0459ac0"}, "docker": "quay.io/biocontainers/bioconductor-simbindprofiles"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simbindprofiles.
shpc-registry automated BioContainers addition for bioconductor-simbindprofiles
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simbindprofiles
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simbindprofiles:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simbindprofiles/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-simbindprofiles/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simbindprofiles-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simbindprofiles-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simbindprofiles-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simbindprofiles-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simbindprofiles-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simbindprofiles-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-simbindprofiles

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