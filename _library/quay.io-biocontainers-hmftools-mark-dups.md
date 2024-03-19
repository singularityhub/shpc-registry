---
layout: container
name:  "quay.io/biocontainers/hmftools-mark-dups"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-mark-dups/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-mark-dups/container.yaml"
updated_at: "2024-03-19 02:34:24.371081"
latest: "1.1.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmftools-mark-dups"
aliases:
 - "annot-tsv"
 - "markdups"
 - "ldc-build-runtime"
 - "ldc-profdata"
 - "ldc-prune-cache"
 - "ldc2"
 - "ldmd2"
 - "sambamba"
 - "jwebserver"
 - "pcre2posix_test"
 - "jpackage"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "hb-info"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "tjbench"
 - "jfr"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "aserver"
 - "ace2sam"
versions:
 - "1.1--hdfd78af_0"
 - "1.1.2--hdfd78af_0"
description: "singularity registry hpc automated addition for hmftools-mark-dups"
config: {"url": "https://biocontainers.pro/tools/hmftools-mark-dups", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hmftools-mark-dups", "latest": {"1.1.2--hdfd78af_0": "sha256:c33439d6c93905dc946e2d8df0243f8ebc166012b1f7e26cce26b2d519f3d5ce"}, "tags": {"1.1--hdfd78af_0": "sha256:066faa9ec1d9ba9b84b1d49f708ff42422df188157bfa5794ff75cc7e4ae5b54", "1.1.2--hdfd78af_0": "sha256:c33439d6c93905dc946e2d8df0243f8ebc166012b1f7e26cce26b2d519f3d5ce"}, "docker": "quay.io/biocontainers/hmftools-mark-dups", "aliases": {"annot-tsv": "/usr/local/bin/annot-tsv", "markdups": "/usr/local/bin/markdups", "ldc-build-runtime": "/usr/local/bin/ldc-build-runtime", "ldc-profdata": "/usr/local/bin/ldc-profdata", "ldc-prune-cache": "/usr/local/bin/ldc-prune-cache", "ldc2": "/usr/local/bin/ldc2", "ldmd2": "/usr/local/bin/ldmd2", "sambamba": "/usr/local/bin/sambamba", "jwebserver": "/usr/local/bin/jwebserver", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "jpackage": "/usr/local/bin/jpackage", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "hb-info": "/usr/local/bin/hb-info", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "tjbench": "/usr/local/bin/tjbench", "jfr": "/usr/local/bin/jfr", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "aserver": "/usr/local/bin/aserver", "ace2sam": "/usr/local/bin/ace2sam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-mark-dups.
singularity registry hpc automated addition for hmftools-mark-dups
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-mark-dups
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-mark-dups:1.1.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-mark-dups/1.1.2--hdfd78af_0
$ module help quay.io/biocontainers/hmftools-mark-dups/1.1.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-mark-dups-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-mark-dups-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-mark-dups-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-mark-dups-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-mark-dups-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-mark-dups-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdups

```bash
$ singularity exec <container> /usr/local/bin/markdups
$ podman run --it --rm --entrypoint /usr/local/bin/markdups   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdups   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-build-runtime

```bash
$ singularity exec <container> /usr/local/bin/ldc-build-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-profdata

```bash
$ singularity exec <container> /usr/local/bin/ldc-profdata
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-prune-cache

```bash
$ singularity exec <container> /usr/local/bin/ldc-prune-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc2

```bash
$ singularity exec <container> /usr/local/bin/ldc2
$ podman run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldmd2

```bash
$ singularity exec <container> /usr/local/bin/ldmd2
$ podman run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sambamba

```bash
$ singularity exec <container> /usr/local/bin/sambamba
$ podman run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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