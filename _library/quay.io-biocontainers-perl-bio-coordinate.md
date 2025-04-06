---
layout: container
name:  "quay.io/biocontainers/perl-bio-coordinate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-coordinate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-coordinate/container.yaml"
updated_at: "2025-04-06 03:24:12.592670"
latest: "1.007001--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/perl-bio-coordinate"
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
 - "1.007001--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for perl-bio-coordinate"
config: {"url": "https://biocontainers.pro/tools/perl-bio-coordinate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-coordinate", "latest": {"1.007001--pl5321hdfd78af_3": "sha256:073dc36ed204698c3c57fa74479b443cfe7226c697e2eea27bf3e8811016e7ae"}, "tags": {"1.007001--pl5321hdfd78af_3": "sha256:073dc36ed204698c3c57fa74479b443cfe7226c697e2eea27bf3e8811016e7ae"}, "docker": "quay.io/biocontainers/perl-bio-coordinate", "aliases": {"bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "ace.pl": "/usr/local/bin/ace.pl", "ccconfig": "/usr/local/bin/ccconfig", "SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "map": "/usr/local/bin/map", "mirrorMappings": "/usr/local/bin/mirrorMappings", "mkCSGB2312": "/usr/local/bin/mkCSGB2312", "mkmapfile": "/usr/local/bin/mkmapfile", "stubmaker.pl": "/usr/local/bin/stubmaker.pl", "chartex": "/usr/local/bin/chartex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-coordinate.
shpc-registry automated BioContainers addition for perl-bio-coordinate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-coordinate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-coordinate:1.007001--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-coordinate/1.007001--pl5321hdfd78af_3
$ module help quay.io/biocontainers/perl-bio-coordinate/1.007001--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-coordinate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-coordinate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-coordinate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-coordinate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-coordinate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-coordinate-inspect-deffile:

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