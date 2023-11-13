---
layout: container
name:  "quay.io/biocontainers/perl-biox-workflow-plugin-filedetails"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-biox-workflow-plugin-filedetails/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-biox-workflow-plugin-filedetails/container.yaml"
updated_at: "2023-11-13 03:05:42.706722"
latest: "0.11--0"
container_url: "https://biocontainers.pro/tools/perl-biox-workflow-plugin-filedetails"
aliases:
 - "biox-workflow.pl"
 - "filedetails.pl"
 - "findrule"
 - "config_data"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "moose-outdated"
 - "package-stash-conflicts"
 - "cpanm"
 - "podselect"
versions:
 - "0.11--0"
description: "shpc-registry automated BioContainers addition for perl-biox-workflow-plugin-filedetails"
config: {"url": "https://biocontainers.pro/tools/perl-biox-workflow-plugin-filedetails", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-biox-workflow-plugin-filedetails", "latest": {"0.11--0": "sha256:d7210c1b7b046de3924d5c297765cd673fb156aafdf442d4a9b4c86b65cf3114"}, "tags": {"0.11--0": "sha256:d7210c1b7b046de3924d5c297765cd673fb156aafdf442d4a9b4c86b65cf3114"}, "docker": "quay.io/biocontainers/perl-biox-workflow-plugin-filedetails", "aliases": {"biox-workflow.pl": "/usr/local/bin/biox-workflow.pl", "filedetails.pl": "/usr/local/bin/filedetails.pl", "findrule": "/usr/local/bin/findrule", "config_data": "/usr/local/bin/config_data", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "moose-outdated": "/usr/local/bin/moose-outdated", "package-stash-conflicts": "/usr/local/bin/package-stash-conflicts", "cpanm": "/usr/local/bin/cpanm", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-biox-workflow-plugin-filedetails.
shpc-registry automated BioContainers addition for perl-biox-workflow-plugin-filedetails
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-biox-workflow-plugin-filedetails
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-biox-workflow-plugin-filedetails:0.11--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-biox-workflow-plugin-filedetails/0.11--0
$ module help quay.io/biocontainers/perl-biox-workflow-plugin-filedetails/0.11--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-biox-workflow-plugin-filedetails-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-biox-workflow-plugin-filedetails-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-biox-workflow-plugin-filedetails-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-biox-workflow-plugin-filedetails-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-biox-workflow-plugin-filedetails-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-biox-workflow-plugin-filedetails-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biox-workflow.pl

```bash
$ singularity exec <container> /usr/local/bin/biox-workflow.pl
$ podman run --it --rm --entrypoint /usr/local/bin/biox-workflow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biox-workflow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filedetails.pl

```bash
$ singularity exec <container> /usr/local/bin/filedetails.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filedetails.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filedetails.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
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