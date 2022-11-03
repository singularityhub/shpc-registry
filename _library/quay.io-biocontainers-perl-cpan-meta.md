---
layout: container
name:  "quay.io/biocontainers/perl-cpan-meta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-cpan-meta/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-cpan-meta/container.yaml"
updated_at: "2022-11-03 01:31:45.519873"
latest: "2.150010--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-cpan-meta"

versions:
 - "2.150010--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-cpan-meta"
config: {"url": "https://biocontainers.pro/tools/perl-cpan-meta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-cpan-meta", "latest": {"2.150010--pl5321hdfd78af_1": "sha256:a8e19fb2227fd3b60c88096b91224b28112e39aa9a8158d7818d0ef86e0b101c"}, "tags": {"2.150010--pl5321hdfd78af_1": "sha256:a8e19fb2227fd3b60c88096b91224b28112e39aa9a8158d7818d0ef86e0b101c"}, "docker": "quay.io/biocontainers/perl-cpan-meta"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-cpan-meta.
shpc-registry automated BioContainers addition for perl-cpan-meta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-cpan-meta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-cpan-meta:2.150010--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-cpan-meta/2.150010--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-cpan-meta/2.150010--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-cpan-meta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-cpan-meta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-cpan-meta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-cpan-meta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-cpan-meta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-cpan-meta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-cpan-meta

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