---
layout: container
name:  "quay.io/biocontainers/bioconductor-velociraptor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-velociraptor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-velociraptor/container.yaml"
updated_at: "2023-10-04 04:51:49.584544"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-velociraptor"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-velociraptor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-velociraptor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-velociraptor", "latest": {"1.10.0--r43hdfd78af_0": "sha256:d8e487ae88664ee3f76c3f554110ba1262f8b4c2965e52763a822d949f631813"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:44faf5989df8b6091a74f6ecb9bc17b8ede99bd67af8384915d41eb0eeb9a0ea", "1.8.0--r42hdfd78af_0": "sha256:dfdf5c113c6526bdc5d22f0b81959ab55587f9b7ddd62da70e22c95a50945ca2", "1.10.0--r43hdfd78af_0": "sha256:d8e487ae88664ee3f76c3f554110ba1262f8b4c2965e52763a822d949f631813"}, "docker": "quay.io/biocontainers/bioconductor-velociraptor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-velociraptor.
shpc-registry automated BioContainers addition for bioconductor-velociraptor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-velociraptor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-velociraptor:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-velociraptor/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-velociraptor/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-velociraptor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-velociraptor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-velociraptor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-velociraptor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-velociraptor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-velociraptor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-velociraptor

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