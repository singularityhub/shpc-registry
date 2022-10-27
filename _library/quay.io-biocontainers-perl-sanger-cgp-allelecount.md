---
layout: container
name:  "quay.io/biocontainers/perl-sanger-cgp-allelecount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-sanger-cgp-allelecount/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-sanger-cgp-allelecount/container.yaml"
updated_at: "2022-10-27 00:48:34.494997"
latest: "4.3.0--pl5321hec16e2b_0"
container_url: "https://biocontainers.pro/tools/perl-sanger-cgp-allelecount"
aliases:
 - "alleleCounter.pl"
 - "alleleCounterToJson.pl"
 - "cgpAppendIdsToVcf.pl"
 - "cgpVCFSplit.pl"
 - "cover"
 - "cpancover"
 - "gcov2perl"
versions:
 - "4.3.0--pl5321hec16e2b_0"
description: "shpc-registry automated BioContainers addition for perl-sanger-cgp-allelecount"
config: {"url": "https://biocontainers.pro/tools/perl-sanger-cgp-allelecount", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-sanger-cgp-allelecount", "latest": {"4.3.0--pl5321hec16e2b_0": "sha256:4a195d434a067d25cdc60f94adf8452ae91b7f3748829e206d2b35297d03d7e2"}, "tags": {"4.3.0--pl5321hec16e2b_0": "sha256:4a195d434a067d25cdc60f94adf8452ae91b7f3748829e206d2b35297d03d7e2"}, "docker": "quay.io/biocontainers/perl-sanger-cgp-allelecount", "aliases": {"alleleCounter.pl": "/usr/local/bin/alleleCounter.pl", "alleleCounterToJson.pl": "/usr/local/bin/alleleCounterToJson.pl", "cgpAppendIdsToVcf.pl": "/usr/local/bin/cgpAppendIdsToVcf.pl", "cgpVCFSplit.pl": "/usr/local/bin/cgpVCFSplit.pl", "cover": "/usr/local/bin/cover", "cpancover": "/usr/local/bin/cpancover", "gcov2perl": "/usr/local/bin/gcov2perl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-sanger-cgp-allelecount.
shpc-registry automated BioContainers addition for perl-sanger-cgp-allelecount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-allelecount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-allelecount:4.3.0--pl5321hec16e2b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-sanger-cgp-allelecount/4.3.0--pl5321hec16e2b_0
$ module help quay.io/biocontainers/perl-sanger-cgp-allelecount/4.3.0--pl5321hec16e2b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-sanger-cgp-allelecount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-allelecount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-allelecount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-sanger-cgp-allelecount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-sanger-cgp-allelecount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-sanger-cgp-allelecount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alleleCounter.pl

```bash
$ singularity exec <container> /usr/local/bin/alleleCounter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alleleCounter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleCounter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alleleCounterToJson.pl

```bash
$ singularity exec <container> /usr/local/bin/alleleCounterToJson.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alleleCounterToJson.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleCounterToJson.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpAppendIdsToVcf.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpAppendIdsToVcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpVCFSplit.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpVCFSplit.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cover

```bash
$ singularity exec <container> /usr/local/bin/cover
$ podman run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpancover

```bash
$ singularity exec <container> /usr/local/bin/cpancover
$ podman run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov2perl

```bash
$ singularity exec <container> /usr/local/bin/gcov2perl
$ podman run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
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