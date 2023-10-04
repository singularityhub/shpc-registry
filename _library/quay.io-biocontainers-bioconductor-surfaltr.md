---
layout: container
name:  "quay.io/biocontainers/bioconductor-surfaltr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-surfaltr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-surfaltr/container.yaml"
updated_at: "2023-10-04 02:44:24.218035"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-surfaltr"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-surfaltr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-surfaltr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-surfaltr", "latest": {"1.6.0--r43hdfd78af_0": "sha256:1069541a2b44d9feb80cf7ee49772050978011824a0c0002ac437a5a8f781ec7"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:8573b883470c3229652491205865a9f421e377ce67a1c8ad1316715040527c54", "1.4.0--r42hdfd78af_0": "sha256:956b8f5894523fb98aa36e6c74b997cc87d886d0e0540212151331e78d611a53", "1.6.0--r43hdfd78af_0": "sha256:1069541a2b44d9feb80cf7ee49772050978011824a0c0002ac437a5a8f781ec7"}, "docker": "quay.io/biocontainers/bioconductor-surfaltr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-surfaltr.
shpc-registry automated BioContainers addition for bioconductor-surfaltr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-surfaltr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-surfaltr:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-surfaltr/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-surfaltr/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-surfaltr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-surfaltr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-surfaltr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-surfaltr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-surfaltr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-surfaltr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-surfaltr

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