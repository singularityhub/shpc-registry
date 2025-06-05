---
layout: container
name:  "quay.io/biocontainers/r-bcbiobase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bcbiobase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-bcbiobase/container.yaml"
updated_at: "2025-06-05 12:44:23.811844"
latest: "0.9.0--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-bcbiobase"

versions:
 - "0.7.0--r41hdfd78af_0"
 - "0.8.1--r42hdfd78af_1"
 - "0.8.1--r43hdfd78af_2"
 - "0.8.2--r43hdfd78af_0"
 - "0.9.0--r43hdfd78af_0"
 - "0.9.0--r44hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-bcbiobase"
config: {"url": "https://biocontainers.pro/tools/r-bcbiobase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bcbiobase", "latest": {"0.9.0--r44hdfd78af_1": "sha256:a5530e11d86a2e78396708b276ee41f91209c0117f2909243873d3bfc5a72b85"}, "tags": {"0.7.0--r41hdfd78af_0": "sha256:3761c429d7dcb4ccec936dba50465eacab01281cb0efa98826791784897c53b3", "0.8.1--r42hdfd78af_1": "sha256:8b43644670f137d6113ddd3cbd56cf54d17b95b9085cacada0732737f528ceb2", "0.8.1--r43hdfd78af_2": "sha256:883dc301349138cd7c25290fb2112a0ef3323077f98a5bbca0a4dca692bcb3f2", "0.8.2--r43hdfd78af_0": "sha256:cba61e5e18cd81d4b90de076b97e4e8da38ec69975d71037d30ed6235fee97ad", "0.9.0--r43hdfd78af_0": "sha256:b87fa6a491430931a72ac4df67d3e30de9f67642a00d15271f336c3ec78ff8bd", "0.9.0--r44hdfd78af_1": "sha256:a5530e11d86a2e78396708b276ee41f91209c0117f2909243873d3bfc5a72b85"}, "docker": "quay.io/biocontainers/r-bcbiobase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bcbiobase.
shpc-registry automated BioContainers addition for r-bcbiobase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bcbiobase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bcbiobase:0.9.0--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bcbiobase/0.9.0--r44hdfd78af_1
$ module help quay.io/biocontainers/r-bcbiobase/0.9.0--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bcbiobase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiobase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bcbiobase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bcbiobase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bcbiobase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bcbiobase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-bcbiobase

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