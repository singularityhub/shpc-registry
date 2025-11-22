---
layout: container
name:  "quay.io/biocontainers/evidencemodeler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/evidencemodeler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/evidencemodeler/container.yaml"
updated_at: "2025-11-22 03:55:47.750273"
latest: "2.1.0--h9948957_5"
container_url: "https://biocontainers.pro/tools/evidencemodeler"
aliases:
 - "evidence_modeler.pl"
 - "perl5.26.2"
 - "podselect"
versions:
 - "v1.1.1--0"
 - "1.1.1--hdfd78af_3"
 - "2.1.0--h87f3376_0"
 - "2.1.0--hdbdd923_1"
 - "2.1.0--hdbdd923_2"
 - "2.1.0--h503566f_4"
 - "2.1.0--h9948957_5"
description: "shpc-registry automated BioContainers addition for evidencemodeler"
config: {"url": "https://biocontainers.pro/tools/evidencemodeler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for evidencemodeler", "latest": {"2.1.0--h9948957_5": "sha256:5c6c5a02547adcd2ea93947c1956e24bf10953641b1c1ff53e018f65446cfaf1"}, "tags": {"v1.1.1--0": "sha256:1fc0accf25612d643919a4781d2e94184b35090d2b3da3f389d24a60cf77cb21", "1.1.1--hdfd78af_3": "sha256:1b241906bc27843924e692aef5f86c73dc01734c1b8af3b43232a127608285a1", "2.1.0--h87f3376_0": "sha256:d6ccd1414e1a8ef3a93343380de1fa93a11a84d8fa3aecda341ed3b2cdac5463", "2.1.0--hdbdd923_1": "sha256:112c8e7cd384a4ce5405ca33467dff0f5cfe5b2e1978126c27e33ac717ffd91c", "2.1.0--hdbdd923_2": "sha256:6e2c85d58498318d7ff9664ce739100d2a495351eb8b3d65e101a47a73cd2481", "2.1.0--h503566f_4": "sha256:23a40580cbd0d25de89f10d98d58630e7185c8b00dbe59f463f1532c8728244c", "2.1.0--h9948957_5": "sha256:5c6c5a02547adcd2ea93947c1956e24bf10953641b1c1ff53e018f65446cfaf1"}, "docker": "quay.io/biocontainers/evidencemodeler", "aliases": {"evidence_modeler.pl": "/usr/local/bin/evidence_modeler.pl", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/evidencemodeler.
shpc-registry automated BioContainers addition for evidencemodeler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/evidencemodeler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/evidencemodeler:2.1.0--h9948957_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/evidencemodeler/2.1.0--h9948957_5
$ module help quay.io/biocontainers/evidencemodeler/2.1.0--h9948957_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### evidencemodeler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### evidencemodeler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### evidencemodeler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### evidencemodeler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### evidencemodeler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### evidencemodeler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### evidence_modeler.pl

```bash
$ singularity exec <container> /usr/local/bin/evidence_modeler.pl
$ podman run --it --rm --entrypoint /usr/local/bin/evidence_modeler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evidence_modeler.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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