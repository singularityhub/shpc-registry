---
layout: container
name:  "quay.io/biocontainers/berokka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/berokka/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/berokka/container.yaml"
updated_at: "2023-07-21 03:29:09.515954"
latest: "0.2.3--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/berokka"
aliases:
 - "berokka"
 - "bam2bedgraph"
 - "bp_pairwise_kaks"
 - "bp_find-blast-matches.pl"
 - "t_coffee"
 - "baseml"
 - "basemlg"
 - "chi2"
 - "codeml"
 - "evolver"
 - "infinitesites"
versions:
 - "0.2.3--hdfd78af_3"
 - "0.2--3"
description: "shpc-registry automated BioContainers addition for berokka"
config: {"url": "https://biocontainers.pro/tools/berokka", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for berokka", "latest": {"0.2.3--hdfd78af_3": "sha256:1fea82109bc0ebd7f2abe7a1f36b5798ce54114f14ae8941339d360de793f7d8"}, "tags": {"0.2.3--hdfd78af_3": "sha256:1fea82109bc0ebd7f2abe7a1f36b5798ce54114f14ae8941339d360de793f7d8", "0.2--3": "sha256:366ef78a81994088121c43d1ccc21da8645ce41fa0ecf260a79001ae599d1d4d"}, "docker": "quay.io/biocontainers/berokka", "aliases": {"berokka": "/usr/local/bin/berokka", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bp_pairwise_kaks": "/usr/local/bin/bp_pairwise_kaks", "bp_find-blast-matches.pl": "/usr/local/bin/bp_find-blast-matches.pl", "t_coffee": "/usr/local/bin/t_coffee", "baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg", "chi2": "/usr/local/bin/chi2", "codeml": "/usr/local/bin/codeml", "evolver": "/usr/local/bin/evolver", "infinitesites": "/usr/local/bin/infinitesites"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/berokka.
shpc-registry automated BioContainers addition for berokka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/berokka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/berokka:0.2.3--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/berokka/0.2.3--hdfd78af_3
$ module help quay.io/biocontainers/berokka/0.2.3--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### berokka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### berokka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### berokka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### berokka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### berokka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### berokka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### berokka

```bash
$ singularity exec <container> /usr/local/bin/berokka
$ podman run --it --rm --entrypoint /usr/local/bin/berokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/berokka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_find-blast-matches.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_find-blast-matches.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_find-blast-matches.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### t_coffee

```bash
$ singularity exec <container> /usr/local/bin/t_coffee
$ podman run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/t_coffee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basemlg

```bash
$ singularity exec <container> /usr/local/bin/basemlg
$ podman run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chi2

```bash
$ singularity exec <container> /usr/local/bin/chi2
$ podman run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codeml

```bash
$ singularity exec <container> /usr/local/bin/codeml
$ podman run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codeml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evolver

```bash
$ singularity exec <container> /usr/local/bin/evolver
$ podman run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evolver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infinitesites

```bash
$ singularity exec <container> /usr/local/bin/infinitesites
$ podman run --it --rm --entrypoint /usr/local/bin/infinitesites   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infinitesites   -v ${PWD} -w ${PWD} <container> -c " $@"
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