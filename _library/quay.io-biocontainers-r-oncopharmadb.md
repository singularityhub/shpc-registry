---
layout: container
name:  "quay.io/biocontainers/r-oncopharmadb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-oncopharmadb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-oncopharmadb/container.yaml"
updated_at: "2024-06-27 03:44:58.202699"
latest: "1.5.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-oncopharmadb"

versions:
 - "0.0.1--r41hdfd78af_0"
 - "0.0.1--r42hdfd78af_1"
 - "1.3.7--r43hdfd78af_0"
 - "1.4.4--r43hdfd78af_0"
 - "1.4.6--r43hdfd78af_0"
 - "1.5.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-oncopharmadb"
config: {"url": "https://biocontainers.pro/tools/r-oncopharmadb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-oncopharmadb", "latest": {"1.5.1--r43hdfd78af_0": "sha256:eefa4d051be97fc0736c9cf38d9c482ba4c6aeb0c0b1c57a0bf717e9226477f1"}, "tags": {"0.0.1--r41hdfd78af_0": "sha256:56797dcc6b0023a99f2a9dc17c4d9aff82b7e6e8eb3372f2e0521f91a3de0b13", "0.0.1--r42hdfd78af_1": "sha256:a427831d8f317c805e09f0c8f4b3632056ec2a33efdf3f5e00da004c89340d84", "1.3.7--r43hdfd78af_0": "sha256:36c0ed84349d78d960d32909e59969e1d345d7dc06a0a800602ff10c38ea68f8", "1.4.4--r43hdfd78af_0": "sha256:d88ae239b0c31a3b652bb65dfe4ceefa09bf97ed2bea2954acebbc4327cdccc8", "1.4.6--r43hdfd78af_0": "sha256:067054a0d6816b98eabdac46be7fd101a566eef09c418888d505ebe80a3d5d0a", "1.5.1--r43hdfd78af_0": "sha256:eefa4d051be97fc0736c9cf38d9c482ba4c6aeb0c0b1c57a0bf717e9226477f1"}, "docker": "quay.io/biocontainers/r-oncopharmadb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-oncopharmadb.
shpc-registry automated BioContainers addition for r-oncopharmadb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-oncopharmadb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-oncopharmadb:1.5.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-oncopharmadb/1.5.1--r43hdfd78af_0
$ module help quay.io/biocontainers/r-oncopharmadb/1.5.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-oncopharmadb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-oncopharmadb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-oncopharmadb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-oncopharmadb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-oncopharmadb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-oncopharmadb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-oncopharmadb

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