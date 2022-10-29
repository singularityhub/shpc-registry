---
layout: container
name:  "quay.io/biocontainers/perl-email-date-format"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-email-date-format/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-email-date-format/container.yaml"
updated_at: "2022-10-29 05:41:42.707392"
latest: "1.005--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/perl-email-date-format"
aliases:
 - "corelist"
 - "cpan"
 - "enc2xs"
 - "encguess"
 - "h2ph"
 - "h2xs"
 - "instmodsh"
 - "json_pp"
 - "libnetcfg"
 - "perl"
versions:
 - "1.005--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for perl-email-date-format"
config: {"url": "https://biocontainers.pro/tools/perl-email-date-format", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-email-date-format", "latest": {"1.005--pl5321hdfd78af_3": "sha256:5d50d9690afeb25c5948555868498ee258f84b62c2fae8dd195d139b3b71eb3c"}, "tags": {"1.005--pl5321hdfd78af_3": "sha256:5d50d9690afeb25c5948555868498ee258f84b62c2fae8dd195d139b3b71eb3c"}, "docker": "quay.io/biocontainers/perl-email-date-format", "aliases": {"corelist": "/usr/local/bin/corelist", "cpan": "/usr/local/bin/cpan", "enc2xs": "/usr/local/bin/enc2xs", "encguess": "/usr/local/bin/encguess", "h2ph": "/usr/local/bin/h2ph", "h2xs": "/usr/local/bin/h2xs", "instmodsh": "/usr/local/bin/instmodsh", "json_pp": "/usr/local/bin/json_pp", "libnetcfg": "/usr/local/bin/libnetcfg", "perl": "/usr/local/bin/perl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-email-date-format.
shpc-registry automated BioContainers addition for perl-email-date-format
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-email-date-format
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-email-date-format:1.005--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-email-date-format/1.005--pl5321hdfd78af_3
$ module help quay.io/biocontainers/perl-email-date-format/1.005--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-email-date-format-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-email-date-format-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-email-date-format-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-email-date-format-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-email-date-format-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-email-date-format-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### corelist

```bash
$ singularity exec <container> /usr/local/bin/corelist
$ podman run --it --rm --entrypoint /usr/local/bin/corelist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corelist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpan

```bash
$ singularity exec <container> /usr/local/bin/cpan
$ podman run --it --rm --entrypoint /usr/local/bin/cpan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enc2xs

```bash
$ singularity exec <container> /usr/local/bin/enc2xs
$ podman run --it --rm --entrypoint /usr/local/bin/enc2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enc2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### encguess

```bash
$ singularity exec <container> /usr/local/bin/encguess
$ podman run --it --rm --entrypoint /usr/local/bin/encguess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/encguess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2ph

```bash
$ singularity exec <container> /usr/local/bin/h2ph
$ podman run --it --rm --entrypoint /usr/local/bin/h2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2xs

```bash
$ singularity exec <container> /usr/local/bin/h2xs
$ podman run --it --rm --entrypoint /usr/local/bin/h2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2xs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### instmodsh

```bash
$ singularity exec <container> /usr/local/bin/instmodsh
$ podman run --it --rm --entrypoint /usr/local/bin/instmodsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/instmodsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### json_pp

```bash
$ singularity exec <container> /usr/local/bin/json_pp
$ podman run --it --rm --entrypoint /usr/local/bin/json_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libnetcfg

```bash
$ singularity exec <container> /usr/local/bin/libnetcfg
$ podman run --it --rm --entrypoint /usr/local/bin/libnetcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libnetcfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl

```bash
$ singularity exec <container> /usr/local/bin/perl
$ podman run --it --rm --entrypoint /usr/local/bin/perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl   -v ${PWD} -w ${PWD} <container> -c " $@"
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