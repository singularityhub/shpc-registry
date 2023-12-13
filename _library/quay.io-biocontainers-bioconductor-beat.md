---
layout: container
name:  "quay.io/biocontainers/bioconductor-beat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beat/container.yaml"
updated_at: "2023-12-13 03:10:19.844211"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-beat"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-beat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beat", "latest": {"1.38.0--r43hdfd78af_0": "sha256:6ed60b8cca4fa6c1950baf9177aceb6941979650b5317dd5f6511844087d0b65"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:e5159a2671fe112ac661cd9f37dabf6606a4c1db6f4944adbb812b636fbcc173", "1.36.0--r42hdfd78af_0": "sha256:294dd532404186773d682f97fea71c1e9bf9459dc7aa99fb218b6ab53467d7d8", "1.38.0--r43hdfd78af_0": "sha256:6ed60b8cca4fa6c1950baf9177aceb6941979650b5317dd5f6511844087d0b65"}, "docker": "quay.io/biocontainers/bioconductor-beat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beat.
shpc-registry automated BioContainers addition for bioconductor-beat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beat:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beat/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-beat/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-beat

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