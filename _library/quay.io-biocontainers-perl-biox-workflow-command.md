---
layout: container
name:  "quay.io/biocontainers/perl-biox-workflow-command"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-biox-workflow-command/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-biox-workflow-command/container.yaml"
updated_at: "2023-06-22 02:49:07.493037"
latest: "2.4.1--pl526_1"
container_url: "https://biocontainers.pro/tools/perl-biox-workflow-command"
aliases:
 - "biosails-biox-render.py"
 - "biox"
 - "biox-workflow.pl"
 - "mustache.pl"
 - "perl-reversion"
 - "findrule"
 - "l4p-tmpl"
 - "config_data"
 - "dbilogstrip"
 - "dbiprof"
 - "dbiproxy"
 - "moose-outdated"
 - "package-stash-conflicts"
 - "cpanm"
 - "json_xs"
versions:
 - "2.4.1--pl526_1"
description: "shpc-registry automated BioContainers addition for perl-biox-workflow-command"
config: {"url": "https://biocontainers.pro/tools/perl-biox-workflow-command", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-biox-workflow-command", "latest": {"2.4.1--pl526_1": "sha256:63a0b470270b26a3cf34ebe381d861c37b6eddb025a1f3812fb673f5ed86b14c"}, "tags": {"2.4.1--pl526_1": "sha256:63a0b470270b26a3cf34ebe381d861c37b6eddb025a1f3812fb673f5ed86b14c"}, "docker": "quay.io/biocontainers/perl-biox-workflow-command", "aliases": {"biosails-biox-render.py": "/usr/local/bin/biosails-biox-render.py", "biox": "/usr/local/bin/biox", "biox-workflow.pl": "/usr/local/bin/biox-workflow.pl", "mustache.pl": "/usr/local/bin/mustache.pl", "perl-reversion": "/usr/local/bin/perl-reversion", "findrule": "/usr/local/bin/findrule", "l4p-tmpl": "/usr/local/bin/l4p-tmpl", "config_data": "/usr/local/bin/config_data", "dbilogstrip": "/usr/local/bin/dbilogstrip", "dbiprof": "/usr/local/bin/dbiprof", "dbiproxy": "/usr/local/bin/dbiproxy", "moose-outdated": "/usr/local/bin/moose-outdated", "package-stash-conflicts": "/usr/local/bin/package-stash-conflicts", "cpanm": "/usr/local/bin/cpanm", "json_xs": "/usr/local/bin/json_xs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-biox-workflow-command.
shpc-registry automated BioContainers addition for perl-biox-workflow-command
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-biox-workflow-command
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-biox-workflow-command:2.4.1--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-biox-workflow-command/2.4.1--pl526_1
$ module help quay.io/biocontainers/perl-biox-workflow-command/2.4.1--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-biox-workflow-command-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-biox-workflow-command-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-biox-workflow-command-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-biox-workflow-command-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-biox-workflow-command-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-biox-workflow-command-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biosails-biox-render.py

```bash
$ singularity exec <container> /usr/local/bin/biosails-biox-render.py
$ podman run --it --rm --entrypoint /usr/local/bin/biosails-biox-render.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biosails-biox-render.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biox

```bash
$ singularity exec <container> /usr/local/bin/biox
$ podman run --it --rm --entrypoint /usr/local/bin/biox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biox-workflow.pl

```bash
$ singularity exec <container> /usr/local/bin/biox-workflow.pl
$ podman run --it --rm --entrypoint /usr/local/bin/biox-workflow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biox-workflow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mustache.pl

```bash
$ singularity exec <container> /usr/local/bin/mustache.pl
$ podman run --it --rm --entrypoint /usr/local/bin/mustache.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mustache.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl-reversion

```bash
$ singularity exec <container> /usr/local/bin/perl-reversion
$ podman run --it --rm --entrypoint /usr/local/bin/perl-reversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl-reversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### l4p-tmpl

```bash
$ singularity exec <container> /usr/local/bin/l4p-tmpl
$ podman run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbilogstrip

```bash
$ singularity exec <container> /usr/local/bin/dbilogstrip
$ podman run --it --rm --entrypoint /usr/local/bin/dbilogstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbilogstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbiprof

```bash
$ singularity exec <container> /usr/local/bin/dbiprof
$ podman run --it --rm --entrypoint /usr/local/bin/dbiprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbiprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbiproxy

```bash
$ singularity exec <container> /usr/local/bin/dbiproxy
$ podman run --it --rm --entrypoint /usr/local/bin/dbiproxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbiproxy   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### json_xs

```bash
$ singularity exec <container> /usr/local/bin/json_xs
$ podman run --it --rm --entrypoint /usr/local/bin/json_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
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