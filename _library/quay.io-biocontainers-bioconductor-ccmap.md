---
layout: container
name:  "quay.io/biocontainers/bioconductor-ccmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ccmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ccmap/container.yaml"
updated_at: "2024-02-23 02:31:17.012746"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ccmap"
aliases:
 - "xgboost"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ccmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ccmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ccmap", "latest": {"1.28.0--r43hdfd78af_0": "sha256:7b20d0f38cb7801d4c96cf5b68e722345b007568c5485d3bbcf906402e5a416c"}, "tags": {"1.8.0--r351_0": "sha256:61d80e33375347b1bdc5352c969f0e14b66e5f14365ee27d12bf522dd63e9ba3", "1.24.0--r42hdfd78af_0": "sha256:9d08c47c68686fd6fb97a92418f52e6c5f691d313f9da8f5a6dbd7e5f055300f", "1.20.0--r41hdfd78af_0": "sha256:ee276f515331c4d5e772e972ba8c75f31f72aca1f1c549615027ca4813875f4d", "1.18.0--r41hdfd78af_0": "sha256:9ae35af46bf72cdae7ee75fe8ecdaca561fa8c404f790e93a70ebc2cf3c6a4fe", "1.16.0--r40hdfd78af_1": "sha256:27fa27081fcaa9261de55e7e6d0a5811bbc616aa8c5197baf7ba03c35d719cbf", "1.14.0--r40_0": "sha256:f89e6db26222b7d77d69521d70e037ea350d8075d0a7a4a2a3a77692fb2818a0", "1.28.0--r43hdfd78af_0": "sha256:7b20d0f38cb7801d4c96cf5b68e722345b007568c5485d3bbcf906402e5a416c"}, "docker": "quay.io/biocontainers/bioconductor-ccmap", "aliases": {"xgboost": "/usr/local/bin/xgboost", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ccmap.
shpc-registry automated BioContainers addition for bioconductor-ccmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ccmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ccmap:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ccmap/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ccmap/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ccmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ccmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ccmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ccmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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