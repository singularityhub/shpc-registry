---
layout: container
name:  "quay.io/biocontainers/bioconductor-interactivedisplaybase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-interactivedisplaybase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-interactivedisplaybase/container.yaml"
updated_at: "2025-12-04 03:28:58.103830"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-interactivedisplaybase"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-interactivedisplaybase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-interactivedisplaybase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-interactivedisplaybase", "latest": {"1.44.0--r44hdfd78af_0": "sha256:8aecc52b7ff28181e3f8bbf9c2730fc17029ce9344090fb97899047daaff9feb"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:78dccc73ae8c866a2ec5d7a7c8a0fdcc66ef3514cb800ca83ee2d3c0f49299a3", "1.36.0--r42hdfd78af_0": "sha256:d62d31e5d599df6265aa11381052038f884415ec498a1ac0ca6e9a9709961621", "1.38.0--r43hdfd78af_0": "sha256:2275037c5d5314fb632b3f1c462996ffaca588c230d5bf52acf68bcc146946e9", "1.40.0--r43hdfd78af_0": "sha256:de15d0588ed673e06ea35f5faf9fd5573253a9845d6b2792dc40afe5ff72a9c6", "1.44.0--r44hdfd78af_0": "sha256:8aecc52b7ff28181e3f8bbf9c2730fc17029ce9344090fb97899047daaff9feb"}, "docker": "quay.io/biocontainers/bioconductor-interactivedisplaybase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-interactivedisplaybase.
shpc-registry automated BioContainers addition for bioconductor-interactivedisplaybase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-interactivedisplaybase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-interactivedisplaybase:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-interactivedisplaybase/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-interactivedisplaybase/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-interactivedisplaybase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interactivedisplaybase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-interactivedisplaybase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-interactivedisplaybase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-interactivedisplaybase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-interactivedisplaybase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-interactivedisplaybase

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