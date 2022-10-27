---
layout: container
name:  "quay.io/biocontainers/perl-bio-phylo-cipres"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-phylo-cipres/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-phylo-cipres/container.yaml"
updated_at: "2022-10-27 01:13:15.068973"
latest: "v0.2.1--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-bio-phylo-cipres"
aliases:
 - "cipresrun"
versions:
 - "v0.2.1--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-bio-phylo-cipres"
config: {"url": "https://biocontainers.pro/tools/perl-bio-phylo-cipres", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-phylo-cipres", "latest": {"v0.2.1--pl5321hdfd78af_2": "sha256:a2dc08e700c19273c2d80a0c8b688cdd3c474b5b22906d10c534beb21ae0e9ce"}, "tags": {"v0.2.1--pl5321hdfd78af_2": "sha256:a2dc08e700c19273c2d80a0c8b688cdd3c474b5b22906d10c534beb21ae0e9ce"}, "docker": "quay.io/biocontainers/perl-bio-phylo-cipres", "aliases": {"cipresrun": "/usr/local/bin/cipresrun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-phylo-cipres.
shpc-registry automated BioContainers addition for perl-bio-phylo-cipres
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-phylo-cipres
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-phylo-cipres:v0.2.1--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-phylo-cipres/v0.2.1--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-bio-phylo-cipres/v0.2.1--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-phylo-cipres-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-phylo-cipres-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-phylo-cipres-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-phylo-cipres-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-phylo-cipres-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-phylo-cipres-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cipresrun

```bash
$ singularity exec <container> /usr/local/bin/cipresrun
$ podman run --it --rm --entrypoint /usr/local/bin/cipresrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cipresrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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