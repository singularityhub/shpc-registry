---
layout: container
name:  "quay.io/biocontainers/seqfu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqfu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqfu/container.yaml"
updated_at: "2023-11-11 03:40:51.076684"
latest: "1.9.1--h38613fd_0"
container_url: "https://biocontainers.pro/tools/seqfu"
aliases:
 - "dadaist2-mergeseqs"
 - "fu-16Sregion"
 - "fu-cov"
 - "fu-homocomp"
 - "fu-index"
 - "fu-msa"
 - "fu-multirelabel"
 - "fu-nanotags"
 - "fu-orf"
 - "fu-primers"
 - "fu-shred"
 - "fu-sw"
 - "fu-tabcheck"
 - "fu-virfilter"
 - "seqfu"
versions:
 - "1.9.1--h38613fd_0"
description: "shpc-registry automated BioContainers addition for seqfu"
config: {"url": "https://biocontainers.pro/tools/seqfu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqfu", "latest": {"1.9.1--h38613fd_0": "sha256:41311b69fd24c9da0ad9213cee97efc34bb4a87b196fbc5c79204182dfab4865"}, "tags": {"1.9.1--h38613fd_0": "sha256:41311b69fd24c9da0ad9213cee97efc34bb4a87b196fbc5c79204182dfab4865"}, "docker": "quay.io/biocontainers/seqfu", "aliases": {"dadaist2-mergeseqs": "/usr/local/bin/dadaist2-mergeseqs", "fu-16Sregion": "/usr/local/bin/fu-16Sregion", "fu-cov": "/usr/local/bin/fu-cov", "fu-homocomp": "/usr/local/bin/fu-homocomp", "fu-index": "/usr/local/bin/fu-index", "fu-msa": "/usr/local/bin/fu-msa", "fu-multirelabel": "/usr/local/bin/fu-multirelabel", "fu-nanotags": "/usr/local/bin/fu-nanotags", "fu-orf": "/usr/local/bin/fu-orf", "fu-primers": "/usr/local/bin/fu-primers", "fu-shred": "/usr/local/bin/fu-shred", "fu-sw": "/usr/local/bin/fu-sw", "fu-tabcheck": "/usr/local/bin/fu-tabcheck", "fu-virfilter": "/usr/local/bin/fu-virfilter", "seqfu": "/usr/local/bin/seqfu"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqfu.
shpc-registry automated BioContainers addition for seqfu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqfu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqfu:1.9.1--h38613fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqfu/1.9.1--h38613fd_0
$ module help quay.io/biocontainers/seqfu/1.9.1--h38613fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqfu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqfu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqfu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqfu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqfu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqfu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dadaist2-mergeseqs

```bash
$ singularity exec <container> /usr/local/bin/dadaist2-mergeseqs
$ podman run --it --rm --entrypoint /usr/local/bin/dadaist2-mergeseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dadaist2-mergeseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-16Sregion

```bash
$ singularity exec <container> /usr/local/bin/fu-16Sregion
$ podman run --it --rm --entrypoint /usr/local/bin/fu-16Sregion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-16Sregion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-cov

```bash
$ singularity exec <container> /usr/local/bin/fu-cov
$ podman run --it --rm --entrypoint /usr/local/bin/fu-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-homocomp

```bash
$ singularity exec <container> /usr/local/bin/fu-homocomp
$ podman run --it --rm --entrypoint /usr/local/bin/fu-homocomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-homocomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-index

```bash
$ singularity exec <container> /usr/local/bin/fu-index
$ podman run --it --rm --entrypoint /usr/local/bin/fu-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-msa

```bash
$ singularity exec <container> /usr/local/bin/fu-msa
$ podman run --it --rm --entrypoint /usr/local/bin/fu-msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-multirelabel

```bash
$ singularity exec <container> /usr/local/bin/fu-multirelabel
$ podman run --it --rm --entrypoint /usr/local/bin/fu-multirelabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-multirelabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-nanotags

```bash
$ singularity exec <container> /usr/local/bin/fu-nanotags
$ podman run --it --rm --entrypoint /usr/local/bin/fu-nanotags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-nanotags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-orf

```bash
$ singularity exec <container> /usr/local/bin/fu-orf
$ podman run --it --rm --entrypoint /usr/local/bin/fu-orf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-orf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-primers

```bash
$ singularity exec <container> /usr/local/bin/fu-primers
$ podman run --it --rm --entrypoint /usr/local/bin/fu-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-shred

```bash
$ singularity exec <container> /usr/local/bin/fu-shred
$ podman run --it --rm --entrypoint /usr/local/bin/fu-shred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-shred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-sw

```bash
$ singularity exec <container> /usr/local/bin/fu-sw
$ podman run --it --rm --entrypoint /usr/local/bin/fu-sw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-sw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-tabcheck

```bash
$ singularity exec <container> /usr/local/bin/fu-tabcheck
$ podman run --it --rm --entrypoint /usr/local/bin/fu-tabcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-tabcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-virfilter

```bash
$ singularity exec <container> /usr/local/bin/fu-virfilter
$ podman run --it --rm --entrypoint /usr/local/bin/fu-virfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-virfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqfu

```bash
$ singularity exec <container> /usr/local/bin/seqfu
$ podman run --it --rm --entrypoint /usr/local/bin/seqfu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqfu   -v ${PWD} -w ${PWD} <container> -c " $@"
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