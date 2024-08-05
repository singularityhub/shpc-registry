---
layout: container
name:  "quay.io/biocontainers/kraken-ea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kraken-ea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kraken-ea/container.yaml"
updated_at: "2024-08-05 03:11:22.163910"
latest: "0.10.5ea.3--pl526ha92aebf_3"
container_url: "https://biocontainers.pro/tools/kraken-ea"
aliases:
 - "kraken"
 - "kraken-build"
 - "kraken-filter"
 - "kraken-mpa-report"
 - "kraken-report"
 - "kraken-translate"
 - "jellyfish"
 - "perl5.26.2"
 - "podselect"
versions:
 - "0.10.5ea.3--pl526ha92aebf_3"
description: "shpc-registry automated BioContainers addition for kraken-ea"
config: {"url": "https://biocontainers.pro/tools/kraken-ea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kraken-ea", "latest": {"0.10.5ea.3--pl526ha92aebf_3": "sha256:1132b67ea0367f52f127c0c1111b09d5672760a964a0ac0ffcd178dffb9633a3"}, "tags": {"0.10.5ea.3--pl526ha92aebf_3": "sha256:1132b67ea0367f52f127c0c1111b09d5672760a964a0ac0ffcd178dffb9633a3"}, "docker": "quay.io/biocontainers/kraken-ea", "aliases": {"kraken": "/usr/local/bin/kraken", "kraken-build": "/usr/local/bin/kraken-build", "kraken-filter": "/usr/local/bin/kraken-filter", "kraken-mpa-report": "/usr/local/bin/kraken-mpa-report", "kraken-report": "/usr/local/bin/kraken-report", "kraken-translate": "/usr/local/bin/kraken-translate", "jellyfish": "/usr/local/bin/jellyfish", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kraken-ea.
shpc-registry automated BioContainers addition for kraken-ea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kraken-ea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kraken-ea:0.10.5ea.3--pl526ha92aebf_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kraken-ea/0.10.5ea.3--pl526ha92aebf_3
$ module help quay.io/biocontainers/kraken-ea/0.10.5ea.3--pl526ha92aebf_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kraken-ea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kraken-ea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kraken-ea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kraken-ea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kraken-ea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kraken-ea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kraken

```bash
$ singularity exec <container> /usr/local/bin/kraken
$ podman run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-build

```bash
$ singularity exec <container> /usr/local/bin/kraken-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-filter

```bash
$ singularity exec <container> /usr/local/bin/kraken-filter
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-mpa-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-mpa-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-mpa-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-report

```bash
$ singularity exec <container> /usr/local/bin/kraken-report
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken-translate

```bash
$ singularity exec <container> /usr/local/bin/kraken-translate
$ podman run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken-translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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