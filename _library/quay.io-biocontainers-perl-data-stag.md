---
layout: container
name:  "quay.io/biocontainers/perl-data-stag"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-data-stag/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-data-stag/container.yaml"
updated_at: "2024-01-29 02:49:56.933451"
latest: "0.14--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-data-stag"
aliases:
 - "stag-autoschema.pl"
 - "stag-db.pl"
 - "stag-diff.pl"
 - "stag-drawtree.pl"
 - "stag-filter.pl"
 - "stag-findsubtree.pl"
 - "stag-flatten.pl"
 - "stag-grep.pl"
 - "stag-handle.pl"
 - "stag-itext2simple.pl"
versions:
 - "0.14--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-data-stag"
config: {"url": "https://biocontainers.pro/tools/perl-data-stag", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-data-stag", "latest": {"0.14--pl5321hdfd78af_2": "sha256:4cd57726ef1b844cdc58a766a1ae04709e283d4ebb81b3e348261676103f6928"}, "tags": {"0.14--pl5321hdfd78af_2": "sha256:4cd57726ef1b844cdc58a766a1ae04709e283d4ebb81b3e348261676103f6928"}, "docker": "quay.io/biocontainers/perl-data-stag", "aliases": {"stag-autoschema.pl": "/usr/local/bin/stag-autoschema.pl", "stag-db.pl": "/usr/local/bin/stag-db.pl", "stag-diff.pl": "/usr/local/bin/stag-diff.pl", "stag-drawtree.pl": "/usr/local/bin/stag-drawtree.pl", "stag-filter.pl": "/usr/local/bin/stag-filter.pl", "stag-findsubtree.pl": "/usr/local/bin/stag-findsubtree.pl", "stag-flatten.pl": "/usr/local/bin/stag-flatten.pl", "stag-grep.pl": "/usr/local/bin/stag-grep.pl", "stag-handle.pl": "/usr/local/bin/stag-handle.pl", "stag-itext2simple.pl": "/usr/local/bin/stag-itext2simple.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-data-stag.
shpc-registry automated BioContainers addition for perl-data-stag
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-data-stag
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-data-stag:0.14--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-data-stag/0.14--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-data-stag/0.14--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-data-stag-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-data-stag-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-data-stag-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-data-stag-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-data-stag-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-data-stag-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stag-autoschema.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-autoschema.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-autoschema.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-autoschema.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-db.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-db.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-db.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-diff.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-diff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-diff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-drawtree.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-drawtree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-drawtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-drawtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-filter.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-filter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-filter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-findsubtree.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-findsubtree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-findsubtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-findsubtree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-flatten.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-flatten.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-flatten.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-flatten.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-grep.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-grep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-grep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-grep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-handle.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-handle.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-handle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-handle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stag-itext2simple.pl

```bash
$ singularity exec <container> /usr/local/bin/stag-itext2simple.pl
$ podman run --it --rm --entrypoint /usr/local/bin/stag-itext2simple.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stag-itext2simple.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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