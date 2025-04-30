---
layout: container
name:  "quay.io/biocontainers/perl-pod-coverage-trustpod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-pod-coverage-trustpod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-pod-coverage-trustpod/container.yaml"
updated_at: "2025-04-30 03:18:21.979265"
latest: "0.100006--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-pod-coverage-trustpod"
aliases:
 - "pod_cover"
 - "cpanm"
 - "podselect"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.100005--pl5321hdfd78af_0"
 - "0.100006--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-pod-coverage-trustpod"
config: {"url": "https://biocontainers.pro/tools/perl-pod-coverage-trustpod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-pod-coverage-trustpod", "latest": {"0.100006--pl5321hdfd78af_0": "sha256:90a77605e314afc53fcd2c446298875303f74441a4da7a186adddc135a455525"}, "tags": {"0.100005--pl5321hdfd78af_0": "sha256:1a341041a22bc258b55db63132db826a05d46a2a073f6de1dc02515bb1d97824", "0.100006--pl5321hdfd78af_0": "sha256:90a77605e314afc53fcd2c446298875303f74441a4da7a186adddc135a455525"}, "docker": "quay.io/biocontainers/perl-pod-coverage-trustpod", "aliases": {"pod_cover": "/usr/local/bin/pod_cover", "cpanm": "/usr/local/bin/cpanm", "podselect": "/usr/local/bin/podselect", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-pod-coverage-trustpod.
shpc-registry automated BioContainers addition for perl-pod-coverage-trustpod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-pod-coverage-trustpod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-pod-coverage-trustpod:0.100006--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-pod-coverage-trustpod/0.100006--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-pod-coverage-trustpod/0.100006--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-pod-coverage-trustpod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-pod-coverage-trustpod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-pod-coverage-trustpod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-pod-coverage-trustpod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-pod-coverage-trustpod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-pod-coverage-trustpod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pod_cover

```bash
$ singularity exec <container> /usr/local/bin/pod_cover
$ podman run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pod_cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpanm

```bash
$ singularity exec <container> /usr/local/bin/cpanm
$ podman run --it --rm --entrypoint /usr/local/bin/cpanm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpanm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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