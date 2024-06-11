---
layout: container
name:  "quay.io/biocontainers/vcfsamplecompare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcfsamplecompare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcfsamplecompare/container.yaml"
updated_at: "2024-06-11 05:25:27.744120"
latest: "2.013--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/vcfsamplecompare"
aliases:
 - "vcfSampleCompare.pl"
 - "perl5.26.2"
 - "podselect"
versions:
 - "v2.008--pl526_1"
 - "2.013--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for vcfsamplecompare"
config: {"url": "https://biocontainers.pro/tools/vcfsamplecompare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcfsamplecompare", "latest": {"2.013--pl5321hdfd78af_2": "sha256:c754c694c91834e4970c106e93f3b8e5d422dd08ca2be615a785aeff903b86f7"}, "tags": {"v2.008--pl526_1": "sha256:5118fbf7ed291e9b58be33f7cc2f023348ffc2607d63b1107060e56369fcc547", "2.013--pl5321hdfd78af_2": "sha256:c754c694c91834e4970c106e93f3b8e5d422dd08ca2be615a785aeff903b86f7"}, "docker": "quay.io/biocontainers/vcfsamplecompare", "aliases": {"vcfSampleCompare.pl": "/usr/local/bin/vcfSampleCompare.pl", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcfsamplecompare.
shpc-registry automated BioContainers addition for vcfsamplecompare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcfsamplecompare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcfsamplecompare:2.013--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcfsamplecompare/2.013--pl5321hdfd78af_2
$ module help quay.io/biocontainers/vcfsamplecompare/2.013--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcfsamplecompare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcfsamplecompare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcfsamplecompare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcfsamplecompare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcfsamplecompare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcfsamplecompare-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcfSampleCompare.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfSampleCompare.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfSampleCompare.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfSampleCompare.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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