---
layout: container
name:  "quay.io/biocontainers/microhapulator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/microhapulator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/microhapulator/container.yaml"
updated_at: "2025-03-06 03:27:09.726366"
latest: "0.8.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/microhapulator"
aliases:
 - "happer"
 - "iss"
 - "mhpl8r"
 - "termgraph"
 - "stone"
 - "flash"
 - "plac_runner.py"
 - "yte"
 - "docutils"
 - "x86_64-conda_cos7-linux-gnu-ld"
 - "jpackage"
 - "fastqc"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
versions:
 - "0.7.2--pyhdfd78af_0"
 - "0.8--pyhdfd78af_0"
 - "0.8.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for microhapulator"
config: {"url": "https://biocontainers.pro/tools/microhapulator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for microhapulator", "latest": {"0.8.4--pyhdfd78af_0": "sha256:975970262dda49228070e14a708c29a387889831ea0a2d34d16e170f90c221ae"}, "tags": {"0.7.2--pyhdfd78af_0": "sha256:c542f99626c3034d8042a28174a40f661b8318e039ebc46dbe51818f481f9973", "0.8--pyhdfd78af_0": "sha256:4438b2011c92edeb4c6848ad082e8b61038b25b859a8239a9ea49670cd61b12e", "0.8.4--pyhdfd78af_0": "sha256:975970262dda49228070e14a708c29a387889831ea0a2d34d16e170f90c221ae"}, "docker": "quay.io/biocontainers/microhapulator", "aliases": {"happer": "/usr/local/bin/happer", "iss": "/usr/local/bin/iss", "mhpl8r": "/usr/local/bin/mhpl8r", "termgraph": "/usr/local/bin/termgraph", "stone": "/usr/local/bin/stone", "flash": "/usr/local/bin/flash", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "docutils": "/usr/local/bin/docutils", "x86_64-conda_cos7-linux-gnu-ld": "/usr/local/bin/x86_64-conda_cos7-linux-gnu-ld", "jpackage": "/usr/local/bin/jpackage", "fastqc": "/usr/local/bin/fastqc", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/microhapulator.
shpc-registry automated BioContainers addition for microhapulator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/microhapulator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/microhapulator:0.8.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/microhapulator/0.8.4--pyhdfd78af_0
$ module help quay.io/biocontainers/microhapulator/0.8.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### microhapulator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### microhapulator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### microhapulator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### microhapulator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### microhapulator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### microhapulator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### happer

```bash
$ singularity exec <container> /usr/local/bin/happer
$ podman run --it --rm --entrypoint /usr/local/bin/happer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/happer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iss

```bash
$ singularity exec <container> /usr/local/bin/iss
$ podman run --it --rm --entrypoint /usr/local/bin/iss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhpl8r

```bash
$ singularity exec <container> /usr/local/bin/mhpl8r
$ podman run --it --rm --entrypoint /usr/local/bin/mhpl8r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhpl8r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### termgraph

```bash
$ singularity exec <container> /usr/local/bin/termgraph
$ podman run --it --rm --entrypoint /usr/local/bin/termgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/termgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flash

```bash
$ singularity exec <container> /usr/local/bin/flash
$ podman run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos7-linux-gnu-ld

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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