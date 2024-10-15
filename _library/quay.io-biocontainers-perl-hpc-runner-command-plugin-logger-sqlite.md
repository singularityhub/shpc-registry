---
layout: container
name:  "quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite/container.yaml"
updated_at: "2024-10-15 03:22:56.034958"
latest: "0.0.3--pl5321hf0dce44_3"
container_url: "https://biocontainers.pro/tools/perl-hpc-runner-command-plugin-logger-sqlite"
aliases:
 - "ansitable-list-border-styles"
 - "ansitable-list-color-themes"
 - "ansitable-list-style-sets"
 - "dbicadmin"
 - "hpcrunner.pl"
 - "perl-reversion"
 - "findrule"
 - "l4p-tmpl"
 - "imgsize"
 - "tpage"
 - "ttree"
 - "dbilogstrip"
 - "dbiprof"
 - "dbiproxy"
 - "moose-outdated"
 - "package-stash-conflicts"
versions:
 - "0.0.3--pl5321hf0dce44_3"
description: "shpc-registry automated BioContainers addition for perl-hpc-runner-command-plugin-logger-sqlite"
config: {"url": "https://biocontainers.pro/tools/perl-hpc-runner-command-plugin-logger-sqlite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-hpc-runner-command-plugin-logger-sqlite", "latest": {"0.0.3--pl5321hf0dce44_3": "sha256:8ea8adbc4a156cb79fb81ff7fa86dbe5ee0323bfd7c9281faf85c4202cb1d4b6"}, "tags": {"0.0.3--pl5321hf0dce44_3": "sha256:8ea8adbc4a156cb79fb81ff7fa86dbe5ee0323bfd7c9281faf85c4202cb1d4b6"}, "docker": "quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite", "aliases": {"ansitable-list-border-styles": "/usr/local/bin/ansitable-list-border-styles", "ansitable-list-color-themes": "/usr/local/bin/ansitable-list-color-themes", "ansitable-list-style-sets": "/usr/local/bin/ansitable-list-style-sets", "dbicadmin": "/usr/local/bin/dbicadmin", "hpcrunner.pl": "/usr/local/bin/hpcrunner.pl", "perl-reversion": "/usr/local/bin/perl-reversion", "findrule": "/usr/local/bin/findrule", "l4p-tmpl": "/usr/local/bin/l4p-tmpl", "imgsize": "/usr/local/bin/imgsize", "tpage": "/usr/local/bin/tpage", "ttree": "/usr/local/bin/ttree", "dbilogstrip": "/usr/local/bin/dbilogstrip", "dbiprof": "/usr/local/bin/dbiprof", "dbiproxy": "/usr/local/bin/dbiproxy", "moose-outdated": "/usr/local/bin/moose-outdated", "package-stash-conflicts": "/usr/local/bin/package-stash-conflicts"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite.
shpc-registry automated BioContainers addition for perl-hpc-runner-command-plugin-logger-sqlite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite:0.0.3--pl5321hf0dce44_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite/0.0.3--pl5321hf0dce44_3
$ module help quay.io/biocontainers/perl-hpc-runner-command-plugin-logger-sqlite/0.0.3--pl5321hf0dce44_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-hpc-runner-command-plugin-logger-sqlite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-command-plugin-logger-sqlite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-hpc-runner-command-plugin-logger-sqlite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-hpc-runner-command-plugin-logger-sqlite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-hpc-runner-command-plugin-logger-sqlite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-hpc-runner-command-plugin-logger-sqlite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ansitable-list-border-styles

```bash
$ singularity exec <container> /usr/local/bin/ansitable-list-border-styles
$ podman run --it --rm --entrypoint /usr/local/bin/ansitable-list-border-styles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansitable-list-border-styles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansitable-list-color-themes

```bash
$ singularity exec <container> /usr/local/bin/ansitable-list-color-themes
$ podman run --it --rm --entrypoint /usr/local/bin/ansitable-list-color-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansitable-list-color-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ansitable-list-style-sets

```bash
$ singularity exec <container> /usr/local/bin/ansitable-list-style-sets
$ podman run --it --rm --entrypoint /usr/local/bin/ansitable-list-style-sets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ansitable-list-style-sets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbicadmin

```bash
$ singularity exec <container> /usr/local/bin/dbicadmin
$ podman run --it --rm --entrypoint /usr/local/bin/dbicadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbicadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpcrunner.pl

```bash
$ singularity exec <container> /usr/local/bin/hpcrunner.pl
$ podman run --it --rm --entrypoint /usr/local/bin/hpcrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hpcrunner.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### imgsize

```bash
$ singularity exec <container> /usr/local/bin/imgsize
$ podman run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpage

```bash
$ singularity exec <container> /usr/local/bin/tpage
$ podman run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttree

```bash
$ singularity exec <container> /usr/local/bin/ttree
$ podman run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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