---
layout: container
name:  "quay.io/biocontainers/bioconductor-reactomegsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-reactomegsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-reactomegsa/container.yaml"
updated_at: "2025-07-28 04:33:03.438824"
latest: "1.16.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-reactomegsa"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-reactomegsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-reactomegsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-reactomegsa", "latest": {"1.16.1--r43hdfd78af_0": "sha256:da99b0663ed9bc60aedd78b97bf31573a45e5e11157cdc213323314c553f62f7"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:c31c9458e2973401ae72935862f215e9cc83e77d6a32e4db395a14db75038a2b", "1.12.0--r42hdfd78af_0": "sha256:bab307c623f5c49f168891bcdc0013a8554ba2eb2b90447d94a2489903e00616", "1.14.0--r43hdfd78af_0": "sha256:8f27411f574dd2b7f6563ed4077edc78024b8dad473d00451dc6079b9349e96e", "1.16.1--r43hdfd78af_0": "sha256:da99b0663ed9bc60aedd78b97bf31573a45e5e11157cdc213323314c553f62f7"}, "docker": "quay.io/biocontainers/bioconductor-reactomegsa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-reactomegsa.
shpc-registry automated BioContainers addition for bioconductor-reactomegsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-reactomegsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-reactomegsa:1.16.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-reactomegsa/1.16.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-reactomegsa/1.16.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-reactomegsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reactomegsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reactomegsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-reactomegsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-reactomegsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-reactomegsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-reactomegsa

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