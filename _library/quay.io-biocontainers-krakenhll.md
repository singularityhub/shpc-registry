---
layout: container
name:  "quay.io/biocontainers/krakenhll"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/krakenhll/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/krakenhll/container.yaml"
updated_at: "2023-11-22 02:48:11.259314"
latest: "0.4.8--pl526ha92aebf_1"
container_url: "https://biocontainers.pro/tools/krakenhll"
aliases:
 - "build_taxdb"
 - "krakenhll"
 - "krakenhll-build"
 - "krakenhll-download"
 - "krakenhll-extract-reads"
 - "krakenhll-filter"
 - "krakenhll-mpa-report"
 - "krakenhll-report"
 - "krakenhll-translate"
 - "read_merger.pl"
 - "jellyfish"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "lwp-download"
 - "lwp-dump"
 - "lwp-mirror"
 - "lwp-request"
 - "perl5.26.2"
 - "podselect"
versions:
 - "0.4.8--pl526ha92aebf_1"
description: "shpc-registry automated BioContainers addition for krakenhll"
config: {"url": "https://biocontainers.pro/tools/krakenhll", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for krakenhll", "latest": {"0.4.8--pl526ha92aebf_1": "sha256:00f1c37d4e35555ec7936081d77346707fd2d54aec15941f4d35480dc72b60ec"}, "tags": {"0.4.8--pl526ha92aebf_1": "sha256:00f1c37d4e35555ec7936081d77346707fd2d54aec15941f4d35480dc72b60ec"}, "docker": "quay.io/biocontainers/krakenhll", "aliases": {"build_taxdb": "/usr/local/bin/build_taxdb", "krakenhll": "/usr/local/bin/krakenhll", "krakenhll-build": "/usr/local/bin/krakenhll-build", "krakenhll-download": "/usr/local/bin/krakenhll-download", "krakenhll-extract-reads": "/usr/local/bin/krakenhll-extract-reads", "krakenhll-filter": "/usr/local/bin/krakenhll-filter", "krakenhll-mpa-report": "/usr/local/bin/krakenhll-mpa-report", "krakenhll-report": "/usr/local/bin/krakenhll-report", "krakenhll-translate": "/usr/local/bin/krakenhll-translate", "read_merger.pl": "/usr/local/bin/read_merger.pl", "jellyfish": "/usr/local/bin/jellyfish", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "lwp-download": "/usr/local/bin/lwp-download", "lwp-dump": "/usr/local/bin/lwp-dump", "lwp-mirror": "/usr/local/bin/lwp-mirror", "lwp-request": "/usr/local/bin/lwp-request", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/krakenhll.
shpc-registry automated BioContainers addition for krakenhll
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/krakenhll
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/krakenhll:0.4.8--pl526ha92aebf_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/krakenhll/0.4.8--pl526ha92aebf_1
$ module help quay.io/biocontainers/krakenhll/0.4.8--pl526ha92aebf_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### krakenhll-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### krakenhll-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### krakenhll-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### krakenhll-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### krakenhll-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### krakenhll-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### build_taxdb

```bash
$ singularity exec <container> /usr/local/bin/build_taxdb
$ podman run --it --rm --entrypoint /usr/local/bin/build_taxdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_taxdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll

```bash
$ singularity exec <container> /usr/local/bin/krakenhll
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll-build

```bash
$ singularity exec <container> /usr/local/bin/krakenhll-build
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll-download

```bash
$ singularity exec <container> /usr/local/bin/krakenhll-download
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll-extract-reads

```bash
$ singularity exec <container> /usr/local/bin/krakenhll-extract-reads
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll-extract-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll-extract-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll-filter

```bash
$ singularity exec <container> /usr/local/bin/krakenhll-filter
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/krakenhll-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll-report

```bash
$ singularity exec <container> /usr/local/bin/krakenhll-report
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### krakenhll-translate

```bash
$ singularity exec <container> /usr/local/bin/krakenhll-translate
$ podman run --it --rm --entrypoint /usr/local/bin/krakenhll-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/krakenhll-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_merger.pl

```bash
$ singularity exec <container> /usr/local/bin/read_merger.pl
$ podman run --it --rm --entrypoint /usr/local/bin/read_merger.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_merger.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### lwp-download

```bash
$ singularity exec <container> /usr/local/bin/lwp-download
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-dump

```bash
$ singularity exec <container> /usr/local/bin/lwp-dump
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-mirror

```bash
$ singularity exec <container> /usr/local/bin/lwp-mirror
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-request

```bash
$ singularity exec <container> /usr/local/bin/lwp-request
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
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