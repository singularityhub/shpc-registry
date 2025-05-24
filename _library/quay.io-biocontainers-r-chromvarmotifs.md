---
layout: container
name:  "quay.io/biocontainers/r-chromvarmotifs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-chromvarmotifs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-chromvarmotifs/container.yaml"
updated_at: "2025-05-24 03:54:03.499087"
latest: "0.2.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-chromvarmotifs"

versions:
 - "0.2.0--r41hdfd78af_0"
 - "0.2.0--r42hdfd78af_0"
description: "singularity registry hpc automated addition for r-chromvarmotifs"
config: {"url": "https://biocontainers.pro/tools/r-chromvarmotifs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-chromvarmotifs", "latest": {"0.2.0--r41hdfd78af_0": "sha256:3c76f65aaf18038d487df230cb5fdda95aeda183ae262fcdc008a2cbe052e7ce"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:3c76f65aaf18038d487df230cb5fdda95aeda183ae262fcdc008a2cbe052e7ce", "0.2.0--r42hdfd78af_0": "sha256:e698b59642ca9d5c624139798614bf4c1704ce7e36eb88eaacb72ca8e9b7f2a2"}, "docker": "quay.io/biocontainers/r-chromvarmotifs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-chromvarmotifs.
singularity registry hpc automated addition for r-chromvarmotifs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-chromvarmotifs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-chromvarmotifs:0.2.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-chromvarmotifs/0.2.0--r41hdfd78af_0
$ module help quay.io/biocontainers/r-chromvarmotifs/0.2.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-chromvarmotifs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-chromvarmotifs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-chromvarmotifs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-chromvarmotifs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-chromvarmotifs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-chromvarmotifs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-chromvarmotifs

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