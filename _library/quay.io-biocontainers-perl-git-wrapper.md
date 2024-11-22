---
layout: container
name:  "quay.io/biocontainers/perl-git-wrapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-git-wrapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-git-wrapper/container.yaml"
updated_at: "2024-11-22 03:01:55.175286"
latest: "0.048--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-git-wrapper"

versions:
 - "0.048--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-git-wrapper"
config: {"url": "https://biocontainers.pro/tools/perl-git-wrapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-git-wrapper", "latest": {"0.048--pl5321hdfd78af_1": "sha256:a2fbfb6a92a4681f7f996b59476f80a9c40664abd1609cec812195cfabd8990b"}, "tags": {"0.048--pl5321hdfd78af_1": "sha256:a2fbfb6a92a4681f7f996b59476f80a9c40664abd1609cec812195cfabd8990b"}, "docker": "quay.io/biocontainers/perl-git-wrapper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-git-wrapper.
shpc-registry automated BioContainers addition for perl-git-wrapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-git-wrapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-git-wrapper:0.048--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-git-wrapper/0.048--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-git-wrapper/0.048--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-git-wrapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-git-wrapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-git-wrapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-git-wrapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-git-wrapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-git-wrapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-git-wrapper

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