---
layout: container
name:  "quay.io/biocontainers/bioconductor-trio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trio/container.yaml"
updated_at: "2024-12-18 03:14:20.871629"
latest: "3.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trio"

versions:
 - "3.32.0--r41hdfd78af_0"
 - "3.36.0--r42hdfd78af_0"
 - "3.38.0--r43hdfd78af_0"
 - "3.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trio"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trio", "latest": {"3.40.0--r43hdfd78af_0": "sha256:30b2c9ce5f4fa40c3dfc73b24085694de1c040a29d462b66f45ff9b96b6b158f"}, "tags": {"3.32.0--r41hdfd78af_0": "sha256:a0878477ae311fa4aef6c283ae6d26f4230b416c25b541adbe57e51258464e81", "3.36.0--r42hdfd78af_0": "sha256:0ee7ab80e1459023ca89ac2259bde069c6769d3391d6dcdf54440b99f89c6692", "3.38.0--r43hdfd78af_0": "sha256:f18fcc8ee30d646716ca4541a16d72d3f0ef19fdd6192a6c043f8ac8c624c2b0", "3.40.0--r43hdfd78af_0": "sha256:30b2c9ce5f4fa40c3dfc73b24085694de1c040a29d462b66f45ff9b96b6b158f"}, "docker": "quay.io/biocontainers/bioconductor-trio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trio.
shpc-registry automated BioContainers addition for bioconductor-trio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trio:3.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trio/3.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trio/3.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-trio

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