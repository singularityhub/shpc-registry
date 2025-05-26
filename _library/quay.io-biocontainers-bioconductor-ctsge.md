---
layout: container
name:  "quay.io/biocontainers/bioconductor-ctsge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ctsge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ctsge/container.yaml"
updated_at: "2025-05-26 11:54:54.713738"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ctsge"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ctsge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ctsge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ctsge", "latest": {"1.32.0--r44hdfd78af_0": "sha256:2f7cd4bc77cad77e858bcdee558e74b5165b9e13c7e8697f2b67ada23564b79b"}, "tags": {"1.8.1--r351_0": "sha256:2da997a9fbecc6915fb1610235ba733cb7038fab43bb3fecc7257b831477497d", "1.24.0--r42hdfd78af_0": "sha256:9fdcbd93b80b65786ef7f8067a8ad3e2c4b94f2b1c4b189a7444de4f77440db8", "1.20.0--r41hdfd78af_0": "sha256:e5edbdfce7acb5e5ce0ca214d4c1d29559d5c05c33c394028d753b81059e0d2c", "1.18.0--r41hdfd78af_0": "sha256:70b6d04911bd140a92be1cedf60fa6f8d6c92aab6e67e025e4344d115e71ace4", "1.16.0--r40hdfd78af_1": "sha256:0169bd37eae43c20090ff1f73b24535d6eb26c0ac5f17a09817e70023068bb46", "1.14.0--r40_0": "sha256:7b54ff74a94ada6c8b3b4ac6d0cc1af7ceb14c4dfa249296c79d2a0136e15a5c", "1.26.0--r43hdfd78af_0": "sha256:07e8a95ae5629438fb5d749a7f04fe5790c25eb515772d9aeadd4abac0a52f77", "1.28.0--r43hdfd78af_0": "sha256:829e3669777b4cd28d88235a4414883f993efeb7d1c4371d1dd2b5ecb040fc0d", "1.32.0--r44hdfd78af_0": "sha256:2f7cd4bc77cad77e858bcdee558e74b5165b9e13c7e8697f2b67ada23564b79b"}, "docker": "quay.io/biocontainers/bioconductor-ctsge", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ctsge.
shpc-registry automated BioContainers addition for bioconductor-ctsge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ctsge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ctsge:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ctsge/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ctsge/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ctsge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctsge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctsge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ctsge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ctsge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ctsge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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