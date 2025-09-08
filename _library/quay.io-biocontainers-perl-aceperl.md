---
layout: container
name:  "quay.io/biocontainers/perl-aceperl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-aceperl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-aceperl/container.yaml"
updated_at: "2025-09-08 04:51:04.736647"
latest: "1.92--pl5321h7b50bb2_8"
container_url: "https://biocontainers.pro/tools/perl-aceperl"
aliases:
 - "ace.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.92--pl5321hec16e2b_4"
 - "1.92--pl5321h031d066_5"
 - "1.92--pl5321h7b50bb2_6"
 - "1.92--pl5321h7b50bb2_7"
 - "1.92--pl5321h7b50bb2_8"
description: "shpc-registry automated BioContainers addition for perl-aceperl"
config: {"url": "https://biocontainers.pro/tools/perl-aceperl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-aceperl", "latest": {"1.92--pl5321h7b50bb2_8": "sha256:8f174b4ee265ed005bfcb9e6c1b1e1b1bcd79d56ed2e0994025ad1a7192160ce"}, "tags": {"1.92--pl5321hec16e2b_4": "sha256:51c3a40bbb22072b38deeabc7a16471a8cd400e8de94069934adb1c27bd04e25", "1.92--pl5321h031d066_5": "sha256:d5b9e103f8c8a279c98497c5960d5dde999e3410ce7b0d2998321c7de265dcac", "1.92--pl5321h7b50bb2_6": "sha256:99c18e5e119fb6ef695e5a19ba44b1014b4a70cfd4afae28ff3bccadb8b360e8", "1.92--pl5321h7b50bb2_7": "sha256:953c6177010f5c021d4675031b607db2418a8c00e0d86412d745b733e58a6e17", "1.92--pl5321h7b50bb2_8": "sha256:8f174b4ee265ed005bfcb9e6c1b1e1b1bcd79d56ed2e0994025ad1a7192160ce"}, "docker": "quay.io/biocontainers/perl-aceperl", "aliases": {"ace.pl": "/usr/local/bin/ace.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-aceperl.
shpc-registry automated BioContainers addition for perl-aceperl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-aceperl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-aceperl:1.92--pl5321h7b50bb2_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-aceperl/1.92--pl5321h7b50bb2_8
$ module help quay.io/biocontainers/perl-aceperl/1.92--pl5321h7b50bb2_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-aceperl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-aceperl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-aceperl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-aceperl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-aceperl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-aceperl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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