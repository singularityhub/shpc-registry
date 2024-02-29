---
layout: container
name:  "quay.io/biocontainers/bioconductor-weaver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-weaver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-weaver/container.yaml"
updated_at: "2024-02-29 02:48:46.521995"
latest: "1.68.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-weaver"

versions:
 - "1.60.0--r41hdfd78af_0"
 - "1.64.0--r42hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-weaver"
config: {"url": "https://biocontainers.pro/tools/bioconductor-weaver", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-weaver", "latest": {"1.68.0--r43hdfd78af_0": "sha256:4aa94d5da76e16943c94686790c8462e5e5a4d56901cee890a573febaad99094"}, "tags": {"1.60.0--r41hdfd78af_0": "sha256:2a5289ca6d6de44780af130ad8901fccc99d01ab7161e1687b3f19136061f0a8", "1.64.0--r42hdfd78af_0": "sha256:40519960a7696ff68a8ee6109a22e586fc4648763ac2e23134367c48fd772426", "1.66.0--r43hdfd78af_0": "sha256:2f21dbcd86cd6e0c25a9d0219e43539d8a83eac001aa22707ddbc2d7fb5ff5a5", "1.68.0--r43hdfd78af_0": "sha256:4aa94d5da76e16943c94686790c8462e5e5a4d56901cee890a573febaad99094"}, "docker": "quay.io/biocontainers/bioconductor-weaver"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-weaver.
shpc-registry automated BioContainers addition for bioconductor-weaver
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-weaver
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-weaver:1.68.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-weaver/1.68.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-weaver/1.68.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-weaver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-weaver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-weaver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-weaver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-weaver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-weaver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-weaver

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