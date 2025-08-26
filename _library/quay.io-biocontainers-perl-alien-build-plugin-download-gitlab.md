---
layout: container
name:  "quay.io/biocontainers/perl-alien-build-plugin-download-gitlab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-alien-build-plugin-download-gitlab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-alien-build-plugin-download-gitlab/container.yaml"
updated_at: "2025-08-26 03:30:02.933714"
latest: "0.01--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-alien-build-plugin-download-gitlab"

versions:
 - "0.01--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for perl-alien-build-plugin-download-gitlab"
config: {"url": "https://biocontainers.pro/tools/perl-alien-build-plugin-download-gitlab", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-alien-build-plugin-download-gitlab", "latest": {"0.01--pl5321hdfd78af_0": "sha256:dd32e869f0fe81868836826918ac17c4de81714798e83718e2781da8fd99a013"}, "tags": {"0.01--pl5321hdfd78af_0": "sha256:dd32e869f0fe81868836826918ac17c4de81714798e83718e2781da8fd99a013"}, "docker": "quay.io/biocontainers/perl-alien-build-plugin-download-gitlab"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-alien-build-plugin-download-gitlab.
singularity registry hpc automated addition for perl-alien-build-plugin-download-gitlab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-alien-build-plugin-download-gitlab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-alien-build-plugin-download-gitlab:0.01--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-alien-build-plugin-download-gitlab/0.01--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-alien-build-plugin-download-gitlab/0.01--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-alien-build-plugin-download-gitlab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-alien-build-plugin-download-gitlab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-alien-build-plugin-download-gitlab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-alien-build-plugin-download-gitlab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-alien-build-plugin-download-gitlab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-alien-build-plugin-download-gitlab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-alien-build-plugin-download-gitlab

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