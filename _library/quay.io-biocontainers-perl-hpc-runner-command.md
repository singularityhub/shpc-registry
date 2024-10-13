---
layout: container
name:  "quay.io/biocontainers/perl-hpc-runner-command"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-hpc-runner-command/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-hpc-runner-command/container.yaml"
updated_at: "2024-10-13 11:11:53.310755"
latest: "3.2.13--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-hpc-runner-command"

versions:
 - "3.2.9--pl5.22.0_0"
 - "3.2.13--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-hpc-runner-command"
config: {"url": "https://biocontainers.pro/tools/perl-hpc-runner-command", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-hpc-runner-command", "latest": {"3.2.13--pl5321hdfd78af_2": "sha256:af94f69ace6ffc0d4a649a88ec276a4daf990e2153fad5dc638936573b5b6d33"}, "tags": {"3.2.9--pl5.22.0_0": "sha256:a28f812ca606dad70fc73491714f6661457f2c50d40ba9b926bae35aae4d8bce", "3.2.13--pl5321hdfd78af_2": "sha256:af94f69ace6ffc0d4a649a88ec276a4daf990e2153fad5dc638936573b5b6d33"}, "docker": "quay.io/biocontainers/perl-hpc-runner-command"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-hpc-runner-command.
shpc-registry automated BioContainers addition for perl-hpc-runner-command
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-command
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-command:3.2.13--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-hpc-runner-command/3.2.13--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-hpc-runner-command/3.2.13--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-hpc-runner-command-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-command-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-command-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-hpc-runner-command-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-hpc-runner-command-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-hpc-runner-command-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-hpc-runner-command

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