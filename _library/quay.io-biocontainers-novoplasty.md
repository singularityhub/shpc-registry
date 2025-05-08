---
layout: container
name:  "quay.io/biocontainers/novoplasty"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/novoplasty/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/novoplasty/container.yaml"
updated_at: "2025-05-08 03:25:31.299378"
latest: "4.3.5--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/novoplasty"
aliases:
 - "Circos.pl"
 - "NOVOPlasty.pl"
 - "NOVOPlasty4.3.1.pl"
 - "filter_reads.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "4.3.1--pl5321hdfd78af_1"
 - "4.3.3--pl5321hdfd78af_0"
 - "4.3.5--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for novoplasty"
config: {"url": "https://biocontainers.pro/tools/novoplasty", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for novoplasty", "latest": {"4.3.5--pl5321hdfd78af_0": "sha256:611cb5efdd1021f4113fedf603386bba091b3087bd80a0901f7918e975a89e6c"}, "tags": {"4.3.1--pl5321hdfd78af_1": "sha256:f5276f7eabaef7d3d660bdd2c8a2b7cecd93e9cdd677ec86233edb4aba35e39f", "4.3.3--pl5321hdfd78af_0": "sha256:c4f8f7e10ca9184dcda0456d75bf45a4e1bb5af03405c3d8e6cf414ec7c2402a", "4.3.5--pl5321hdfd78af_0": "sha256:611cb5efdd1021f4113fedf603386bba091b3087bd80a0901f7918e975a89e6c"}, "docker": "quay.io/biocontainers/novoplasty", "aliases": {"Circos.pl": "/usr/local/bin/Circos.pl", "NOVOPlasty.pl": "/usr/local/bin/NOVOPlasty.pl", "NOVOPlasty4.3.1.pl": "/usr/local/bin/NOVOPlasty4.3.1.pl", "filter_reads.pl": "/usr/local/bin/filter_reads.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/novoplasty.
shpc-registry automated BioContainers addition for novoplasty
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/novoplasty
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/novoplasty:4.3.5--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/novoplasty/4.3.5--pl5321hdfd78af_0
$ module help quay.io/biocontainers/novoplasty/4.3.5--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### novoplasty-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### novoplasty-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### novoplasty-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### novoplasty-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### novoplasty-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### novoplasty-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Circos.pl

```bash
$ singularity exec <container> /usr/local/bin/Circos.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Circos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Circos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NOVOPlasty.pl

```bash
$ singularity exec <container> /usr/local/bin/NOVOPlasty.pl
$ podman run --it --rm --entrypoint /usr/local/bin/NOVOPlasty.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NOVOPlasty.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NOVOPlasty4.3.1.pl

```bash
$ singularity exec <container> /usr/local/bin/NOVOPlasty4.3.1.pl
$ podman run --it --rm --entrypoint /usr/local/bin/NOVOPlasty4.3.1.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NOVOPlasty4.3.1.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_reads.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_reads.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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