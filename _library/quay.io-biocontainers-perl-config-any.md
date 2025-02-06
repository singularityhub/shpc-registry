---
layout: container
name:  "quay.io/biocontainers/perl-config-any"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-config-any/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-config-any/container.yaml"
updated_at: "2025-02-06 03:32:11.802207"
latest: "0.33--pl5321h7b50bb2_4"
container_url: "https://biocontainers.pro/tools/perl-config-any"
aliases:
 - "cpanm"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.32--pl5321hec16e2b_3"
 - "0.33--pl5321h031d066_2"
 - "0.33--pl5321h031d066_3"
 - "0.33--pl5321h7b50bb2_4"
description: "shpc-registry automated BioContainers addition for perl-config-any"
config: {"url": "https://biocontainers.pro/tools/perl-config-any", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-config-any", "latest": {"0.33--pl5321h7b50bb2_4": "sha256:2e724ecd20682639c128758e7ba9f67612ac21e17e18e46f58ed1bc54107c38b"}, "tags": {"0.32--pl5321hec16e2b_3": "sha256:ea712f84b35ffd0c4ca46f54492251cbb43460f560a5eea35b7e265a8e779e52", "0.33--pl5321h031d066_2": "sha256:52df7f09c989dea5067bdb053b3aba4059a545c8a8c84317f026bea9a9326c9e", "0.33--pl5321h031d066_3": "sha256:773a6b5ceb3df92e7fd31789581eb63c0989a0aae87a3d1cc57c89580a7966c5", "0.33--pl5321h7b50bb2_4": "sha256:2e724ecd20682639c128758e7ba9f67612ac21e17e18e46f58ed1bc54107c38b"}, "docker": "quay.io/biocontainers/perl-config-any", "aliases": {"cpanm": "/usr/local/bin/cpanm", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-config-any.
shpc-registry automated BioContainers addition for perl-config-any
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-config-any
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-config-any:0.33--pl5321h7b50bb2_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-config-any/0.33--pl5321h7b50bb2_4
$ module help quay.io/biocontainers/perl-config-any/0.33--pl5321h7b50bb2_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-config-any-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-config-any-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-config-any-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-config-any-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-config-any-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-config-any-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cpanm

```bash
$ singularity exec <container> /usr/local/bin/cpanm
$ podman run --it --rm --entrypoint /usr/local/bin/cpanm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpanm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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