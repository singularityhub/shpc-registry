---
layout: container
name:  "quay.io/biocontainers/ggd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ggd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ggd/container.yaml"
updated_at: "2025-02-02 03:14:11.752712"
latest: "1.1.3--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/ggd"
aliases:
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "check-sort-order"
 - "conda-build"
 - "conda-convert"
 - "conda-debug"
 - "conda-develop"
 - "conda-index"
 - "conda-inspect"
 - "conda-metapackage"
 - "conda-render"
 - "conda-skeleton"
 - "ggd"
 - "gsort"
 - "patchelf"
 - "pkginfo"
 - "rg"
 - "conda-env"
 - "cph"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
 - "cyvcf2"
versions:
 - "1.1.3--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for ggd"
config: {"url": "https://biocontainers.pro/tools/ggd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ggd", "latest": {"1.1.3--pyh3252c3a_0": "sha256:575286a303e811f67e002e36146e4da21cdef4d84864cd5b355f574e0ac6777a"}, "tags": {"1.1.3--pyh3252c3a_0": "sha256:575286a303e811f67e002e36146e4da21cdef4d84864cd5b355f574e0ac6777a"}, "docker": "quay.io/biocontainers/ggd", "aliases": {"bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "check-sort-order": "/usr/local/bin/check-sort-order", "conda-build": "/usr/local/bin/conda-build", "conda-convert": "/usr/local/bin/conda-convert", "conda-debug": "/usr/local/bin/conda-debug", "conda-develop": "/usr/local/bin/conda-develop", "conda-index": "/usr/local/bin/conda-index", "conda-inspect": "/usr/local/bin/conda-inspect", "conda-metapackage": "/usr/local/bin/conda-metapackage", "conda-render": "/usr/local/bin/conda-render", "conda-skeleton": "/usr/local/bin/conda-skeleton", "ggd": "/usr/local/bin/ggd", "gsort": "/usr/local/bin/gsort", "patchelf": "/usr/local/bin/patchelf", "pkginfo": "/usr/local/bin/pkginfo", "rg": "/usr/local/bin/rg", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk", "cyvcf2": "/usr/local/bin/cyvcf2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ggd.
shpc-registry automated BioContainers addition for ggd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ggd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ggd:1.1.3--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ggd/1.1.3--pyh3252c3a_0
$ module help quay.io/biocontainers/ggd/1.1.3--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ggd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ggd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ggd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ggd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ggd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ggd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check-sort-order

```bash
$ singularity exec <container> /usr/local/bin/check-sort-order
$ podman run --it --rm --entrypoint /usr/local/bin/check-sort-order   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check-sort-order   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-build

```bash
$ singularity exec <container> /usr/local/bin/conda-build
$ podman run --it --rm --entrypoint /usr/local/bin/conda-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-convert

```bash
$ singularity exec <container> /usr/local/bin/conda-convert
$ podman run --it --rm --entrypoint /usr/local/bin/conda-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-debug

```bash
$ singularity exec <container> /usr/local/bin/conda-debug
$ podman run --it --rm --entrypoint /usr/local/bin/conda-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-develop

```bash
$ singularity exec <container> /usr/local/bin/conda-develop
$ podman run --it --rm --entrypoint /usr/local/bin/conda-develop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-develop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-index

```bash
$ singularity exec <container> /usr/local/bin/conda-index
$ podman run --it --rm --entrypoint /usr/local/bin/conda-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-inspect

```bash
$ singularity exec <container> /usr/local/bin/conda-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/conda-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-metapackage

```bash
$ singularity exec <container> /usr/local/bin/conda-metapackage
$ podman run --it --rm --entrypoint /usr/local/bin/conda-metapackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-metapackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-render

```bash
$ singularity exec <container> /usr/local/bin/conda-render
$ podman run --it --rm --entrypoint /usr/local/bin/conda-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-skeleton

```bash
$ singularity exec <container> /usr/local/bin/conda-skeleton
$ podman run --it --rm --entrypoint /usr/local/bin/conda-skeleton   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-skeleton   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ggd

```bash
$ singularity exec <container> /usr/local/bin/ggd
$ podman run --it --rm --entrypoint /usr/local/bin/ggd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ggd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsort

```bash
$ singularity exec <container> /usr/local/bin/gsort
$ podman run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### patchelf

```bash
$ singularity exec <container> /usr/local/bin/patchelf
$ podman run --it --rm --entrypoint /usr/local/bin/patchelf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/patchelf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkginfo

```bash
$ singularity exec <container> /usr/local/bin/pkginfo
$ podman run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rg

```bash
$ singularity exec <container> /usr/local/bin/rg
$ podman run --it --rm --entrypoint /usr/local/bin/rg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-env

```bash
$ singularity exec <container> /usr/local/bin/conda-env
$ podman run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git

```bash
$ singularity exec <container> /usr/local/bin/git
$ podman run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-cvsserver

```bash
$ singularity exec <container> /usr/local/bin/git-cvsserver
$ podman run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/git-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-shell

```bash
$ singularity exec <container> /usr/local/bin/git-shell
$ podman run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-archive

```bash
$ singularity exec <container> /usr/local/bin/git-upload-archive
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/git-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gitk

```bash
$ singularity exec <container> /usr/local/bin/gitk
$ podman run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
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