---
layout: container
name:  "quay.io/biocontainers/rnaz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnaz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rnaz/container.yaml"
updated_at: "2025-09-28 03:22:54.924162"
latest: "2.1--pl526h6bb024c_4"
container_url: "https://biocontainers.pro/tools/rnaz"
aliases:
 - "RNAz"
 - "rnazAnnotate.pl"
 - "rnazBEDsort.pl"
 - "rnazBEDstats.pl"
 - "rnazBlast.pl"
 - "rnazCluster.pl"
 - "rnazFilter.pl"
 - "rnazIndex.pl"
 - "rnazMAF2BED.pl"
 - "rnazRandomizeAln.pl"
 - "rnazSelectSeqs.pl"
 - "rnazSort.pl"
 - "rnazWindow.pl"
 - "perl5.26.2"
 - "podselect"
versions:
 - "2.1--pl526h6bb024c_4"
description: "shpc-registry automated BioContainers addition for rnaz"
config: {"url": "https://biocontainers.pro/tools/rnaz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnaz", "latest": {"2.1--pl526h6bb024c_4": "sha256:551ad2f80dd05ef794139d7df61cc25cd3dc795d8e184e88828d4a138dd43e12"}, "tags": {"2.1--pl526h6bb024c_4": "sha256:551ad2f80dd05ef794139d7df61cc25cd3dc795d8e184e88828d4a138dd43e12"}, "docker": "quay.io/biocontainers/rnaz", "aliases": {"RNAz": "/usr/local/bin/RNAz", "rnazAnnotate.pl": "/usr/local/bin/rnazAnnotate.pl", "rnazBEDsort.pl": "/usr/local/bin/rnazBEDsort.pl", "rnazBEDstats.pl": "/usr/local/bin/rnazBEDstats.pl", "rnazBlast.pl": "/usr/local/bin/rnazBlast.pl", "rnazCluster.pl": "/usr/local/bin/rnazCluster.pl", "rnazFilter.pl": "/usr/local/bin/rnazFilter.pl", "rnazIndex.pl": "/usr/local/bin/rnazIndex.pl", "rnazMAF2BED.pl": "/usr/local/bin/rnazMAF2BED.pl", "rnazRandomizeAln.pl": "/usr/local/bin/rnazRandomizeAln.pl", "rnazSelectSeqs.pl": "/usr/local/bin/rnazSelectSeqs.pl", "rnazSort.pl": "/usr/local/bin/rnazSort.pl", "rnazWindow.pl": "/usr/local/bin/rnazWindow.pl", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnaz.
shpc-registry automated BioContainers addition for rnaz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnaz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnaz:2.1--pl526h6bb024c_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnaz/2.1--pl526h6bb024c_4
$ module help quay.io/biocontainers/rnaz/2.1--pl526h6bb024c_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnaz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnaz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnaz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnaz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnaz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnaz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAz

```bash
$ singularity exec <container> /usr/local/bin/RNAz
$ podman run --it --rm --entrypoint /usr/local/bin/RNAz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazAnnotate.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazAnnotate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazAnnotate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazAnnotate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazBEDsort.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazBEDsort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazBEDsort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazBEDsort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazBEDstats.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazBEDstats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazBEDstats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazBEDstats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazBlast.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazBlast.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazBlast.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazBlast.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazCluster.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazCluster.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazCluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazCluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazFilter.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazFilter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazFilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazFilter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazIndex.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazIndex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazIndex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazIndex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazMAF2BED.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazMAF2BED.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazMAF2BED.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazMAF2BED.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazRandomizeAln.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazRandomizeAln.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazRandomizeAln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazRandomizeAln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazSelectSeqs.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazSelectSeqs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazSelectSeqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazSelectSeqs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazSort.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazSort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazSort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazSort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnazWindow.pl

```bash
$ singularity exec <container> /usr/local/bin/rnazWindow.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rnazWindow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnazWindow.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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