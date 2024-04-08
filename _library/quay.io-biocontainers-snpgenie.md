---
layout: container
name:  "quay.io/biocontainers/snpgenie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snpgenie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snpgenie/container.yaml"
updated_at: "2024-04-08 03:04:26.063407"
latest: "1.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/snpgenie"
aliases:
 - "fasta2revcom.pl"
 - "gtf2revcom.pl"
 - "snpgenie.pl"
 - "snpgenie_between_group.pl"
 - "snpgenie_between_group_processor.pl"
 - "snpgenie_within_group.pl"
 - "snpgenie_within_group_processor.pl"
 - "vcf2revcom.pl"
 - "moose-outdated"
 - "package-stash-conflicts"
 - "cpanm"
 - "perl5.26.2"
 - "podselect"
versions:
 - "1.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for snpgenie"
config: {"url": "https://biocontainers.pro/tools/snpgenie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snpgenie", "latest": {"1.0--hdfd78af_1": "sha256:bacfcf5093982fab1078b1b326b3ae2c16aca8874cab1afe9a4facac953310bc"}, "tags": {"1.0--hdfd78af_1": "sha256:bacfcf5093982fab1078b1b326b3ae2c16aca8874cab1afe9a4facac953310bc"}, "docker": "quay.io/biocontainers/snpgenie", "aliases": {"fasta2revcom.pl": "/usr/local/bin/fasta2revcom.pl", "gtf2revcom.pl": "/usr/local/bin/gtf2revcom.pl", "snpgenie.pl": "/usr/local/bin/snpgenie.pl", "snpgenie_between_group.pl": "/usr/local/bin/snpgenie_between_group.pl", "snpgenie_between_group_processor.pl": "/usr/local/bin/snpgenie_between_group_processor.pl", "snpgenie_within_group.pl": "/usr/local/bin/snpgenie_within_group.pl", "snpgenie_within_group_processor.pl": "/usr/local/bin/snpgenie_within_group_processor.pl", "vcf2revcom.pl": "/usr/local/bin/vcf2revcom.pl", "moose-outdated": "/usr/local/bin/moose-outdated", "package-stash-conflicts": "/usr/local/bin/package-stash-conflicts", "cpanm": "/usr/local/bin/cpanm", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snpgenie.
shpc-registry automated BioContainers addition for snpgenie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snpgenie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snpgenie:1.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snpgenie/1.0--hdfd78af_1
$ module help quay.io/biocontainers/snpgenie/1.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snpgenie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snpgenie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snpgenie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snpgenie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snpgenie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snpgenie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasta2revcom.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta2revcom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2revcom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2revcom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2revcom.pl

```bash
$ singularity exec <container> /usr/local/bin/gtf2revcom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gtf2revcom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtf2revcom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpgenie.pl

```bash
$ singularity exec <container> /usr/local/bin/snpgenie.pl
$ podman run --it --rm --entrypoint /usr/local/bin/snpgenie.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpgenie.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpgenie_between_group.pl

```bash
$ singularity exec <container> /usr/local/bin/snpgenie_between_group.pl
$ podman run --it --rm --entrypoint /usr/local/bin/snpgenie_between_group.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpgenie_between_group.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpgenie_between_group_processor.pl

```bash
$ singularity exec <container> /usr/local/bin/snpgenie_between_group_processor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/snpgenie_between_group_processor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpgenie_between_group_processor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpgenie_within_group.pl

```bash
$ singularity exec <container> /usr/local/bin/snpgenie_within_group.pl
$ podman run --it --rm --entrypoint /usr/local/bin/snpgenie_within_group.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpgenie_within_group.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpgenie_within_group_processor.pl

```bash
$ singularity exec <container> /usr/local/bin/snpgenie_within_group_processor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/snpgenie_within_group_processor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpgenie_within_group_processor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2revcom.pl

```bash
$ singularity exec <container> /usr/local/bin/vcf2revcom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2revcom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2revcom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moose-outdated

```bash
$ singularity exec <container> /usr/local/bin/moose-outdated
$ podman run --it --rm --entrypoint /usr/local/bin/moose-outdated   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moose-outdated   -v ${PWD} -w ${PWD} <container> -c " $@"
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