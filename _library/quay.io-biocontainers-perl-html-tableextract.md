---
layout: container
name:  "quay.io/biocontainers/perl-html-tableextract"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-html-tableextract/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-html-tableextract/container.yaml"
updated_at: "2024-08-16 03:19:50.843769"
latest: "2.13--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/perl-html-tableextract"
aliases:
 - "htmltree"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.13--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for perl-html-tableextract"
config: {"url": "https://biocontainers.pro/tools/perl-html-tableextract", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-html-tableextract", "latest": {"2.13--pl5321hdfd78af_3": "sha256:3b6c18d87adf444572afd8c10cc10330a96b1f7c9bd3bfb8cf32f4e32ceed500"}, "tags": {"2.13--pl5321hdfd78af_3": "sha256:3b6c18d87adf444572afd8c10cc10330a96b1f7c9bd3bfb8cf32f4e32ceed500"}, "docker": "quay.io/biocontainers/perl-html-tableextract", "aliases": {"htmltree": "/usr/local/bin/htmltree", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-html-tableextract.
shpc-registry automated BioContainers addition for perl-html-tableextract
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-html-tableextract
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-html-tableextract:2.13--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-html-tableextract/2.13--pl5321hdfd78af_3
$ module help quay.io/biocontainers/perl-html-tableextract/2.13--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-html-tableextract-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-tableextract-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-tableextract-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-html-tableextract-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-html-tableextract-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-html-tableextract-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### htmltree

```bash
$ singularity exec <container> /usr/local/bin/htmltree
$ podman run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
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