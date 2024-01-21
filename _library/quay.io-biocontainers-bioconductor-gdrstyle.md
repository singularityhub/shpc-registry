---
layout: container
name:  "quay.io/biocontainers/bioconductor-gdrstyle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gdrstyle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gdrstyle/container.yaml"
updated_at: "2024-01-21 02:44:28.810748"
latest: "1.0.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gdrstyle"
aliases:
 - "git2"
 - "pcre2posix_test"
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-gdrstyle"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gdrstyle", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-gdrstyle", "latest": {"1.0.0--r43hdfd78af_0": "sha256:80935e21c9e208433af135e8cfa805a4cc13ba920b1706d88f7f7e7798a493df"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:80935e21c9e208433af135e8cfa805a4cc13ba920b1706d88f7f7e7798a493df"}, "docker": "quay.io/biocontainers/bioconductor-gdrstyle", "aliases": {"git2": "/usr/local/bin/git2", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gdrstyle.
singularity registry hpc automated addition for bioconductor-gdrstyle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gdrstyle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gdrstyle:1.0.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gdrstyle/1.0.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gdrstyle/1.0.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gdrstyle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gdrstyle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gdrstyle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gdrstyle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gdrstyle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gdrstyle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### git2

```bash
$ singularity exec <container> /usr/local/bin/git2
$ podman run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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