---
layout: container
name:  "quay.io/biocontainers/bioconductor-msqc1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msqc1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msqc1/container.yaml"
updated_at: "2025-02-26 02:57:51.171073"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msqc1"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.25.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msqc1"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msqc1", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msqc1", "latest": {"1.34.0--r44hdfd78af_0": "sha256:e5eb4cce000cb28fdf8716fc0d431e3b8572675a57e6e0012a0e046d0895e53f"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:5d83c51e814c32c9df09bb08621dd6acac192f8d1052db3bb16ca4dff5efca2c", "1.25.0--r42hdfd78af_0": "sha256:1817513467827fbf60fc3f5c34628bddaf5468fa29a3b8acb81ac8897cad458c", "1.28.0--r43hdfd78af_0": "sha256:dc55d5482544c3a79fe0f88b58f2a6946c2181891cbe4d636d1487625fae2c46", "1.30.0--r43hdfd78af_0": "sha256:5b4e1d466b4e82a948912fb3b2330f5acd03504218e70ab079fc5379794c723f", "1.34.0--r44hdfd78af_0": "sha256:e5eb4cce000cb28fdf8716fc0d431e3b8572675a57e6e0012a0e046d0895e53f"}, "docker": "quay.io/biocontainers/bioconductor-msqc1"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msqc1.
shpc-registry automated BioContainers addition for bioconductor-msqc1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msqc1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msqc1:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msqc1/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msqc1/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msqc1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msqc1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msqc1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msqc1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msqc1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msqc1-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msqc1

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