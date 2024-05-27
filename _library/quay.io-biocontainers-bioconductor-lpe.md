---
layout: container
name:  "quay.io/biocontainers/bioconductor-lpe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lpe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lpe/container.yaml"
updated_at: "2024-05-27 03:47:34.241921"
latest: "1.76.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-lpe"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.76.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-lpe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lpe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lpe", "latest": {"1.76.0--r43hdfd78af_1": "sha256:8264c20df33c014b411ea53bb3563c47ef06153c1e139af6e9273503e2a40582"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:0bd68a662ea70ac0bb04730c9586910572367530f4e4bd2dafbdc51613112ae8", "1.72.0--r42hdfd78af_0": "sha256:4585eaa2728344135d6e2fccc316fe11c792f9c62ba9a9185eb96c5ca7dbb9a9", "1.74.0--r43hdfd78af_0": "sha256:eaffb86bdfecb559400bbb7c2683ef452d1642ee6746a73dbb1208c54b12e6bf", "1.76.0--r43hdfd78af_1": "sha256:8264c20df33c014b411ea53bb3563c47ef06153c1e139af6e9273503e2a40582"}, "docker": "quay.io/biocontainers/bioconductor-lpe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lpe.
shpc-registry automated BioContainers addition for bioconductor-lpe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lpe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lpe:1.76.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lpe/1.76.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-lpe/1.76.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lpe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lpe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lpe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lpe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lpe

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