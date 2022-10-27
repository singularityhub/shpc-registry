---
layout: container
name:  "quay.io/biocontainers/staphopia-sccmec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staphopia-sccmec/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/staphopia-sccmec/container.yaml"
updated_at: "2022-10-27 00:24:58.113171"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/staphopia-sccmec"
aliases:
 - "executor"
 - "staphopia-sccmec"
versions:
 - "1.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for staphopia-sccmec"
config: {"url": "https://biocontainers.pro/tools/staphopia-sccmec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for staphopia-sccmec", "latest": {"1.0.0--hdfd78af_0": "sha256:f006276565254f788bee4adc73d146959ade537ecd7b14501a725401fd1dea87"}, "tags": {"1.0.0--hdfd78af_0": "sha256:f006276565254f788bee4adc73d146959ade537ecd7b14501a725401fd1dea87"}, "docker": "quay.io/biocontainers/staphopia-sccmec", "aliases": {"executor": "/usr/local/bin/executor", "staphopia-sccmec": "/usr/local/bin/staphopia-sccmec"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/staphopia-sccmec.
shpc-registry automated BioContainers addition for staphopia-sccmec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staphopia-sccmec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staphopia-sccmec:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staphopia-sccmec/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/staphopia-sccmec/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staphopia-sccmec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staphopia-sccmec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staphopia-sccmec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staphopia-sccmec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staphopia-sccmec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staphopia-sccmec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### executor

```bash
$ singularity exec <container> /usr/local/bin/executor
$ podman run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### staphopia-sccmec

```bash
$ singularity exec <container> /usr/local/bin/staphopia-sccmec
$ podman run --it --rm --entrypoint /usr/local/bin/staphopia-sccmec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/staphopia-sccmec   -v ${PWD} -w ${PWD} <container> -c " $@"
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