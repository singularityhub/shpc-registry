---
layout: container
name:  "quay.io/biocontainers/n50"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/n50/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/n50/container.yaml"
updated_at: "2023-01-31 18:01:30.114694"
latest: "1.5.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/n50"
aliases:
 - "fqc"
 - "fqlen.pl"
 - "fu-cat"
 - "fu-compare"
 - "fu-count"
 - "fu-extract"
 - "fu-grep"
 - "fu-hash"
 - "fu-len"
 - "fu-rename"
 - "fu-sort"
 - "fu-uniq"
 - "n50"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.5.0--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for n50"
config: {"url": "https://biocontainers.pro/tools/n50", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for n50", "latest": {"1.5.0--pl5321hdfd78af_0": "sha256:922c631bfe7177b00b92556e28920909f8dadbfba6760fc49582efed0128d886"}, "tags": {"1.5.0--pl5321hdfd78af_0": "sha256:922c631bfe7177b00b92556e28920909f8dadbfba6760fc49582efed0128d886"}, "docker": "quay.io/biocontainers/n50", "aliases": {"fqc": "/usr/local/bin/fqc", "fqlen.pl": "/usr/local/bin/fqlen.pl", "fu-cat": "/usr/local/bin/fu-cat", "fu-compare": "/usr/local/bin/fu-compare", "fu-count": "/usr/local/bin/fu-count", "fu-extract": "/usr/local/bin/fu-extract", "fu-grep": "/usr/local/bin/fu-grep", "fu-hash": "/usr/local/bin/fu-hash", "fu-len": "/usr/local/bin/fu-len", "fu-rename": "/usr/local/bin/fu-rename", "fu-sort": "/usr/local/bin/fu-sort", "fu-uniq": "/usr/local/bin/fu-uniq", "n50": "/usr/local/bin/n50", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/n50.
shpc-registry automated BioContainers addition for n50
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/n50
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/n50:1.5.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/n50/1.5.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/n50/1.5.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### n50-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### n50-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### n50-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### n50-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### n50-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### n50-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqc

```bash
$ singularity exec <container> /usr/local/bin/fqc
$ podman run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fqlen.pl

```bash
$ singularity exec <container> /usr/local/bin/fqlen.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fqlen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqlen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-cat

```bash
$ singularity exec <container> /usr/local/bin/fu-cat
$ podman run --it --rm --entrypoint /usr/local/bin/fu-cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-compare

```bash
$ singularity exec <container> /usr/local/bin/fu-compare
$ podman run --it --rm --entrypoint /usr/local/bin/fu-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-count

```bash
$ singularity exec <container> /usr/local/bin/fu-count
$ podman run --it --rm --entrypoint /usr/local/bin/fu-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-extract

```bash
$ singularity exec <container> /usr/local/bin/fu-extract
$ podman run --it --rm --entrypoint /usr/local/bin/fu-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-extract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-grep

```bash
$ singularity exec <container> /usr/local/bin/fu-grep
$ podman run --it --rm --entrypoint /usr/local/bin/fu-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-hash

```bash
$ singularity exec <container> /usr/local/bin/fu-hash
$ podman run --it --rm --entrypoint /usr/local/bin/fu-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-len

```bash
$ singularity exec <container> /usr/local/bin/fu-len
$ podman run --it --rm --entrypoint /usr/local/bin/fu-len   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-len   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-rename

```bash
$ singularity exec <container> /usr/local/bin/fu-rename
$ podman run --it --rm --entrypoint /usr/local/bin/fu-rename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-rename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-sort

```bash
$ singularity exec <container> /usr/local/bin/fu-sort
$ podman run --it --rm --entrypoint /usr/local/bin/fu-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-uniq

```bash
$ singularity exec <container> /usr/local/bin/fu-uniq
$ podman run --it --rm --entrypoint /usr/local/bin/fu-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### n50

```bash
$ singularity exec <container> /usr/local/bin/n50
$ podman run --it --rm --entrypoint /usr/local/bin/n50   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/n50   -v ${PWD} -w ${PWD} <container> -c " $@"
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