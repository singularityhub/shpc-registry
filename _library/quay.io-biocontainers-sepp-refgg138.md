---
layout: container
name:  "quay.io/biocontainers/sepp-refgg138"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sepp-refgg138/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sepp-refgg138/container.yaml"
updated_at: "2023-09-14 03:34:21.678352"
latest: "4.5.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/sepp-refgg138"

versions:
 - "v4.3.6--0"
 - "4.5.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for sepp-refgg138"
config: {"url": "https://biocontainers.pro/tools/sepp-refgg138", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sepp-refgg138", "latest": {"4.5.1--hdfd78af_1": "sha256:4b170a7388b79c8bdf90931d896e05f2460e26dc3f300217c485d52587d2e34e"}, "tags": {"v4.3.6--0": "sha256:f721c73a1303d78648291763f2f0dbe601b3636b9fed8f98f825ee92e05ace0b", "4.5.1--hdfd78af_1": "sha256:4b170a7388b79c8bdf90931d896e05f2460e26dc3f300217c485d52587d2e34e"}, "docker": "quay.io/biocontainers/sepp-refgg138"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sepp-refgg138.
shpc-registry automated BioContainers addition for sepp-refgg138
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sepp-refgg138
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sepp-refgg138:4.5.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sepp-refgg138/4.5.1--hdfd78af_1
$ module help quay.io/biocontainers/sepp-refgg138/4.5.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sepp-refgg138-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sepp-refgg138-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sepp-refgg138-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sepp-refgg138-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sepp-refgg138-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sepp-refgg138-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### sepp-refgg138

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