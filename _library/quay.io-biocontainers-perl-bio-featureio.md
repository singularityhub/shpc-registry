---
layout: container
name:  "quay.io/biocontainers/perl-bio-featureio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-featureio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-featureio/container.yaml"
updated_at: "2024-11-26 03:37:39.335509"
latest: "1.6.905--pl5321hdfd78af_4"
container_url: "https://biocontainers.pro/tools/perl-bio-featureio"
aliases:
 - "bp_find-blast-matches.pl"
 - "ace.pl"
 - "ccconfig"
 - "SOAPsh.pl"
 - "map"
 - "mirrorMappings"
 - "mkCSGB2312"
 - "mkmapfile"
 - "stubmaker.pl"
 - "chartex"
versions:
 - "1.6.905--pl5321hdfd78af_4"
description: "shpc-registry automated BioContainers addition for perl-bio-featureio"
config: {"url": "https://biocontainers.pro/tools/perl-bio-featureio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-featureio", "latest": {"1.6.905--pl5321hdfd78af_4": "sha256:5dc777d265a7cdd276fa75b484bc1a5f27ab3731a7ea698fbb59262c5ba0b2de"}, "tags": {"1.6.905--pl5321hdfd78af_4": "sha256:5dc777d265a7cdd276fa75b484bc1a5f27ab3731a7ea698fbb59262c5ba0b2de"}, "docker": "quay.io/biocontainers/perl-bio-featureio", "aliases": {"bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "ace.pl": "/usr/local/bin/ace.pl", "ccconfig": "/usr/local/bin/ccconfig", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "map": "/usr/local/bin/map", "mirrorMappings": "/usr/local/bin/mirrorMappings", "mkCSGB2312": "/usr/local/bin/mkCSGB2312", "mkmapfile": "/usr/local/bin/mkmapfile", "stubmaker.pl": "/usr/local/bin/stubmaker.pl", "chartex": "/usr/local/bin/chartex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-featureio.
shpc-registry automated BioContainers addition for perl-bio-featureio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-featureio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-featureio:1.6.905--pl5321hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-featureio/1.6.905--pl5321hdfd78af_4
$ module help quay.io/biocontainers/perl-bio-featureio/1.6.905--pl5321hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-featureio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-featureio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-featureio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-featureio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-featureio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-featureio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccconfig

```bash
$ singularity exec <container> /usr/local/bin/ccconfig
$ podman run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map

```bash
$ singularity exec <container> /usr/local/bin/map
$ podman run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirrorMappings

```bash
$ singularity exec <container> /usr/local/bin/mirrorMappings
$ podman run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirrorMappings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkCSGB2312

```bash
$ singularity exec <container> /usr/local/bin/mkCSGB2312
$ podman run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkCSGB2312   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkmapfile

```bash
$ singularity exec <container> /usr/local/bin/mkmapfile
$ podman run --it --rm --entrypoint /usr/local/bin/mkmapfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkmapfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stubmaker.pl

```bash
$ singularity exec <container> /usr/local/bin/stubmaker.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stubmaker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stubmaker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chartex

```bash
$ singularity exec <container> /usr/local/bin/chartex
$ podman run --it --rm --entrypoint /usr/local/bin/chartex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chartex   -v ${PWD} -w ${PWD} <container> -c " $@"
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