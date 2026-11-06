---
layout: container
name:  "quay.io/biocontainers/fadu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fadu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fadu/container.yaml"
updated_at: "2026-11-06 09:33:24.668186"
latest: "1.10.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/fadu"
aliases:
 - "7z"
 - "7za"
 - "7zr"
 - "fadu"
 - "julia"
 - "perl5.44.0"
 - "scalar"
 - "git2"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
 - "cmpfillin"
 - "gpmetis"
 - "graphchk"
 - "m2gmetis"
 - "mpmetis"
 - "ndmetis"
versions:
 - "1.10.1--h9ee0642_0"
description: "singularity registry hpc automated addition for fadu"
config: {"url": "https://biocontainers.pro/tools/fadu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fadu", "latest": {"1.10.1--h9ee0642_0": "sha256:ca73b23aace98c7c241bdbd52b5275638b6a67795b83a9c1f65a6eabd7b10fd7"}, "tags": {"1.10.1--h9ee0642_0": "sha256:ca73b23aace98c7c241bdbd52b5275638b6a67795b83a9c1f65a6eabd7b10fd7"}, "docker": "quay.io/biocontainers/fadu", "aliases": {"7z": "/usr/local/bin/7z", "7za": "/usr/local/bin/7za", "7zr": "/usr/local/bin/7zr", "fadu": "/usr/local/bin/fadu", "julia": "/usr/local/bin/julia", "perl5.44.0": "/usr/local/bin/perl5.44.0", "scalar": "/usr/local/bin/scalar", "git2": "/usr/local/bin/git2", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk", "m2gmetis": "/usr/local/bin/m2gmetis", "mpmetis": "/usr/local/bin/mpmetis", "ndmetis": "/usr/local/bin/ndmetis"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fadu.
singularity registry hpc automated addition for fadu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fadu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fadu:1.10.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fadu/1.10.1--h9ee0642_0
$ module help quay.io/biocontainers/fadu/1.10.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fadu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fadu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fadu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fadu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fadu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fadu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 7z

```bash
$ singularity exec <container> /usr/local/bin/7z
$ podman run --it --rm --entrypoint /usr/local/bin/7z   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/7z   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 7za

```bash
$ singularity exec <container> /usr/local/bin/7za
$ podman run --it --rm --entrypoint /usr/local/bin/7za   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/7za   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 7zr

```bash
$ singularity exec <container> /usr/local/bin/7zr
$ podman run --it --rm --entrypoint /usr/local/bin/7zr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/7zr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fadu

```bash
$ singularity exec <container> /usr/local/bin/fadu
$ podman run --it --rm --entrypoint /usr/local/bin/fadu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fadu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### julia

```bash
$ singularity exec <container> /usr/local/bin/julia
$ podman run --it --rm --entrypoint /usr/local/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.44.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.44.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.44.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.44.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scalar

```bash
$ singularity exec <container> /usr/local/bin/scalar
$ podman run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git2

```bash
$ singularity exec <container> /usr/local/bin/git2
$ podman run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m2gmetis

```bash
$ singularity exec <container> /usr/local/bin/m2gmetis
$ podman run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpmetis

```bash
$ singularity exec <container> /usr/local/bin/mpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndmetis

```bash
$ singularity exec <container> /usr/local/bin/ndmetis
$ podman run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
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