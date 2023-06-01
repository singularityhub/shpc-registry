---
layout: container
name:  "quay.io/biocontainers/perl-xml-sax-writer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-xml-sax-writer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-xml-sax-writer/container.yaml"
updated_at: "2023-06-01 03:59:16.152934"
latest: "0.57--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-xml-sax-writer"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.57--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-xml-sax-writer"
config: {"url": "https://biocontainers.pro/tools/perl-xml-sax-writer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-xml-sax-writer", "latest": {"0.57--pl5321hdfd78af_1": "sha256:9cfac1f93d6edf1456f6924ca51bfd1cbfa2aae087b4c84f6ffea7645eb7c2cc"}, "tags": {"0.57--pl5321hdfd78af_1": "sha256:9cfac1f93d6edf1456f6924ca51bfd1cbfa2aae087b4c84f6ffea7645eb7c2cc"}, "docker": "quay.io/biocontainers/perl-xml-sax-writer", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-xml-sax-writer.
shpc-registry automated BioContainers addition for perl-xml-sax-writer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-xml-sax-writer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-xml-sax-writer:0.57--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-xml-sax-writer/0.57--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-xml-sax-writer/0.57--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-xml-sax-writer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-xml-sax-writer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-xml-sax-writer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-xml-sax-writer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-xml-sax-writer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-xml-sax-writer-inspect-deffile:

```bash
$ singularity inspect -d <container>
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