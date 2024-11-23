---
layout: container
name:  "quay.io/biocontainers/bioconductor-cogena"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cogena/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cogena/container.yaml"
updated_at: "2024-11-23 03:22:00.915641"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cogena"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cogena"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cogena", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cogena", "latest": {"1.36.0--r43hdfd78af_0": "sha256:f5a3f37afa300f0041ac6582ff353b438c6243f2eb600f218bdda9a0de79a0ce"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:63da5554e96b3c7c27c5eb8dfb7292721822e2c10102587d7edaf6631fb21e28", "1.32.0--r42hdfd78af_0": "sha256:c1a45d4bcc6d4f985b719520f7618ba9fe7656ba447a26604c4b7c8b8f401cd1", "1.34.0--r43hdfd78af_0": "sha256:8fb6917d622d0dc22849b3925155329dbc0805fe49ecf037188c432107c1dcb0", "1.36.0--r43hdfd78af_0": "sha256:f5a3f37afa300f0041ac6582ff353b438c6243f2eb600f218bdda9a0de79a0ce"}, "docker": "quay.io/biocontainers/bioconductor-cogena"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cogena.
shpc-registry automated BioContainers addition for bioconductor-cogena
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cogena
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cogena:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cogena/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cogena/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cogena-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogena-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cogena-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cogena-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cogena-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cogena-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cogena

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