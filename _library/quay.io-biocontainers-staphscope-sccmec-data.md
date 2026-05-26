---
layout: container
name:  "quay.io/biocontainers/staphscope-sccmec-data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staphscope-sccmec-data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/staphscope-sccmec-data/container.yaml"
updated_at: "2026-05-26 06:58:13.011002"
latest: "1.2.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/staphscope-sccmec-data"

versions:
 - "1.2.0--hdfd78af_1"
 - "1.2.1--hdfd78af_1"
 - "1.2.2--hdfd78af_0"
description: "singularity registry hpc automated addition for staphscope-sccmec-data"
config: {"url": "https://biocontainers.pro/tools/staphscope-sccmec-data", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for staphscope-sccmec-data", "latest": {"1.2.2--hdfd78af_0": "sha256:ecc59815847bb5155f9c6f68187f08a318963179cf0ae77557ed0ec892216aaa"}, "tags": {"1.2.0--hdfd78af_1": "sha256:131e30a08f04ec1b72f55cb8a8f92ced5fae8946605981dfb68a5d99721708fc", "1.2.1--hdfd78af_1": "sha256:31ce294468caf9828eb5f757202e0b2b7a36f4d382ed96a5248c30bcd0b4a2d5", "1.2.2--hdfd78af_0": "sha256:ecc59815847bb5155f9c6f68187f08a318963179cf0ae77557ed0ec892216aaa"}, "docker": "quay.io/biocontainers/staphscope-sccmec-data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/staphscope-sccmec-data.
singularity registry hpc automated addition for staphscope-sccmec-data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staphscope-sccmec-data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staphscope-sccmec-data:1.2.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staphscope-sccmec-data/1.2.2--hdfd78af_0
$ module help quay.io/biocontainers/staphscope-sccmec-data/1.2.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staphscope-sccmec-data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staphscope-sccmec-data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staphscope-sccmec-data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staphscope-sccmec-data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staphscope-sccmec-data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staphscope-sccmec-data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### staphscope-sccmec-data

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