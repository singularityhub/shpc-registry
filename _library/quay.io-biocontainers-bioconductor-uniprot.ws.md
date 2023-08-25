---
layout: container
name:  "quay.io/biocontainers/bioconductor-uniprot.ws"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-uniprot.ws/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-uniprot.ws/container.yaml"
updated_at: "2023-08-25 02:45:46.395307"
latest: "2.40.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-uniprot.ws"

versions:
 - "2.34.0--r41hdfd78af_0"
 - "2.38.0--r42hdfd78af_0"
 - "2.40.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-uniprot.ws"
config: {"url": "https://biocontainers.pro/tools/bioconductor-uniprot.ws", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-uniprot.ws", "latest": {"2.40.1--r43hdfd78af_0": "sha256:69688e7c5b8c6a3a83973712234f277cd1d7bf6d1f6ecaf8deb95fa1764d79bd"}, "tags": {"2.34.0--r41hdfd78af_0": "sha256:2e84af438953e016df793a551b6f2d0a43a8c93a4b9dbeb4e0bd79faf7ca9778", "2.38.0--r42hdfd78af_0": "sha256:7839abe6f394b17fa3af15322074fd3db4f4eafe5611416967a79b90cb157395", "2.40.1--r43hdfd78af_0": "sha256:69688e7c5b8c6a3a83973712234f277cd1d7bf6d1f6ecaf8deb95fa1764d79bd"}, "docker": "quay.io/biocontainers/bioconductor-uniprot.ws"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-uniprot.ws.
shpc-registry automated BioContainers addition for bioconductor-uniprot.ws
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-uniprot.ws
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-uniprot.ws:2.40.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-uniprot.ws/2.40.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-uniprot.ws/2.40.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-uniprot.ws-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-uniprot.ws-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-uniprot.ws-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-uniprot.ws-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-uniprot.ws-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-uniprot.ws-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-uniprot.ws

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