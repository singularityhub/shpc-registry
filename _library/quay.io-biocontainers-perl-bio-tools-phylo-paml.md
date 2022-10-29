---
layout: container
name:  "quay.io/biocontainers/perl-bio-tools-phylo-paml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-tools-phylo-paml/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-tools-phylo-paml/container.yaml"
updated_at: "2022-10-29 05:55:47.749249"
latest: "1.7.3--pl5262hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-bio-tools-phylo-paml"
aliases:
 - "SOAPsh.pl"
 - "ace.pl"
 - "acyclic"
 - "annotate"
 - "bam2bedgraph"
 - "bamToGBrowse.pl"
 - "baseml"
 - "basemlg"
 - "bcomps"
 - "bdf2gdfont.pl"
versions:
 - "1.7.3--pl5262hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-bio-tools-phylo-paml"
config: {"url": "https://biocontainers.pro/tools/perl-bio-tools-phylo-paml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-tools-phylo-paml", "latest": {"1.7.3--pl5262hdfd78af_2": "sha256:53fa967afabc8d2bd3ca42b490ad55f3311eaf57716b73df2d27118c456218f1"}, "tags": {"1.7.3--pl5262hdfd78af_2": "sha256:53fa967afabc8d2bd3ca42b490ad55f3311eaf57716b73df2d27118c456218f1"}, "docker": "quay.io/biocontainers/perl-bio-tools-phylo-paml", "aliases": {"SOAPsh.pl": "/usr/local/bin/SOAPsh.pl", "ace.pl": "/usr/local/bin/ace.pl", "acyclic": "/usr/local/bin/acyclic", "annotate": "/usr/local/bin/annotate", "bam2bedgraph": "/usr/local/bin/bam2bedgraph", "bamToGBrowse.pl": "/usr/local/bin/bamToGBrowse.pl", "baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg", "bcomps": "/usr/local/bin/bcomps", "bdf2gdfont.pl": "/usr/local/bin/bdf2gdfont.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-tools-phylo-paml.
shpc-registry automated BioContainers addition for perl-bio-tools-phylo-paml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-tools-phylo-paml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-tools-phylo-paml:1.7.3--pl5262hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-tools-phylo-paml/1.7.3--pl5262hdfd78af_2
$ module help quay.io/biocontainers/perl-bio-tools-phylo-paml/1.7.3--pl5262hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-tools-phylo-paml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-tools-phylo-paml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-tools-phylo-paml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-tools-phylo-paml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-tools-phylo-paml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-tools-phylo-paml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SOAPsh.pl

```bash
$ singularity exec <container> /usr/local/bin/SOAPsh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SOAPsh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace.pl

```bash
$ singularity exec <container> /usr/local/bin/ace.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bedgraph

```bash
$ singularity exec <container> /usr/local/bin/bam2bedgraph
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bedgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToGBrowse.pl

```bash
$ singularity exec <container> /usr/local/bin/bamToGBrowse.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bamToGBrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToGBrowse.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdf2gdfont.pl

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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