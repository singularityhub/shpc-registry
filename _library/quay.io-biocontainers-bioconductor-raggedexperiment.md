---
layout: container
name:  "quay.io/biocontainers/bioconductor-raggedexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-raggedexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-raggedexperiment/container.yaml"
updated_at: "2023-09-21 03:07:47.742452"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-raggedexperiment"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r40hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-raggedexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-raggedexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-raggedexperiment", "latest": {"1.24.0--r43hdfd78af_0": "sha256:14f1eda3cc982da56322a2e4450f482bd7b4d9c249cbe4d9048ad367801e66cb"}, "tags": {"1.8.0--r36_1": "sha256:08fcafd5ee52a4679de83fd64f3dffa6fe8413b2a6a4c77ede9ff0c4d5c65e89", "1.18.0--r41hdfd78af_0": "sha256:718348e009a234f2f4676f2c37ede0a4db3f1bfa6d779a1a368a60c24201601d", "1.16.0--r41hdfd78af_0": "sha256:310f0affb9a24bec39c88cd82979fef8886b8888a5618ce79a2c5a5abf1ebf0a", "1.14.1--r40hdfd78af_0": "sha256:30a282b4e6fe4f16159b8d5ce00186a058efb668c7da170d0792922d3ed60212", "1.12.0--r40_0": "sha256:99df1d37e43fa3dd566ef1fff6a1caa63c6543f56c009ed50e94a8ab16fa7f66", "1.10.0--r36_0": "sha256:078c47831fff5417244df971de4bd079452a1beb2782e0fe92d30583cc7a1c25", "1.22.0--r42hdfd78af_0": "sha256:94ee6f0d6540cfcc05cc4b6147ab2e9d5403647bb5951b80d54ac93b9bef2498", "1.24.0--r43hdfd78af_0": "sha256:14f1eda3cc982da56322a2e4450f482bd7b4d9c249cbe4d9048ad367801e66cb"}, "docker": "quay.io/biocontainers/bioconductor-raggedexperiment", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-raggedexperiment.
shpc-registry automated BioContainers addition for bioconductor-raggedexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-raggedexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-raggedexperiment:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-raggedexperiment/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-raggedexperiment/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-raggedexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-raggedexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-raggedexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-raggedexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-raggedexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-raggedexperiment-inspect-deffile:

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