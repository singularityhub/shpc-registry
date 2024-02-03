---
layout: container
name:  "quay.io/biocontainers/bioconductor-wavcluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-wavcluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-wavcluster/container.yaml"
updated_at: "2024-02-03 02:52:08.810207"
latest: "2.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-wavcluster"

versions:
 - "2.28.0--r41hdfd78af_0"
 - "2.32.0--r42hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
 - "2.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-wavcluster"
config: {"url": "https://biocontainers.pro/tools/bioconductor-wavcluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-wavcluster", "latest": {"2.36.0--r43hdfd78af_0": "sha256:0dd544d30a203c67b6b00e992126efd6601b8829339612e072906fcac70032f5"}, "tags": {"2.28.0--r41hdfd78af_0": "sha256:1ef5ef0be5ffff0074ee06ee69fcbaa960df625305810f903f475051b3118d8d", "2.32.0--r42hdfd78af_0": "sha256:79ff13bde9ed7813d5aeed3d1de55b82297e977b28c22bf92bbf90a3ced960d9", "2.34.0--r43hdfd78af_0": "sha256:9e9a214fc7b076698f89514cb78e3653fee9350a963442d27102287d373a44f1", "2.36.0--r43hdfd78af_0": "sha256:0dd544d30a203c67b6b00e992126efd6601b8829339612e072906fcac70032f5"}, "docker": "quay.io/biocontainers/bioconductor-wavcluster"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-wavcluster.
shpc-registry automated BioContainers addition for bioconductor-wavcluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-wavcluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-wavcluster:2.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-wavcluster/2.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-wavcluster/2.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-wavcluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wavcluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wavcluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-wavcluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-wavcluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-wavcluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-wavcluster

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