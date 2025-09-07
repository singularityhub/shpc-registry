---
layout: container
name:  "quay.io/biocontainers/perl-json"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-json/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-json/container.yaml"
updated_at: "2025-09-07 03:24:35.165879"
latest: "4.10--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-json"

versions:
 - "4.10--pl5321hdfd78af_0"
 - "4.10--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-json"
config: {"url": "https://biocontainers.pro/tools/perl-json", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-json", "latest": {"4.10--pl5321hdfd78af_1": "sha256:86ed7274fb215be49b1f79a41bc9bc523e520b20b5dc6ef65efde91b20a4b6d5"}, "tags": {"4.10--pl5321hdfd78af_0": "sha256:51e2fe2e640859a2dd73ecdac638687927e5afca83e92dc20162a44679d98e22", "4.10--pl5321hdfd78af_1": "sha256:86ed7274fb215be49b1f79a41bc9bc523e520b20b5dc6ef65efde91b20a4b6d5"}, "docker": "quay.io/biocontainers/perl-json"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-json.
shpc-registry automated BioContainers addition for perl-json
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-json
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-json:4.10--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-json/4.10--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-json/4.10--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-json-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-json-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-json-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-json-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-json

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