---
layout: container
name:  "quay.io/biocontainers/perl-datetime-locale"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-datetime-locale/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-datetime-locale/container.yaml"
updated_at: "2024-08-07 03:27:19.305852"
latest: "1.39--pl5321h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/perl-datetime-locale"
aliases:
 - "package-stash-conflicts"
 - "cpanm"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.36--pl5321h9f5acd7_0"
 - "1.37--pl5321h9f5acd7_0"
 - "1.38--pl5321h9f5acd7_0"
 - "1.38--pl5321h4ac6f70_1"
 - "1.39--pl5321h4ac6f70_0"
description: "shpc-registry automated BioContainers addition for perl-datetime-locale"
config: {"url": "https://biocontainers.pro/tools/perl-datetime-locale", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-datetime-locale", "latest": {"1.39--pl5321h4ac6f70_0": "sha256:62de94776cdbb3a88c57f613676c2d9144ae533a4cf0b643f3e1d4fc0ddb9c1b"}, "tags": {"1.36--pl5321h9f5acd7_0": "sha256:5dee016a721c609a03bf2ee0e6d327048e4325fda77efc2c8ddef4a29e2edd32", "1.37--pl5321h9f5acd7_0": "sha256:2df055ab5cc2f3a54287e56f9b884f39107332cb15d60edaf7138fc04ebb3802", "1.38--pl5321h9f5acd7_0": "sha256:6797084c9cf7ad3778a1c84e4f855238397f216573378709591b93393d53fb77", "1.38--pl5321h4ac6f70_1": "sha256:5888f3b1777be561d04824f96979ca80bde3ca3ee86392d6d4e1a0af7686a45e", "1.39--pl5321h4ac6f70_0": "sha256:62de94776cdbb3a88c57f613676c2d9144ae533a4cf0b643f3e1d4fc0ddb9c1b"}, "docker": "quay.io/biocontainers/perl-datetime-locale", "aliases": {"package-stash-conflicts": "/usr/local/bin/package-stash-conflicts", "cpanm": "/usr/local/bin/cpanm", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-datetime-locale.
shpc-registry automated BioContainers addition for perl-datetime-locale
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-datetime-locale
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-datetime-locale:1.39--pl5321h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-datetime-locale/1.39--pl5321h4ac6f70_0
$ module help quay.io/biocontainers/perl-datetime-locale/1.39--pl5321h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-datetime-locale-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-datetime-locale-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-datetime-locale-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-datetime-locale-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-datetime-locale-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-datetime-locale-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### package-stash-conflicts

```bash
$ singularity exec <container> /usr/local/bin/package-stash-conflicts
$ podman run --it --rm --entrypoint /usr/local/bin/package-stash-conflicts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/package-stash-conflicts   -v ${PWD} -w ${PWD} <container> -c " $@"
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