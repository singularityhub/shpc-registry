---
layout: container
name:  "quay.io/biocontainers/bioconductor-tmexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tmexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tmexplorer/container.yaml"
updated_at: "2023-12-20 04:16:10.269101"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tmexplorer"

versions:
 - "1.4.0--r41hdfd78af_1"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tmexplorer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tmexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tmexplorer", "latest": {"1.12.0--r43hdfd78af_0": "sha256:838933b562b34aee70425affca3fd63fbdd7318eba591f1ae9b91ddaf2794919"}, "tags": {"1.4.0--r41hdfd78af_1": "sha256:67a00176f095280bc961c04f779720c36ef808f17aacf2f7930935b5a77471b7", "1.8.0--r42hdfd78af_0": "sha256:46e045e21a5459674699a89e65f9f85b1686d6f691f38f40b91a59cd8e2648fa", "1.10.0--r43hdfd78af_0": "sha256:4449e17cc9ac0682f0bd303f1082737dd7851117f1ae9fd6146445479c226a68", "1.12.0--r43hdfd78af_0": "sha256:838933b562b34aee70425affca3fd63fbdd7318eba591f1ae9b91ddaf2794919"}, "docker": "quay.io/biocontainers/bioconductor-tmexplorer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tmexplorer.
shpc-registry automated BioContainers addition for bioconductor-tmexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tmexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tmexplorer:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tmexplorer/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tmexplorer/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tmexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tmexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tmexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tmexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tmexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tmexplorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tmexplorer

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