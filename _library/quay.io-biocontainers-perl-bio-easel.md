---
layout: container
name:  "quay.io/biocontainers/perl-bio-easel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-easel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-easel/container.yaml"
updated_at: "2024-08-28 03:26:16.151012"
latest: "0.16--pl5321h031d066_1"
container_url: "https://biocontainers.pro/tools/perl-bio-easel"
aliases:
 - "esl-alidepair.pl"
 - "esl-ssplit.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.15--pl5321hec16e2b_2"
 - "0.16--pl5321hec16e2b_0"
 - "0.16--pl5321h031d066_1"
description: "shpc-registry automated BioContainers addition for perl-bio-easel"
config: {"url": "https://biocontainers.pro/tools/perl-bio-easel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-easel", "latest": {"0.16--pl5321h031d066_1": "sha256:99249963c1cedee43ca488d8864cebe07d1944ed1a3710007429d205e4d1dd98"}, "tags": {"0.15--pl5321hec16e2b_2": "sha256:5b6155d97943e7c22e78385f4cd47b09428fc2de08c6935bf614e44f990c2ed8", "0.16--pl5321hec16e2b_0": "sha256:f7ac86b99426c504276c600816cfdc8ada257e14607ddb5101af0e90a3241973", "0.16--pl5321h031d066_1": "sha256:99249963c1cedee43ca488d8864cebe07d1944ed1a3710007429d205e4d1dd98"}, "docker": "quay.io/biocontainers/perl-bio-easel", "aliases": {"esl-alidepair.pl": "/usr/local/bin/esl-alidepair.pl", "esl-ssplit.pl": "/usr/local/bin/esl-ssplit.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-easel.
shpc-registry automated BioContainers addition for perl-bio-easel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-easel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-easel:0.16--pl5321h031d066_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-easel/0.16--pl5321h031d066_1
$ module help quay.io/biocontainers/perl-bio-easel/0.16--pl5321h031d066_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-easel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-easel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-easel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-easel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-easel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-easel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### esl-alidepair.pl

```bash
$ singularity exec <container> /usr/local/bin/esl-alidepair.pl
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alidepair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alidepair.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-ssplit.pl

```bash
$ singularity exec <container> /usr/local/bin/esl-ssplit.pl
$ podman run --it --rm --entrypoint /usr/local/bin/esl-ssplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-ssplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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