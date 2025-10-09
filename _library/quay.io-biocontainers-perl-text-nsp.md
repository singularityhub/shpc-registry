---
layout: container
name:  "quay.io/biocontainers/perl-text-nsp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-text-nsp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-text-nsp/container.yaml"
updated_at: "2025-10-09 03:09:34.024004"
latest: "1.31--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/perl-text-nsp"
aliases:
 - "combig-script.sh"
 - "combig.pl"
 - "count.pl"
 - "count2huge.pl"
 - "find-compounds.pl"
 - "huge-count.pl"
 - "huge-delete.pl"
 - "huge-merge.pl"
 - "huge-sort.pl"
 - "huge-split.pl"
 - "kocos-script.sh"
 - "kocos.pl"
 - "rank-script.sh"
 - "rank.pl"
 - "statistic.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.31--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for perl-text-nsp"
config: {"url": "https://biocontainers.pro/tools/perl-text-nsp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-text-nsp", "latest": {"1.31--pl5321hdfd78af_3": "sha256:c34f9645cfbe56ece8183c2dd1ec5bcdf95d84d198208677572831f585b3c8e5"}, "tags": {"1.31--pl5321hdfd78af_3": "sha256:c34f9645cfbe56ece8183c2dd1ec5bcdf95d84d198208677572831f585b3c8e5"}, "docker": "quay.io/biocontainers/perl-text-nsp", "aliases": {"combig-script.sh": "/usr/local/bin/combig-script.sh", "combig.pl": "/usr/local/bin/combig.pl", "count.pl": "/usr/local/bin/count.pl", "count2huge.pl": "/usr/local/bin/count2huge.pl", "find-compounds.pl": "/usr/local/bin/find-compounds.pl", "huge-count.pl": "/usr/local/bin/huge-count.pl", "huge-delete.pl": "/usr/local/bin/huge-delete.pl", "huge-merge.pl": "/usr/local/bin/huge-merge.pl", "huge-sort.pl": "/usr/local/bin/huge-sort.pl", "huge-split.pl": "/usr/local/bin/huge-split.pl", "kocos-script.sh": "/usr/local/bin/kocos-script.sh", "kocos.pl": "/usr/local/bin/kocos.pl", "rank-script.sh": "/usr/local/bin/rank-script.sh", "rank.pl": "/usr/local/bin/rank.pl", "statistic.pl": "/usr/local/bin/statistic.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-text-nsp.
shpc-registry automated BioContainers addition for perl-text-nsp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-text-nsp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-text-nsp:1.31--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-text-nsp/1.31--pl5321hdfd78af_3
$ module help quay.io/biocontainers/perl-text-nsp/1.31--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-text-nsp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-text-nsp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-text-nsp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-text-nsp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-text-nsp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-text-nsp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### combig-script.sh

```bash
$ singularity exec <container> /usr/local/bin/combig-script.sh
$ podman run --it --rm --entrypoint /usr/local/bin/combig-script.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combig-script.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combig.pl

```bash
$ singularity exec <container> /usr/local/bin/combig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/combig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count.pl

```bash
$ singularity exec <container> /usr/local/bin/count.pl
$ podman run --it --rm --entrypoint /usr/local/bin/count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count2huge.pl

```bash
$ singularity exec <container> /usr/local/bin/count2huge.pl
$ podman run --it --rm --entrypoint /usr/local/bin/count2huge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count2huge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find-compounds.pl

```bash
$ singularity exec <container> /usr/local/bin/find-compounds.pl
$ podman run --it --rm --entrypoint /usr/local/bin/find-compounds.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find-compounds.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huge-count.pl

```bash
$ singularity exec <container> /usr/local/bin/huge-count.pl
$ podman run --it --rm --entrypoint /usr/local/bin/huge-count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huge-count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huge-delete.pl

```bash
$ singularity exec <container> /usr/local/bin/huge-delete.pl
$ podman run --it --rm --entrypoint /usr/local/bin/huge-delete.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huge-delete.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huge-merge.pl

```bash
$ singularity exec <container> /usr/local/bin/huge-merge.pl
$ podman run --it --rm --entrypoint /usr/local/bin/huge-merge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huge-merge.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huge-sort.pl

```bash
$ singularity exec <container> /usr/local/bin/huge-sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/huge-sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huge-sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huge-split.pl

```bash
$ singularity exec <container> /usr/local/bin/huge-split.pl
$ podman run --it --rm --entrypoint /usr/local/bin/huge-split.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huge-split.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kocos-script.sh

```bash
$ singularity exec <container> /usr/local/bin/kocos-script.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kocos-script.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kocos-script.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kocos.pl

```bash
$ singularity exec <container> /usr/local/bin/kocos.pl
$ podman run --it --rm --entrypoint /usr/local/bin/kocos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kocos.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rank-script.sh

```bash
$ singularity exec <container> /usr/local/bin/rank-script.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rank-script.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rank-script.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rank.pl

```bash
$ singularity exec <container> /usr/local/bin/rank.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rank.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rank.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statistic.pl

```bash
$ singularity exec <container> /usr/local/bin/statistic.pl
$ podman run --it --rm --entrypoint /usr/local/bin/statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statistic.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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