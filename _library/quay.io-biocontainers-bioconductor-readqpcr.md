---
layout: container
name:  "quay.io/biocontainers/bioconductor-readqpcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-readqpcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-readqpcr/container.yaml"
updated_at: "2025-11-30 04:14:04.829623"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-readqpcr"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-readqpcr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-readqpcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-readqpcr", "latest": {"1.52.0--r44hdfd78af_0": "sha256:d97817a9f6360f1dc9db55fbd337aba005e5a46a115caafda1d8a1f7d3e4f944"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:a7c5f8a4fd6677d4859ea04af6751394a843c091456217c7d2a2f029ae60d3f5", "1.44.0--r42hdfd78af_0": "sha256:baacd40a901342653361db5329faaac9bc97887b872fd7e839ca0d4567b0f34d", "1.46.0--r43hdfd78af_0": "sha256:28a305c432207d1f3a8bae7dbfecd2a37a8e74406190ba64f7bf20b68b5e03af", "1.48.0--r43hdfd78af_0": "sha256:24861efc0cade35e2a39809e2c0968e5738e8109df4d31b387e55caefb416380", "1.52.0--r44hdfd78af_0": "sha256:d97817a9f6360f1dc9db55fbd337aba005e5a46a115caafda1d8a1f7d3e4f944"}, "docker": "quay.io/biocontainers/bioconductor-readqpcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-readqpcr.
shpc-registry automated BioContainers addition for bioconductor-readqpcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-readqpcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-readqpcr:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-readqpcr/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-readqpcr/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-readqpcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-readqpcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-readqpcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-readqpcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-readqpcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-readqpcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-readqpcr

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